#!/usr/bin/python

import sys
import random
import string
import common_git_functions as git
import check_params as check
import config_manager as config
from ConfigParser import SafeConfigParser


# Executes the command to generate a simple configuration with commit and branches
def simple_command(branches, commits):
    git.init_git_repo()

    for i in range(1, branches + 1):

        # create new branch
        branch_name = 'new_branch_' + str(i)
        git.create_branch(branch_name)

        # checkout on the created branch
        git.checkout(branch_name)

        for j in range(0, commits):
            # create a new file
            filename = 'file_in_branch_' + str(i) + '.txt'
            random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            git.update_file(filename, random_string)

            # commit that file
            git.commit()

        # come back to master
        git.reset()

    # master moves ahead
    git.checkout('master')
    git.update_file('file_in_master.txt', '[master] Last commit on master')
    git.commit()

    return


# Executes the command to generate branches and commit based on the user input
def custom_command(couples):
    git.init_git_repo()

    for single_couple in couples:
        parameter_couple = single_couple.replace('(', '').replace(')', '').split(',')
        branch_name = parameter_couple[0]
        commits = int(parameter_couple[1])

        git.create_branch(branch_name)
        git.checkout(branch_name)

        for j in range(0, commits):
            # create a new file
            filename = 'file_in_branch_' + str(branch_name) + '.txt'
            random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            git.update_file(filename, random_string)

            # commit that file
            git.commit()

        git.reset()

    # master moves ahead
    git.checkout('master')
    git.update_file('file_in_master.txt', '[master] Last commit on master')
    git.commit()

    return


# Executes the command to generate random branches and commit
def random_command(max_number_of_branches, max_number_of_commits):
    git.init_git_repo()

    branches = random.randint(1, max_number_of_branches)

    for i in range(1, branches + 1):

        # create new branch
        branch_name = 'new_branch_' + str(i)
        git.create_branch(branch_name)

        # checkout on the created branch
        git.checkout(branch_name)

        commits = random.randint(1, max_number_of_commits)

        for j in range(0, commits):
            # create a new file
            filename = 'file_in_branch_' + str(i) + '.txt'
            random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            git.update_file(filename, random_string)

            # commit that file
            git.commit()

        # come back to master
        git.reset()

    # master moves ahead
    git.checkout('master')
    git.update_file('file_in_master.txt', '[master] Last commit on master')
    git.commit()

    return


def help_command():
    check.print_usage()
    return


# Prints the retrieved configuration in a formatted way
def show_conf():
    configs = config.get_all()
    print configs
    return

if __name__ == '__main__':

    parser = SafeConfigParser().read('config.ini')

    parameters = sys.argv[:]
    parameters.pop(0)
    if check.check_params(parameters):

        command = sys.argv[1]

        if command == 'random':
            random_branches = random.randint(int(parser.get('random_mode', 'min_branch')), int(parser.get('random_mode', 'max_branch')))
            random_commits = random.randint(int(parser.get('random_mode', 'min_commit')), int(parser.get('random_mode', 'max_commit')))

            print('\x1b[2;30;42m' + 'COMMAND: ' + command + ' ' + str(random_branches) + ' ' + str(random_commits) + '\x1b[0m')
            random_command(random_branches, random_commits)
            print('\x1b[2;30;42m' + 'SUCCESS!' + '\x1b[0m')

        if command == 'simple':
            n_of_branches = int(parameters[0])
            n_of_commits = int(parameters[1])

            print('\x1b[2;30;42m' + 'COMMAND: ' + command + ' ' + str(n_of_branches) + ' ' + str(n_of_commits) + '\x1b[0m')
            simple_command(n_of_branches, n_of_commits)
            print('\x1b[2;30;42m' + 'SUCCESS!' + '\x1b[0m')

        if command == 'custom':
            print('\x1b[2;30;42m' + 'COMMAND: ' + command + ' ' + str(parameters) + '\x1b[0m')
            custom_command(parameters)
            print('\x1b[2;30;42m' + 'SUCCESS!' + '\x1b[0m')

        if command == '--help':
            help_command()

        if command == 'edit-conf':
            edit_conf(parameters)

        if command == 'show-conf':
            show_conf()

