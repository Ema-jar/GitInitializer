# Contains all the function used to manage the config file

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')


# Returns the value for a given parameter
def get(section, key):
    parameter = parser.get(section, key)
    return parameter


# Returns a map containing the configurations
def get_all():
    config_map = {}
    for section in parser.sections():
        section_map = {}
        for (key, val) in parser.items(section):
            section_map[key] = val

        config_map[section] = section_map

    return config_map
