#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/mylocalcovidCANADA')# /  /home/username/ExampleFlask/')
from covid_portal_app import app as application
# application.secret_key = 'anything you wish'

