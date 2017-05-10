#!/usr/bin/python

import sys
import subprocess

command = sys.argv[1]
if command == 'random':
    n_of_branches = sys.argv[2]
    max_n_of_commits = sys.argv[3]

    print 'Creating: ', n_of_branches, ' branches.'
    print 'Max number of commits on each branch: ', max_n_of_commits


    create_branch = 'git branch new_branch'
    subprocess.Popen(create_branch, shell=True)




print 'Inviati ' , len(sys.argv), ' arguments'
print 'Arguments: ', str(sys.argv)
