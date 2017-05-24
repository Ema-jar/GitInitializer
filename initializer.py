#!/usr/bin/python

import sys
import random
import string
import common_git_functions as git
import check_params as check


# Executes the command to generate a simple configuration with commit and branches
def simple_command(n_of_branches, n_of_commits):

    git.init_git_repo()

    for i in range(1, n_of_branches + 1):

        # create new branch
        branch_name = 'new_branch_' + str(i)
        git.create_branch(branch_name)

        # checkout on the created branch
        git.checkout(branch_name)

        for j in range(1, n_of_commits):
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
    git.update_file('file_in_master.txt', '[master] Fast commit on master')
    git.commit()

    return

# Executes the command to generate branches and commit based on the user input
def custom_command(branches):
    return

if __name__ == '__main__':

    parameters = sys.argv[:]
    parameters.pop(0)
    check.check_params(parameters)

    command = sys.argv[1]

    if command == 'random':
        random_branches = random.randint(3, 5)
        random_commits = random.randint(2, 5)
        simple_command(random_branches, random_commits)

    if command == 'simple':
        simple_command(int(sys.argv[2]), int(sys.argv[3]))

    if command == 'custom':
        custom_command(sys.argv)

    print('End of ' + __name__)
