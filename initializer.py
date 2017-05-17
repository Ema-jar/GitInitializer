#!/usr/bin/python

import sys
import subprocess
import random
import string
import os
import time

BASE_PATH = '../testGit'
BASE_GIT = 'git -C ' + BASE_PATH
LOG_FILE = 'log.txt'


# Adds all and commits all using git commit command
def commit():
    execute(BASE_GIT + ' add . ')
    execute(BASE_GIT + ' commit -m "date: ' + str(time.time()) + '"')
    return


# Append a given string to a file
def update_file(filename, string_to_append):
    execute('echo "[' + str(time.time()) + '] -> ' + string_to_append + '" >> ' + BASE_PATH + '/' + filename)
    return


# Creates an empty folder (if it doesn't exist) and initialize a git repo in it
def init_git_repo():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
    
    execute(BASE_GIT + ' init ')
    update_file('master_file.txt', '[master] First commit on master')
    commit()

    return


# Resets the branch on master
def reset():
    execute(BASE_GIT + ' checkout master')
    return


# Creates a new branch
def create_branch(branch_name):
    execute(BASE_GIT + ' branch ' + branch_name)
    return


# Check out on a new branch
def checkout(branch_name):
    execute(BASE_GIT + ' checkout ' + branch_name)
    return


# Executes and log a command
def execute(command):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(command + '\n')

    subprocess.Popen(command, shell=True)
    time.sleep(1)

    return


# Executes the command to generate random commit and branches
def random_command(n_of_branches, max_n_of_commits):

    init_git_repo()

    for i in range(1, n_of_branches + 1):

        # create new branch
        branch_name = 'new_branch_' + str(i)
        create_branch(branch_name)

        # checkout on the created branh
        checkout(branch_name)

        for j in range(1, max_n_of_commits):
            # create a new file
            filename = 'file_in_branch_' + str(i) + '.txt'
            random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            update_file(filename, random_string)

            # commit that file
            commit()

        # come back to master
        reset()

    # master moves ahead
    checkout('master')
    update_file('file_in_master.txt', '[master] Fast commit on master')
    commit()

    return

if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'random':
        random_command(int(sys.argv[3]), int(sys.argv[4]))

    print('End of ' + __name__)
