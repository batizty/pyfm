#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from .exception import ParameterError

class CMDLine(object):
	"""CMDLine is to parse parameter.
	
	Attributes:
		_delimiter_:
		_values_:
		_help_:
	"""	
	def __init__(self):
		"""Construct for 'CMDLine'."""
		self._delimiter_ = ";,"
		self._values_ = {}
		self._help_ = {}

	def parse_name(self, ss):
		"""Parse string is valid or not parameter

		Args:
			ss: input string

		Returns:
			Tuple(True, Valid_String) if this input string is valid
			Tuple(False, None) if input string is not valid
		"""
		if not ss or len(ss) <= 0:
			return False, None

		if len(ss) > 0 and ss[0] == '-':
			if len(ss) > 1 and ss[1] == '-':
				return True, ss[2:]
			else:
				return True, ss[1:]
		return False, None

	def delimiter(self):
		return self._delimiter_

	def set_delimiter(self, delimiter):
		assert(delimiter != None)
		self._delimiter_ = delimiter

	def has_parameter(self, parameter):
		return self._values_.has_key(parameter)

	def set_value(self, parameter, value):
		self._values_[ parameter ] = value

	def remove_parameter(self, parameter):
		if self.has_parameter(parameter):
			self._values_.pop(parameter)
	
	def check_parameters(self):
		"""Check Parameters if there is any parameter is not registed.

		Raises:
			ParameterError: if met parameter not in help dict, then raise
		"""
		for name, value in self._values_:
			if not self._help_.has_key(name):
				raise ParameterError("Could not find Parameter {} with Value {}".format(name, value))
		return
	
	def register_parameter(self, name, desc):
		"""Register Parameter

		Args:
			name: parameter name
			desc: description for this parameter
		"""
		if self._help_.has_key(name):
			raise ParameterError("Parameter {} Registed".format(name))
		self._help_[ name ] = desc
		return name

	def print_help(self):
		for name, desc in self._help_:
			s = "\t"
			s += "{0}\t\t{}\n".format(name, desc)

	def get_value(self, parameter, default_value=None):
		if self.has_parameter(parameter):
			return self._values_[parameter]
		else:
			if not default_value:
				return default_value

		raise ParameterError("Not Found Parameter {} Value \
			and without default value".format(parameter))

	def get_values(self, parameter, fn=None):
		if self.has_parameter(parameter):
			return [ fn(ss.strip()) if fn != None else ss.strip() 
				for ss in self.get_value(parameter).split(self.delimiter()) ]
		return [] 

	def get_str_values(self, parameter):
		return self.get_values(parameter)

	def get_int_values(self, parameter):
		def fn(x):
			return int(x)
		return self.get_values(parameter, fn)

	def get_float_values(self, parameter):
		def fn(x):
			return float(x)
		return self.get_values(parameter, fn)


