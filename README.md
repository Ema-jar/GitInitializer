# GitInitializer

GitInitializer is a small python library you can use to generate a git repository whit branches and commits.
I've used GitInitializer to make experiments with git without having to recreate a repo each time.

## Simple mode

`simple n_of_branches n_of_commits`

It is the simplest command and is used to create 
a basic configuration.

**n_of_branches**: the number of branches you 
want to generate in your local repository.

**n_of_commits**: the number of commits on each branch
of your local repository.

#### Example

`simple 3 4`

This command will generate three branches named 
_new_branch_1_, _new_branch_2_ and _new_branch_3_.
Each branch will have 4 commits.

## Random mode

`random`

This command generate a random combination of branches
and commit on your local repository.

## Custom mode

`custom couple ...`

The custom mode allows you to create your own set of
branches and commits providing a list of couples.
Each couple should follow this format:

**(branch_name, number_of_commits)**

#### Example

`custom (first,3) (secon,5)`

This command generates two branches named 
_first_ and _second_. 
The first branch will have 3 commits while the second 
one will have 5 commits.
