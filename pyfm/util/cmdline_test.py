#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import unittest
import logging


from .cmdline import CMDLine
from .exception import ParameterError


logger = logging.getLogger(__file__)


class TestCMDLine(unittest.TestCase):
    """Unit Test class for CMDLine."""

    def test_cmdline(self):
        args = ['--help', '--schema', '1,2,3', '-input', 'input_file_name']
        cmd = self.prepare()

        logger.info("cmd print help information as follow")
        logger.info(cmd)

        logger.info("Args: {}".format(args))
        cmd.parse_args(args)

        with self.assertRaisesRegexp(ParameterError,
                                     "Not Found Parameter output "
                                     "Value and without default value"):
            cmd.get_value('output')

        self.assertEqual(cmd.get_value('help'), "")
        self.assertEqual(cmd.get_values('schema'), ['1', '2', '3'])
        self.assertEqual(cmd.get_int_values('schema'), [1, 2, 3])
        self.assertEqual(cmd.get_str_values('input'), ['input_file_name'])

    @staticmethod
    def prepare():
        cmdline = CMDLine()
        cmdline.register_parameter('help', 'print help information')
        cmdline.register_parameter('schema', 'name1,name2,name3 data schema')
        cmdline.register_parameter('input', 'input filename')
        cmdline.register_parameter('output', 'output filename')
        return cmdline

