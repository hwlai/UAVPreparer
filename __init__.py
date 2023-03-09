# -*- coding: utf-8 -*-
"""
/***************************************************************************
 UAVPreparer
                                 A QGIS plugin
 This plugin examines height properties on a DSM
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-03-09
        copyright            : (C) 2023 by Hui-Wen Lai
        email                : hui-wen.lai@gu.se
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
    """Load UAVPreparer class from file UAVPreparer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .uav_preparer import UAVPreparer
    return UAVPreparer(iface)
