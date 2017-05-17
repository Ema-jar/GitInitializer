#!/usr/bin/python

import sys
import random
import string
import common_git_functions as git


# Executes the command to generate random commit and branches
def random_command(n_of_branches, max_n_of_commits):

    git.init_git_repo()

    for i in range(1, n_of_branches + 1):

        # create new branch
        branch_name = 'new_branch_' + str(i)
        git.create_branch(branch_name)

        # checkout on the created branh
        git.checkout(branch_name)

        for j in range(1, max_n_of_commits):
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

if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'random':
        random_command(int(sys.argv[3]), int(sys.argv[4]))

    print('End of ' + __name__)
