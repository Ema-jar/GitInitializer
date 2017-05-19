# Contains all the function used to check the inputs from shell


def check_params(params):

    command = params[0]
    params.pop(0)

    if command == 'simple':
        check_simple(params)

    if command == 'random':
        check_random(command)

    return


def check_simple(params):
    return


def check_random(params):
    return

