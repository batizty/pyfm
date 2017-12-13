#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

__author__ = 'tuoyu'
__desc__ = """This file is to gererate libfm format for later trainning"""

import logging
import sys
import numpy as np

from ..reader.pandas_reader import PandasReader

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__file__)

def creat_libfm_data():
	'''
	Create libfm format data for later fm trainning
	'''

	# Common Constant Var
	delimiter = '::'
	
	# Load User Data
	user_schema = ['UserID', 'Genre', 'Age', 'Occupation', 'ZipCode']
	user_data = PandasReader(delimiter=delimiter, schema=user_schema)
	user_data.read('./data/ml-1m/users.dat')
	logger.info("Loading user data OK")

	# Load Moive Data
	movie_schma = ['MovieID', 'Name', 'Genre_list']
	movie_data = PandasReader(delimiter=delimiter, schema=movie_schma)
	movie_data.read('./data/ml-1m/movies.dat')
	movie_data.drop(['Name'])
	logger.info("Loading movie data OK")

	# Rating Data
	rating_schma = ['UserID', 'MovieID', 'Ratings', 'Timestamp']
	rating_data = PandasReader(delimiter=delimiter, schema=rating_schma)
	rating_data.read('./data/ml-1m/ratings.dat')
	ratings = rating_data.data()['Ratings']
	rating_data.drop(['Ratings', 'Timestamp'])
	logger.info("Loading rating data OK")

	feat = [
		('UserID', rating_data.data()),
		('MovieID', rating_data.data())
		# ('Genre', user_data.data()),
		# ('Age', user_data.data()),
		# ('Occupation', user_data.data())
	]

	# Offset array
	offset_array = [0]
	dict_array = []
	for (feature_name, dataset) in feat:
		uniq = np.unique(dataset[feature_name])
		# according field different values to setting offset_array
		offset_array.append(len(uniq) + offset_array[-1])
		# setting revert search table for keys
		dict_array.append({ key : value + offset_array[-2] for value, key in enumerate(uniq) })
	logger.info("Mapping data done")

	output_filename = 'libfm.dat'
	with open(output_filename, 'w') as f:
		# read ratings data
		for i in range(rating_data.data().shape[0]):
			# just pick up ratings data as labels
			s = "{0}".format(ratings[i])
			sample = rating_data.data().loc[i]

			# add features data, using one-hot encoding
			for index_feat, (feature_name, dataset) in enumerate(feat):
				fvalue = sample.get(feature_name)
				if fvalue:
					key = dict_array[index_feat][fvalue]
					logger.debug("feature_name : {} raw : {} value : {}".format(feature_name, fvalue, key))
					s += " {0}:1".format( key )
			s += '\n'
			f.write(s)
		logger.info("Generate samples done")

if __name__ == '__main__':
	creat_libfm_data()




	


		