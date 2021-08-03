# imports operating system to give us a 'base directory'
import os

# __file__ is current file, surrounded by it's current filepath
# it's parent folder/dir is traced outside of the () with abspath
# programmatic way of finding the current filepath in any OS
basedir = os.path.abspath(os.path.dirname(__file__))

# gives access to the project in ANY OS we find ourselves in
# allows outside files/folders to be added so to the project from
# the base directory.

# "hey, this is where this file is in my computer"
#  - done every time we make a Flask application.

