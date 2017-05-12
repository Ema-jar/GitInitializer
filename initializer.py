#!/usr/bin/python

import sys
import subprocess
import random
import string

def update_file(filename, branch):
    subprocess.Popen('git checkout ' + branch, shell=True)
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    subprocess.Popen(''.join(['(', branch, ') -> ', random_string]), shell=True)
    return

command = sys.argv[1]
if command == 'random':
    n_of_branches = int(sys.argv[2])
    max_n_of_commits = int(sys.argv[3])

    print 'Creating: ', n_of_branches, ' branches.'
    print 'Max number of commits on each branch: ', max_n_of_commits

    for i in range(1, n_of_branches + 1):
        branch_name = 'new_branch_' + str(i)
        subprocess.Popen('git branch ' + branch_name, shell=True)

        filename = ''.join(['file_in_branch_', str(i), '.txt'])
        update_file(filename, branch_name)

print 'Inviati ' , len(sys.argv), ' arguments'
print 'Arguments: ', str(sys.argv)
