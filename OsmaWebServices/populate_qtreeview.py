from PyQt4.QtGui import *
from PyQt4.QtCore import *

__author__ = 'matthew.walsh'


class PopulateTree:
    """Deals with populating and searching the WMS/WMTS tree views."""
    def __init__(self, treeview):
        # local class reference
        self.treeview = treeview

    # Create proxy model for filtering and main model for data
        self.proxyModel = LeafFilterProxyModel()
        self.sourceModel = QStandardItemModel()

        # Set main model as source for the proxy model
        self.proxyModel.setSourceModel(self.sourceModel)

        # Set proxy model as data source for qtreeview
        self.treeview.setModel(self.proxyModel)
        self.treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def add_layers(self, layers):
        # Set header of source model
        self.sourceModel.setHorizontalHeaderLabels(["Available Layers"])

        # Create greyscale/colour root items
        colour_cat = QStandardItem()
        colour_cat.setText("Colour")
        self.sourceModel.setItem(0, 0, colour_cat)
        grey_cat = QStandardItem()
        grey_cat.setText("Greyscale")
        self.sourceModel.setItem(1, 0, grey_cat)

        # Add layers_wms to correct category
        for layer in layers:
            print layer
            data = layer.get('name')
            title = layer.get('title')
            new_item = QStandardItem()
            new_item.setText(title)
            new_item.setData(data, Qt.UserRole)
            if "grey" in title or "grey" in data:
                grey_cat.insertRow(0, new_item)
            else:
                colour_cat.insertRow(0, new_item)

        # Sort alphabetically and expand roots
        colour_cat.sortChildren(0)
        grey_cat.sortChildren(0)
        self.treeview.expandAll()

    def filter_layers(self, string):
        # remove selection if one row is selected
        self.treeview.clearSelection()

        # self.currentLayer = None
        self.proxyModel.setFilterKeyColumn(0)
        self.proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxyModel.setFilterFixedString(string)
        self.treeview.expandAll()


class LeafFilterProxyModel(QSortFilterProxyModel):
    """Class to override the following behaviour:
            If a parent item doesn't match the filter,
            none of its children will be shown.
        This Model matches items which are descendants
        or ascendants of matching items."""

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
        """Traverse to the root node and check if any of the
            ancestors match the filter"""
        while parent.isValid():
            if self.filter_accepts_row_itself(parent.row(), parent.parent()):
                return True
            parent = parent.parent()
        return False

    def has_accepted_children(self, row_num, parent):
        """Starting from the current node as root, traverse all
            the descendants and test if any of the children match"""
        model = self.sourceModel()
        source_index = model.index(row_num, 0, parent)
        children_count = model.rowCount(source_index)
        for i in xrange(children_count):
            if self.filterAcceptsRow(i, source_index):
                return True
        return False
