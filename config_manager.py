# Contains all the function used to manage the config file

from ConfigParser import SafeConfigParser

parser = SafeConfigParser().read('config.ini')


# Edits the values in config.ini
def edit(params):
    return


# Returns the value for a single param saved in config.ini
def get(param, under=None):
    parser.get(under, param)
    return
