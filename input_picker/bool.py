#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .common import Option, ExceptionOption, Picker, Stop, Help


def pick_bool(defval: bool=True,
        raise_on_help: bool=True) -> bool:
    ''' pick a bool value. '''
    if not isinstance(defval, bool):
        raise TypeError('defval must be a bool value')
    options = Picker(sep='  ')
    options.add(Option('Yes', ['Y', 'yes'], True))
    options.add(Option('No', ['N', 'no'], False))
    options.add(ExceptionOption('Stop', ['S', 'stop'], Stop))
    if raise_on_help:
        options.add(ExceptionOption('Help', ['?', 'H'], Help))
    else:
        options.add(Option('Help', ['?', 'H'], Help))
    return options.pick(defval)
