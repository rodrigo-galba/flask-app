#!/bin/bash

wget https://github.com/rgalba/flask-app/archive/master.zip
unip master.zip
cd flask-app-master
pip install -r requirements.txt --user