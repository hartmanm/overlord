# appengine_config.py
from google.appengine.ext import vendor

#import os

# Add any libraries install in the "lib" folder.
#vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
vendor.add('lib')

#import requests
#import sendgrid
