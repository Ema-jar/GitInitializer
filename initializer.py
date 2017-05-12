#!/usr/bin/python

import sys
import subprocess
import random
import string
import os
import time

BASE_PATH = sys.argv[2]
BASE_GIT = 'git -C ' + BASE_PATH

# Append a given string to a file
def update_file(filename, string_to_append):
    subprocess.Popen('[' + time.time() + '] -> ' + string_to_append, shell=True)
    return

# Creates an empty folder (if it doesn't exist) and initialize a git repo in it
def init_git_repo(path):
    if not os.path.exists(path):
        os.makedirs(path)
    
    subprocess.Popen(BASE_GIT + path + ' init ', shell=True)
    return

# Resets the branch on master
def reset(path):
    subprocess.Popen(BASE_GIT + path + ' checkout master')
    return

# Creates a new branch
def create_branch(branch_name):
    subprocess.Popen(BASE_GIT + ' branch ' + branch_name)
    return

# Check out on a new branch
def checkout(branch_name):
    subprocess.Popen(BASE_GIT + ' checkout ' + branch_name)
    return

command = sys.argv[1]

init_git_repo(path)

if command == 'random':
    n_of_branches = int(sys.argv[3])
    max_n_of_commits = int(sys.argv[4])

    print 'Creating: ', n_of_branches, ' branches.'
    print 'Max number of commits on each branch: ', max_n_of_commits

    for i in range(1, n_of_branches + 1):
        branch_name = 'new_branch_' + str(i)
        create_branch(branch_name)

        filename = 'file_in_branch_' + str(i) + '.txt'
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        update_file(filename, random_string)

print 'Inviati ' , len(sys.argv), ' arguments'
print 'Arguments: ', str(sys.argv)
