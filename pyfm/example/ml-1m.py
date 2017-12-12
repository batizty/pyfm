#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

__author__ = 'tuoyu'
__desc__ = """This file is to gererate libfm format for later trainning"""


from ..reader.pandas_reader import PandasReader


def creat_libfm_data():
	'''
	Create libfm format data for later fm trainning
	'''

	# Common Constant Var
	delimiter = '::'
	
	# Load User Data
	user_schema = ['UserID', 'Genre', 'Age', 'Occupation', 'ZipCode']
	user_data = PandasReader(delimiter=delimiter, schema=user_schema)
	user_data.read('./pyfm/data/ml-1m/users.dat')

	# Load Moive Data
	movie_schma = ['MovieID', 'Name', 'Genre_list']
	movie_data = PandasReader(delimiter=delimiter, schema=movie_schma)
	movie_data.read('./pyfm/data/ml-1m/movie.dat')
	movie_data.drop(['Name'])

	# Rating Data
	rating_schma = ['UserID', 'MovieID', 'Ratings', 'Timestamp']
	rating_data = PandasReader(delimiter=delimiter, schema=rating_schma)
	rating_data.read('./pyfm/data/ml-1m/ratings.dat')
	ratings = rating_data.data()['Ratings']
	rating_data.drop(['Ratings', 'Timestamp'])




	


		