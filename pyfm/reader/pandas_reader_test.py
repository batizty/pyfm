#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

__author__ = 'tuoyu'
__desc__ = """This file is unit test script to do test case worker"""

import unittest
import logging
import pandas as pd

from .pandas_reader import PandasReader

logger = logging.getLogger(__file__)


class TestPandasReader(unittest.TestCase):
    """Unit Test class for Pands Reader."""

    def test_ml_reader(self):
        filename = './data/ml-1m/users.dat'
        schema = ['UserID', 'Genre', 'Age', 'Ocuupation', 'ZipCode']
        first_data = [1, 'F', 1, 10, '48067']
        drop_index = ['Age']

        logger.debug("test_ml_reader init")
        reader = PandasReader(
            delimiter="::",
            schema=schema)

        logger.debug("reading file {}".format(filename))
        reader.read(filename)
        self.assertTrue(reader.size() > 0, "Data Size should not be zero")

        first = reader.data().loc[0]
        self.assertTrue(first.size == len(schema),
                        'Data width should be '
                        'equal to len(schema) {}'.format(schema))

        self.assertTrue(first.shape == (5,),
                        'Single Data shape should be (5,0)')

        target_series = pd.Series(data=first_data, index=schema)
        self.assertTrue(first.equals(target_series),
                        'Target({}) should equals to First({})'.format(
                            first, target_series))

        reader.drop(columns=drop_index)
        droped_shape = (reader.size(), len(schema) - 1)
        data_shape = reader.data().shape
        self.assertTrue(data_shape == droped_shape,
                        'Droped data shape should equal {}, '
                        'But now shape is {}'.format(droped_shape, data_shape))


if __name__ == '__main__':
    unittest.main()
