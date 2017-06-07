# Contains all the function used to check the inputs from shell


def check_params(params):

    command = params[0]
    params.pop(0)

    if command == 'simple':
        return check_simple(params)

    if command == 'random':
        return check_random(params)

    if command == 'custom':
        return check_custom(params)

    return False


# SIMPLE takes two params n_of_branches and n_of_commits
def check_simple(params):
    if len(params) != 2:
        print 'Expected 2 parameters for SIMPLE action, ' + len(params) + ' where found'
        return False
    else:
        are_numbers = params[0].isdigit() & params[1].isdigit()
        if not are_numbers:
            print 'Expected parameters for SIMPLE to be integers'
            return False

    return True


# RANDOM takes no parameters
def check_random(params):
    if len(params) != 0:
        print 'Expected no parameters for RANDOM action, ' + len(params) + ' where found'
        return False

    return True


# CUSTOM takes any number of couples like this -> (branch_name, number_of_commits)
def check_custom(params):
    if len(params) == 0:
        print 'Expected at least one parameter for RANDOM action'
        return False

    return True


# Prints the usage message
def print_usage():
    print 'Usage: initializer.py [simple n_of_branches n_of_commits ] [random] [custom couple ...]'
    return

