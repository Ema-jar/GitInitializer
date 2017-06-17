# Contains all the function used to manage the config file

from ConfigParser import SafeConfigParser

parser = SafeConfigParser().read('config.ini')


# Returns a map that contains the config file
def get_all():
    config_map = {}
    for section in parser.sections():
        section_map = {}
        for (key, val) in parser.items(section):
            section_map[key] = val

            config_map[section] = section_map

    return config_map
