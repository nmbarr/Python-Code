#!/bin/bash

function create() {

    source .env
    python create_git_repo.py $1
    cd $FILEPATH$1
    echo "$GIT_USER"
    # git init 
    # git remote add origin git@github.com:$USERNAME/$1.git
    # touch README.md
    # git add .
    # git commit -m "Initial commit"
    # git push -u origin master
    # code .
}