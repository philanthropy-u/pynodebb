#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pynodebb/client.py

Copyright (c) 2015 David Vuong <david.vuong256@gmail.com>
Licensed MIT
"""
from __future__ import unicode_literals
from pynodebb.http_client import HttpClient

from pynodebb.api.users import User
from pynodebb.api.topics import Topic
from pynodebb.api.groups import Group
from pynodebb.api.categories import Category


class Client(object):
    def __init__(self, endpoint, token, admin_uid=None):
        http_client = HttpClient(endpoint, token, admin_uid)

        self.users = User(http_client)
        self.topics = Topic(http_client)
        self.groups = Group(http_client)
        self.categories = Category(http_client)
