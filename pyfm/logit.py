#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

"""
This file is to compute sigmoid function
"""

def sigmoid(margin, round=False, limit=15):
	z = 0
	if round == True and limit > 0:
		z = max(min(margin, limit))
	else:
		z = margin
	return 1.0 / (1.0 + exp(-z))


