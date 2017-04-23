import urllib2
import base64
import os
import xml.etree.ElementTree as ElmTree

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from osma_web_services_dialog import MultiWmsDialog

__author__ = 'matthew.walsh'

BASE_MAPCLOUD_URL = 'https://api.themapcloud.com'


def make_mapcloud_request(url, username, password):
    """
    Make a request to the MapCloud.
    :param url: URL to request
    :param username: MC username
    :param password: MC password
    :return: response content, status code
    """
    base64_auth = base64.b64encode('%s:%s' % (username, password))

    request = urllib2.Request(url)
    request.add_header("Authorization", "Basic %s" % base64_auth)
    result_wms = urllib2.urlopen(request)
    return result_wms.read(), result_wms.getcode()


class GetOsmaLayers:

    def get_available_layers(self, username, password):
        """
        Retrieve the WMS/WMTS layer details from there
        respective GetCapabilities docs. Also extract service
        metadata.
        :param mc_auth:
        :return: wms layers dict, wmts layers dict, metadata dict
        """

        base_mc_url = BASE_MAPCLOUD_URL + '/maps'
        wms_getcaps = '/wms?REQUEST=GetCapabilities'
        wmts_getcaps = '/wmts/1.0.0/WMTSCapabilities.xml'

        # Request WMS GetCapabilities
        wms_url = base_mc_url + wms_getcaps
        wms_getcaps_xml, _ = make_mapcloud_request(wms_url, username, password)
        xml_root_wms = ElmTree.fromstring(wms_getcaps_xml)

        # Extract WMS layers and metadata
        layers_wms = self.extract_wms_layers_from_getcapabilities(xml_root_wms)
        about_service_info = self.extract_metadata_from_getcapabilities(xml_root_wms)

        # Request WMTS GetCapabilities
        wmts_url = base_mc_url + wmts_getcaps
        wmts_getcaps_xml, _ = make_mapcloud_request(wmts_url, username, password)
        xml_root_wmts = ElmTree.fromstring(wmts_getcaps_xml)

        # Extract WMTS layers
        layers_wmts = self.extract_wmts_layers_from_getcapabilities(xml_root_wmts)
        return layers_wms, layers_wmts, about_service_info

    def extract_wms_layers_from_getcapabilities(self, xml_root):
        """
        Extract the WMS layers from the WMS
        GetCapabilities XML.
        :param xml_root: XML Element of GetCapabilities
        :return: list of layer dicts
        """
        layers = []

        all_layers = xml_root.findall('./Capability/Layer/Layer')
        for layer in all_layers:

            # Extract title and name
            title = layer.find('./Title').text
            name = layer.find('./Name').text

            # Extract the min and max scale thresholds
            min = None
            max = None
            scale_hint = layer.find('./ScaleHint')
            if scale_hint is not None:
                min = scale_hint.attrib.get('min')
                max = scale_hint.attrib.get('max')

            # Create layer dict entry
            layer_metadata = {'title': title,
                              'name': name,
                              'min_scale': min,
                              'max_scale': max}
            layers.append(layer_metadata)

        return layers

    def extract_metadata_from_getcapabilities(self, xml_root):
        """
        Extract the metadata/contact info from the WMS
        GetCapabilities XML.
        :param xml_root: XML Element of GetCapabilities
        :return: dict of metadata
        """
        service = xml_root.find('./Service')
        contact_info = service.find('./ContactInformation')

        metadata = {
            'abstract': service.find('./Abstract').text,
            'person': contact_info.find('./ContactPersonPrimary/ContactPerson').text,
            'position': contact_info.find('./ContactPosition').text,
            'org': contact_info.find('./ContactPersonPrimary/ContactOrganization').text,
            'address': contact_info.find('./ContactAddress/Address').text,
            'city': contact_info.find('./ContactAddress/City').text,
            'country': contact_info.find('./ContactAddress/Country').text,
            'postcode': contact_info.find('./ContactAddress/PostCode').text,
            'phone': contact_info.find('./ContactVoiceTelephone').text,
            # 'fax': contact_info.find('./ContactFacsimileTelephone').text,
            'email': contact_info.find('./ContactElectronicMailAddress').text,
            'access': service.find('./AccessConstraints').text
        }
        return metadata

    def extract_wmts_layers_from_getcapabilities(self, xml_root):
        """
        Extract the WMTS layers from the WMTS
        GetCapabilities XML.
        :param xml_root: XML Element of GetCapabilities
        :return: list of layer dicts
        """
        layers = []
        # ns = {
        #     'ows': 'http://www.opengis.net/ows/1.1',
        #     'xmlns': 'http://www.opengis.net/wmts/1.0',
        # }
        # for prefix, uri in ns.items():
        #     xml_root.register_namespace(prefix, uri)
        all_layers = xml_root.findall('./{http://www.opengis.net/wmts/1.0}Contents/'
                                      '{http://www.opengis.net/wmts/1.0}Layer')

        for layer in all_layers:

            # Create layer dict entry
            title = layer.find('./{http://www.opengis.net/ows/1.1}Title').text
            grid = layer.find('./{http://www.opengis.net/wmts/1.0}TileMatrixSetLink/{http://www.opengis.net/wmts/1.0}TileMatrixSet').text
            name = layer.find('./{http://www.opengis.net/ows/1.1}Identifier').text

            layer_metadata = {'title': title,
                              'name': name,
                              'grid': grid,
                              'min_scale': None,
                              'max_scale': None}
            layers.append(layer_metadata)

        return layers


class PreviewButton(QStyledItemDelegate):
    """
    Custom delegate to add a push button to a
    """
    buttonClicked = pyqtSignal(QModelIndex)

    def __init__(self, sourcemodel, proxymodel, iface, parent=None):
        super(PreviewButton, self).__init__(parent)
        self.sourcemodel = sourcemodel
        self.proxymodel = proxymodel
        self.iface = iface
        self._pressed = None
        self.buttonClicked.connect(self.show_preview)

    def paint(self, painter, option, index):
        # Reimplementing the default paint function
        data = index.data(Qt.UserRole)
        try:
            if data[0] == "preview":
                button_options = QStyleOptionButton()
                button_options.text = "preview"
                # button_options.rect = option.rect
                left = option.rect.left()
                top = option.rect.top()
                height = option.rect.height()
                width = 80
                button_options.rect = QRect(left, top, width, height)
                button_options.palette = option.palette

                if self._pressed and self._pressed == (index.row(), index.column()):
                    button_options.state = QStyle.State_Enabled | QStyle.State_Sunken
                else:
                    button_options.state = QStyle.State_Enabled | QStyle.State_Raised

                QApplication.style().drawControl(QStyle.CE_PushButton, button_options, painter)
            else:
                QStyledItemDelegate.paint(self, painter, option, index)
        except TypeError:
            # TypeError catches all data which is not a tuple
            QStyledItemDelegate.paint(self, painter, option, index)

    def editorEvent(self, event, model, option, index):
        # Catch button push and send signal with position
        if event.type() == QEvent.MouseButtonPress:
            # store the position that is clicked
            self._pressed = (index.row(), index.column())
            return True
        elif event.type() == QEvent.MouseButtonRelease:
            if self._pressed == (index.row(), index.column()):
                # we are at the same place, so emit
                self.buttonClicked.emit(index)
            elif self._pressed:
                old_index = index.model().index(index, *self._pressed)
                self._pressed = None
                index.model().dataChanged.emit(old_index, old_index)
            self._pressed = None
            return True
        else:
            # for all other cases, default action will be fine
            return super(PreviewButton, self).editorEvent(event, model, option, index)

    def show_preview(self, index):
        # Display preview tile of mapping product with custom dialog
        try:
            # get layername from data tuple
            layer = index.data(Qt.UserRole)[1]

            # Construct path to image
            f_layer = r"osma_tile_previews/" + str(layer) + ".png"  # TODO: Change to use resources_rc
            plugin_dir = os.path.dirname(__file__)
            image_path = os.path.join(plugin_dir, f_layer)
            if not os.path.exists(image_path):
                image_path = os.path.join(plugin_dir, r"osma_tile_previews/no_preview.png")

            # Construct pixmap and load image from file
            image = QPixmap()
            image.load(image_path)

            # send pixmap to custom qdialog
            image_dlg = PreviewDialog(image, self.iface.mainWindow)
            image_dlg.show()
        except TypeError:
            pass


class PreviewDialog(QDialog):
    """Custom Qdialog for displaying tile preview, mimics Windows UAC style dialog"""

    def __init__(self, image, parent=None):
        super(PreviewDialog, self).__init__(parent)

        pixmap = image
        # Get screen size and set qdialog size
        desktop = QDesktopWidget().screenGeometry()
        self.setGeometry(desktop)
        self.setModal(False)

        # Set qdialog to be black and transparent
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.setWindowOpacity(0.65)
        self.setStyleSheet("background: 'black'")

        # Set QGraphicsView to screen size
        g_view = QGraphicsView(self)
        g_view.setGeometry(desktop)

        # Disable scroll bars
        g_view.setHorizontalScrollBarPolicy(1)
        g_view.setVerticalScrollBarPolicy(1)

        # Create and set graphics scene
        scn = QGraphicsScene(g_view)  # TODO: image should not have the same transparency a background of dlg
        scn.addPixmap(pixmap)
        g_view.setScene(scn)

    def keyPressEvent(self, qkeyevent):
        # Close dialog on any key press event
        self.close()

    def mousePressEvent(self, *args, **kwargs):
        # Close dialog on mouse click
        self.close()


class PopulateTree:
    """Deals with populating and searching the WMS/WMTS tree views"""

    def __init__(self, dock, iface, mc_auth, wms):
        # local class reference
        self.wms = wms
        self.dock = dock
        self.iface = iface
        # Create single instance of AddToCanvas so number increment works
        self.add_layer = AddToCanvas(self.iface, self.dock)
        self.mc_auth = mc_auth

        if self.wms:
            self.treeview = self.dock.wmsTreeView
            self.dock.addWmsButton.clicked.connect(self.get_item_data)
        else:
            self.treeview = dock.wmtsTreeView
            self.dock.addWmtsButton.clicked.connect(self.get_item_data)

        # self.treeview.setScrollBarPolicy(Qt.Horizontal, Qt.ScrollBarAlwaysOff)

        # Create proxy model for filtering and main model for data
        self.proxyModel = LeafFilterProxyModel(self.iface)
        self.sourceModel = QStandardItemModel()
        self.sourceModel.setColumnCount(2)

        # Hookup custom delegate for push puttons to be painted in second column
        self.treeview.setItemDelegateForColumn(1, PreviewButton(iface, self.sourceModel, self.proxyModel))

        # Set main model as source for the proxy model
        self.proxyModel.setSourceModel(self.sourceModel)

        # Set proxy model as data source for qtreeview
        self.treeview.setModel(self.proxyModel)
        self.treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set header of source model and col width
        self.sourceModel.setHorizontalHeaderLabels(["Available Layers", "Tile Preview"])
        self.treeview.setColumnWidth(0, 210)
        self.treeview.setColumnWidth(1, 80)

        # Connect double click event
        self.treeview.doubleClicked.connect(self.get_item_data)

    def get_item_data(self, model_index=None):
        # Use QModelIndex to map to sourceModel, retrieve data and then pass to add wms/wmts
        data = []
        if model_index:
            # Deals with layer added from double click
            index_data = model_index.data(Qt.UserRole)
            if index_data:
                all_data = (model_index.data(), index_data)
                data.append(all_data)
        else:
            # Deals with layer added from button
            sel_indexes = self.treeview.selectedIndexes()
            for each_index in sel_indexes:
                # Get item from the first col (not preview)
                if not each_index.data() == "preview":
                    zero_index_data = each_index.data(Qt.UserRole)
                    all_data = (each_index.data(), zero_index_data)
                    data.append(all_data)

        username = self.mc_auth.username
        password = self.mc_auth.password

        if self.wms:
            self.add_layer.add_wms(data, username, password)
        else:
            self.add_layer.add_wmts(data, username, password)

    def add_layers(self, layers):

        # Create greyscale/colour root items
        colour_cat = QStandardItem()
        colour_cat.setText("Colour")
        self.sourceModel.setItem(0, 0, colour_cat)
        grey_cat = QStandardItem()
        grey_cat.setText("Greyscale")
        self.sourceModel.setItem(1, 0, grey_cat)

        # Add layers_wms to correct category
        for layer in layers:
            data = layer.get('name')
            title = layer.get('title')
            if "grey" in str(title).lower():
                title = title.replace("Greyscale", "")
            if not self.wms:
                grid = layer.get('grid')
                data = (data, grid)
            new_item = QStandardItem()
            new_item.setText(title)
            new_item.setData(data, Qt.UserRole)

            btn = QStandardItem()
            btn.setData(("preview", layer.get('name')), Qt.UserRole)
            btn.setText("preview")

            if "grey" in str(data):
                grey_cat.appendRow([new_item, btn])
            else:
                colour_cat.appendRow([new_item, btn])

        # Sort alphabetically and expand roots
        colour_cat.sortChildren(0)
        grey_cat.sortChildren(0)
        self.treeview.expandAll()

    def filter_layers(self, string):
        # remove selection if one row is selected
        self.treeview.clearSelection()
        self.proxyModel.setFilterKeyColumn(0)
        self.proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxyModel.setFilterFixedString(string)
        self.treeview.expandAll()

    def preview_column(self, ischecked):
        # Show/hide preview column
        if ischecked:
            self.treeview.showColumn(1)
            self.treeview.setColumnWidth(0, 210)
            self.treeview.setColumnWidth(1, 80)
            QSettings().setValue("OsmaWebServices/Preview", "True")
        else:
            self.treeview.hideColumn(1)
            QSettings().setValue("OsmaWebServices/Preview", "False")

    def clear_tree(self):
        pass


class LeafFilterProxyModel(QSortFilterProxyModel):
    """Class to override the following behaviour: If a parent item doesn't match the filter,
    none of its children will be shown. This Model matches items which are descendants
    or ascendants of matching items."""

    def __init__(self, iface, parent=None):
        # Main window required here to open preview dlg
        self.mainWindow = iface.mainWindow()
        super(LeafFilterProxyModel, self).__init__(parent)

    def filterAcceptsRow(self, row_num, source_parent):
        """Overriding the parent function"""

        # Check if the current row matches
        if self.filter_accepts_row_itself(row_num, source_parent):
            return True
        # Traverse up all the way to root and check if any of them match
        if self.filter_accepts_any_parent(source_parent):
            return True
        # Finally, check if any of the children match
        return self.has_accepted_children(row_num, source_parent)

    def filter_accepts_row_itself(self, row_num, parent):
        return super(LeafFilterProxyModel, self).filterAcceptsRow(row_num, parent)

    def filter_accepts_any_parent(self, parent):
        """Traverse to the root node and check if any of the ancestors match the filter"""
        while parent.isValid():
            if self.filter_accepts_row_itself(parent.row(), parent.parent()):
                return True
            parent = parent.parent()
        return False

    def has_accepted_children(self, row_num, parent):
        """Starting from the current node as root, traverse all the descendants and test if
        any of the children match"""
        model = self.sourceModel()
        source_index = model.index(row_num, 0, parent)
        children_count = model.rowCount(source_index)
        for i in xrange(children_count):
            if self.filterAcceptsRow(i, source_index):
                return True
        return False


class AddToCanvas:
    """Add layers_wms to QGIS map canvas"""

    def __init__(self, iface, dock):
        self.iface = iface
        self.dock = dock
        self.layer_n = None
        self.layers_ordered = []
        self.multi_l_count = 0
        self.order_layers = MultiWmsDialog()
        self.order_layers.ui.layerOrderPushButton.clicked.connect(self.store_user_title_and_order)

    def store_user_title_and_order(self):
        # Store user input title for multi wms
        self.layer_n = self.order_layers.ui.displayNameLineEdit.text()
        layer_list_widget = self.order_layers.ui.layerOrderListWidget
        for index in xrange(layer_list_widget.count()):
            self.layers_ordered.append(
                (layer_list_widget.item(index).text(), layer_list_widget.item(index).data(Qt.UserRole)))
        self.order_layers.close()

    def title_and_order(self, data):
        # Opens dlg for user to input layer name, creates generic if not provided
        self.order_layers.ui.layerOrderListWidget.clear()
        for d in data:
            print d
            item = QListWidgetItem()
            item.setText(d[0])
            item.setData(Qt.UserRole, d[1])
            self.order_layers.ui.layerOrderListWidget.addItem(item)
        self.order_layers.exec_()
        if self.layer_n:
            return self.layer_n
        else:
            self.multi_l_count += 1
            title = "MultipleWMSLayer_" + str(self.multi_l_count)
            return title

    def add_wms(self, data, username, password):
        self.reset()
        # Add wms layer to map canvas
        if data:
            if len(data) == 1:
                # Add single WMS layer to canvas
                title = str(data[0][0])
                layer = str(data[0][1])
                if "grey" in layer.lower():
                    title += "Greyscale"
                url = "contextualWMSLegend=0&crs=EPSG:27700&dpiMode=7&featureCount=10&format=image/png" \
                      "&layers={0}&styles=default&url={1}/maps/wms&password={2}" \
                      "&username={3}".format(layer, BASE_MAPCLOUD_URL,password, username)
            else:
                # Adds multiple layers_wms to canvas as single layer
                title = self.title_and_order(data)
                layers = []
                styles = ""
                if self.layers_ordered:
                    data = self.layers_ordered
                for layer_t in data:
                    layer = str(layer_t[1]) + "&layers_wms="
                    layers.append(layer)
                    styles += "&styles="
                layers_clean = "".join(layers)[:-8]
                url = "contextualWMSLegend=0&crs=EPSG:27700&dpiMode=7&featureCount=10&format=image/png" \
                      "&layers_wms={0}{1}&url={2}/maps/wms&password={3}" \
                      "&username={4}".format(layers_clean, styles, BASE_MAPCLOUD_URL, password, username)
            self.iface.addRasterLayer(url, title, "wms")
            self.zoom_to_extent()

    def add_wmts(self, data, username, password):
        # Add wmts layer to canvas
        self.reset()
        for layer_t in data:
            title = str(layer_t[0])
            layer = str(layer_t[1][0])
            grid = str(layer_t[1][1])

            if "grey" in layer.lower():
                title += " Greyscale"
            url = r"crs=EPSG:27700&dpiMode=7&featureCount=10&format=image/png&layers={0}&" \
                  r"styles=default&tileMatrixSet={4}&url={1}/maps/wmts/1.0.0/WMTSCapabilities.xml&" \
                  r"password={2}&username={3}".format(layer, BASE_MAPCLOUD_URL, password, username, grid)

            self.iface.addRasterLayer(url, title, "wms")
        self.zoom_to_extent()

    def zoom_to_extent(self):
        # If checkbox is ticked then zoom to layer extent
        if self.dock.zoomExtentWmsBox.isChecked():
            self.iface.zoomToActiveLayer()

    def reset(self):
        # Reset for adding a new layer
        self.layers_ordered = []
        self.layer_n = ""
