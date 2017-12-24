#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
import sys
import traceback
import unittest
from input_picker import (
    pick_bool, pick_item, pick_method,
    Stop, Help
)


class Test(unittest.TestCase):
    def test_bool(self):
        return
        self.assertTrue(pick_bool())
        self.assertFalse(pick_bool())
        with self.assertRaises(Stop):
            pick_bool()
        with self.assertRaises(Help):
            pick_bool()

    def test_item(self):
        return
        source = ['abc', 'efg']
        self.assertEqual(pick_item(source), 0)
        self.assertEqual(pick_item(source, defidx=0), 0)
        self.assertEqual(pick_item(source), 1)
        with self.assertRaises(Stop):
            pick_item(source)
        with self.assertRaises(Help):
            pick_item(source)

    def test_method(self):
        class A:
            def a(self):
                pass
            @staticmethod
            def b():
                pass
            @classmethod
            def c(cls):
                pass
        pick_method(A)
        pick_method(A())


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        unittest.main()
    except Exception:
        traceback.print_exc()
        input()

if __name__ == '__main__':
    main()
