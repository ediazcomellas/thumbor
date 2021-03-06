#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

from . import file_loader
from tornado.concurrent import return_future


@return_future
def load(context, path, callback):
    def callback_wrapper(result):
        if result.successful:
            callback(result)
        else:
            # If file_loader failed try file_loader with fixed "404.png" callback
            file_loader.load(context, '404.png', callback)

    # First attempt to load with file_loader
    file_loader.load(context, path, callback_wrapper)
