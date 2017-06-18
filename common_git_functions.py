# Contains all the common functions used to interact with your git repository

import subprocess
import time
import os

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
