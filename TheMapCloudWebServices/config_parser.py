import ConfigParser
from os import path


def parse_config_from_file():
    """
    Parse the plugin configuration from a
    file.
    :return: dict of config
    """
    config = ConfigParser.ConfigParser()
    dir_path = path.dirname(path.realpath(__file__))
    config.read(path.join(dir_path, 'plugin.cfg'))
    name = config.get('plugin_configuration', 'name')
    title = config.get('plugin_configuration', 'title')
    help_url = config.get('plugin_configuration', 'help_url')

    config_dict = {
        'name': name,
        'title': title,
        'help_url': help_url
    }
    return config_dict
