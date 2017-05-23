# Contains all the function used to check the inputs from shell


def check_params(params):

    command = params[0]
    params.pop(0)

    if command == 'simple':
        check_simple(params)

    if command == 'random':
        check_random(command)

    return


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

