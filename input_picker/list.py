#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
from .common import Option, Picker, Stop, Help


def pick_item(source: typing.List[str], defidx: int=None) -> bool:
    ''' require a bool type input. '''
    if not isinstance(source, list):
        raise TypeError('source must be a list')
    if defidx is not None:
        if not isinstance(defidx, int):
            raise TypeError('defidx must be a int')
        if defidx < 0 or defidx >= len(source):
            raise IndexError

    options = Picker(sep='\n')
    for idx, item in enumerate(source):
        if not isinstance(item, str):
            raise TypeError('all item of source must be a str')
        options.add(Option(item, [str(idx), item], idx))

    options.add(Option('None', ['X', 'none'], -1))
    options.add(Option('Stop', ['S', 'stop'], Stop))
    options.add(Option('Help', ['?', 'H'], Help))
    return options.pick(defidx)
