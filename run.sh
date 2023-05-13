#!/bin/bash

cur_path=$(dirname "$(realpath "$0")")

cd $cur_path

source $cur_path/.venv/bin/activate

$cur_path/.venv/bin/python $cur_path/main.py
