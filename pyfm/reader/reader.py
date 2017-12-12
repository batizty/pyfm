#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

__author__ = 'tuoyu'
__desc__ = """This file is the basic reader for different input source"""

class Reader(object):
	"""
	Reader for different format filss
	"""
	def __init__(self, delimiter, schema, **kwargs):
		assert(delimiter == None, "Delimiter should not be empty")
		assert(schema == None, "Data schema should not be empty")
		self._delimiter_ = delimiter
		self._schema_ = schema
		self._kwargs_ = kwargs
		self._data_ = None

	def delimiter(self):
		return self._delimiter_
	
	def schema(self):
		return self._schema_

	def data(self):
		return self._data_

	def read(self, filename):
		# check files information valid
		self.check_file(filename)

		# read data
		self._data_ =  self.read_impl(filename)

		# check data format and valid
		self.check_data()
		return

	def check_file(self, filename):
		# TODO basic file check
		print "check filename {}".format(filename)
		return

	def check_data(self):
		assert(len(self._data_) > 0, "Data should not be empty")
		return

	def read_impl(self, filename):
		raise NotImplementedError()
	
	
