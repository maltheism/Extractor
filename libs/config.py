import os
import sys


class Settings:
    def __init__(self):
        pass

    # url of loris instance.
    url = 'https://preventad-open-dev.loris.ca'
    # username for loris.
    username = 'dave'
    # password for loris.
    password = 'mnwi!k2)'
    # enable debug mode.
    debug = True

    # disables print if debug false.
    @staticmethod
    def debugger():
        if not Settings.debug:
            # disable print.
            sys.stdout = open(os.devnull, 'w')
        else:
            # enable print.
            sys.stdout = sys.__stdout__
