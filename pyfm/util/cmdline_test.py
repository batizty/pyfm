#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import unittest
import logging


logger = logging.getLogger(__file__)


class TestCMDLine(unittest.TestCase):
    """Unit Test class for CMDLine."""

    def test_cmdline(self):
        print "hello"
        return
