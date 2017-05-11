#!/usr/bin/python

import sys
import subprocess

command = sys.argv[1]
if command == 'random':
    n_of_branches = int(sys.argv[2])
    max_n_of_commits = int(sys.argv[3])

    print 'Creating: ', n_of_branches, ' branches.'
    print 'Max number of commits on each branch: ', max_n_of_commits

    for i in range(1, n_of_branches + 1):
        create_branch = 'git branch new_branch_' + str(i)
        subprocess.Popen(create_branch, shell=True)





print 'Inviati ' , len(sys.argv), ' arguments'
print 'Arguments: ', str(sys.argv)
