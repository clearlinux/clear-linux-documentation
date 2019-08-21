#! /bin/bash

# run with no arguments
# 1. deletes previous build output
# 2. builds default language version of docs only (English)
# 3. changes directory to html output
# 4. runs http server for local review of docs
#
# Requires python 3 

make clean
make html
cd source/_build/html
python3 -m http.server
