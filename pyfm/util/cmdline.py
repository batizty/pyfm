#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from .exception import ParameterError

"""
This file is to finish an simple command line parser

TODO:
    1. add Long Desc and Short Desc
    2. add Valid Check
    3. add Bar and Foot
"""


class CMDLine(object):
    """CMDLine is to parse parameter.

    Attributes:
        _delimiter_:
        _values_:
        _help_:
    """

    def __init__(self):
        """Construct for 'CMDLine'."""
        self._delimiter_ = ","
        self._values_ = {}
        self._help_ = {}

    def parse_args(self, args):
        """Parse Arguments"""
        i = 0
        while i < len(args):
            arg = args[i]
            (result, parameter) = self.parse_name(arg)
            if result:
                if self.has_parameter(parameter):
                    raise ParameterError("Parameter {} is specified already"
                                         .format(parameter))
                value = ""
                if (i + 1) < len(args):
                    value = args[i + 1]
                    (result_next, _) = self.parse_name(value)
                    if result_next is False:
                        i = i + 1
                    else:
                        value = ""
                self.set_value(parameter, value)
                i = i + 1
            else:
                raise ParameterError("Parse Parameter {} Error"
                                     .format(parameter))

    @staticmethod
    def parse_name(ss):
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
        assert delimiter is None, "Delimiter should not be None"
        assert len(delimiter) == 1, "Delimiter should be an character"
        self._delimiter_ = delimiter

    def has_parameter(self, parameter):
        return parameter in self._values_

    def set_value(self, parameter, value):
        self._values_[parameter] = value

    def remove_parameter(self, parameter):
        if self.has_parameter(parameter):
            self._values_.pop(parameter)

    def check_parameters(self):
        """Check Parameters if there is any parameter is not registed.

        Raises:
            ParameterError: if met parameter not in help dict, then raise
        """
        for name, value in self._values_:
            if name not in self._help_:
                raise ParameterError("Could not find "
                                     "Parameter {} with "
                                     "Value {}".format(name, value))
        return

    def register_parameter(self, name, desc):
        """Register Parameter

        Args:
            name: parameter name
            desc: description for this parameter
        """
        if name in self._help_:
            raise ParameterError("Parameter {} Registered".format(name))
        self._help_[name] = desc
        return name

    def print_help(self):
        print self.__str__()

    def __str__(self):
        s = "\n"
        for (name, desc) in self._help_.iteritems():
            s += "\t"
            s += "{}\t\t{}\n".format(name, desc)
        return s

    def get_value(self, parameter, default_value=None):
        if self.has_parameter(parameter) is True:
            return self._values_[parameter]
        else:
            if default_value is not None:
                return default_value

        raise ParameterError("Not Found Parameter {} "
                             "Value and without default "
                             "value".format(parameter))

    def get_values(self, parameter, fn=None):
        if self.has_parameter(parameter):
            return [fn(ss.strip()) if fn is not None else ss.strip()
                    for ss in self.get_value(parameter).split(self.delimiter())]
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
