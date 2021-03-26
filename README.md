# theMapCloud-QGIS-Plugin

## About 

thinkWhere has developed a plugin to make viewing theMapCloud web services more efficient when using the open source desktop GIS package, QGIS.

Features:
- Gazetteer search
- Easily add WMS/WMTS to the canvas
- Preview layers
- Search layers

This plugin is intended for use by consumers and customers of theMapCloud. The use of this plugin is restricted by token authentication. 

## Installing the plugin

The plugin can be installed from the thinkWhere QGIS repository. Navigate to the repository settings :  'Plugins' > 'Manage and in Install plugins' > 'Settings'  

Then add a new repository with the URL:

- *http://qgis.themapcloud.com/plugin.xml*

Alternatively, the plugin can be installed by cloning the repository and placing it in your QGIS plugin folder 
- QGIS2 on Windows: e.g. C:\Users\USERNAME\.qgis2\python\plugins
- QGIS3 on Windows: e.g. C:\Users\USERNAME\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins

## Configuration

The branding and target web service URL are parsed from a config file (plugin.cfg) in the directory of the plugin.

## Support

[theMapCloud API](https://api.themapcloud.com)

[thinkWhere Support](https://support.thinkwhere.com/)



