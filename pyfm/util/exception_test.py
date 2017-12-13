#!/usr/bin/env python2.7
#   -*- coding:utf-8 -*-

import unittest
import logging

from .exception import ParameterError

class TestParameterError(unittest.TestCase):
	"""Unit Test class for Parameter Error."""
	def test_exception(self):
		with self.assertRaisesRegexp(ParameterError, "message"):
			raise ParameterError("message")

		with self.assertRaisesRegexp(ParameterError, "message"):
			raise ParameterError("message")

		with self.assertRaisesRegexp(ParameterError, 
		"message | Extra Infomation: yy -> 1.0, raw -> value, xx -> 1,"):
			raise ParameterError("message", raw='value', xx='1', yy=1.0)	
