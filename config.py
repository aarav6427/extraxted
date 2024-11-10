#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7595907385:AAFxOWCPWCa57YrHyS0THz6TbiNRZdY-GK4")
    API_ID = int(os.environ.get("API_ID", "2645474"))
    API_HASH = os.environ.get("API_HASH", "6c9a5044d2f2c2350ac20b3838a7896e")
    AUTH_USERS = "929216155"

