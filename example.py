#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

""" Run this script to get a preview of EzWebScraping.
"""

import time
import logging

from EzWebScraping import EzWebScraping


def main():
    # After inspecting Github's login form, we have :
    # - "login": which is the content of the name attribute of the login
    # input,
    # - "password": which is the content of the name attribute of the
    # password input.
    #
    # - "authenticity_token": (aka csrfmiddlewaretoken or csrf_token for
    # example) We need to put its name in the connect function so we
    # will retrieve it automatically while connecting.

    payload = {  # NEVER PUSH YOUR PERSONAL INFORMATION TO GIT
        "login": "YOUR LOGIN",
        "password": "YOUR PASSWORD"
    }

    scraper = EzWebScraping()
    # The url corresponds to the content of "action" in the <form> tag.
    scraper.connect('http://github.com/session',
                    payload=payload,
                    auth_token_name="authenticity_token")


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s ' +
                                  '-- %(levelname)s ' +
                                  '-- [%(filename)s:%(lineno)s ' +
                                  '-- %(funcName)s() ] ' +
                                  '-- %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    main()
