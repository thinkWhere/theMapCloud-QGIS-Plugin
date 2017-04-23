# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TheMapCloudWebServices
                                 A QGIS plugin
 Easy add OSMA WMS and WMTS layers_wms to QGIS
                             -------------------
        begin                : 2014-11-10
        copyright            : (C) 2014 by thinkWhere
        email                : support@thinkwhere.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TheMapCloudWebServices class from file TheMapCloudWebServices.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .osma_web_services import TheMapCloudWebServices
    return TheMapCloudWebServices(iface)
