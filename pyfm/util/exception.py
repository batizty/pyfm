#!/usr/bin/env python2.7
#   -*- coding:utf-8 -*-

class ParameterError(Exception):
	"""Paramter Error, raise for parameter errors

	Attributes:
		msg: error message
		values: extra information
	"""

	def __init__(self, msg, **kwargs):
		"""Construct for 'ParameterError'

		Create an ParameterError Exception with error message,
		if needs, you can add some extra information
		
		Args:
			msg: parameter error message
			kwargs: extra information, like parameter values
		"""
		self._msg_ = msg
		self._kwargs_ = kwargs

	def __str__(self):
		s = self._msg_
		if len(self._kwargs_) > 0:
			s += " | Extra Infomation:"
			for (k, v) in self._kwargs_.iteritems():
				s += " {} -> {},".format(k, v)
		return s