#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

__author__ = 'tuoyu'
__desc__ = """This file is the ml data reader for different input source"""

import pandas as pd
import numpy as np

from .reader import Reader

class PandasReader(Reader):
	def __init__(self, delimiter, schema, **kwargs):
		super(PandasReader, self).__init__(delimiter=delimiter, schema=schema, kwargs=kwargs) 

	def read_impl(self, filename):
		"""Implementation for read_impl for csv reader"""
		return pd.read_csv(filename, 
			delimiter=self.delimiter(),
			engine='python',
			names=self.schema())

	def drop(self, columns, axis=1):
		self.check_data()
		self._data_ = self._data_.drop(labels=columns, axis=axis)
		self.check_data()

	def size(self):
		return len(self._data_)
		
		

