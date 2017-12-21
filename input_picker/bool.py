#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .common import Option, Picker, Stop, Help


def pick_bool(defval: bool=True) -> bool:
    ''' pick a bool type input. '''
    assert isinstance(defval, bool)
    options = Picker(sep='  ')
    options.add(Option('Yes', ['Y', 'yes'], True))
    options.add(Option('No', ['N', 'no'], False))
    options.add(Option('Stop', ['S', 'stop'], Stop))
    options.add(Option('Help', ['?', 'H'], Help))
    return options.pick(defval)
