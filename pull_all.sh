#!/bin/bash
# sudo apt-get update
# sudo apt-get install python3-pip
# cd ..
# git clone https://github.com/muhasturk/gitim gitim
# cd gitim
# python3 setup.py build
# sudo python3 setup.py install
# -t <github api key>  -o <organization name> -d <output directory> --ssh  // -ssh to use ssh links for cloning
# export api_key="<put your github api key here>"
python3 -m gitim --ssh -t $api_key -o FIIT-CS311 -d ../submissions 

