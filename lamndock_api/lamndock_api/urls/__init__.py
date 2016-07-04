# -*- coding: utf-8 -*-

import os

from split_settings.tools import optional, include

include(
    'admin.py',
    'lambdock_api.py',
    scope=locals()
)
