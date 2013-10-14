# -*- coding: utf8 - *-
"""
    tmuxp.exc
    ~~~~~~~~~
    :copyright: Copyright 2013 Tony Narlock.
    :license: BSD, see LICENSE for details
"""

class TmuxSessionExists(Exception):
    pass

class ConfigError(Exception):
    pass

class EmptyConfigException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
