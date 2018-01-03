#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file       TimeSeries.py
@project    timeSeriesAnalysis
--------------------------------------
@author     hjw
@date       2018-01-03 14:18:41
@version    0.0.1.20180103
--------------------------------------
<enter description here>
"""

import sys
import logging
import pandas as pd

logger = logging.getLogger('datageek')


class TimeSeries(object):
    def __init__(self, index=None, value=None):
        if len(index) != len(value):
            logger.error('Index & Values series have different lengths.')
            logger.info("Index series length = [%i]" % len(index))
            logger.info("Value series length = [%i]" % len(value))
            raise "Failed to created TimeSeries object."
        else:
            self.index = list(index)
            self.value = value
            self.data = pd.DataFrame(data=self.value, columns=['value'])
            self.data.index = self.index
            self.length = len(index)
            self.min_time = min(self.index)
            self.max_time = max(self.index)
            self.step = 0
            self.isSorted = False
            self.ascending = True
        
    def sort(self, ascending: bool=True, inplace=True):
        """
        # This function can sort the time series by time
        :param ascending:
        :param inplace:
        :return:
        """
        #TODO
        logger.info("*" * 50)
        logger.info("Sort time series process begins...")
        
        if self.isSorted & self.ascending == ascending:
            logger.info("--> Time series has already sorted. Passed")
        else:
            aux = self
            
            aux.data = self.data.sort_index(ascending=ascending, inplace=inplace)
            aux.index = aux.data.index
            aux.value = aux.data.values
            
        logger.info("Time Series sorting process ends successfully.")
        
        if not inplace:
            return aux
        
        self = aux
        
        
    
    
    def getDataframe(self):
        """
        :return: pandas dataframe style of time series
        """
        return self.data
    
    
    def getStep(self, mode='auto', maxSample=100):
        if self.step > 0:
            pass
        
        if not self.isSorted:
            self.sort(desc=False)
            
        maxSample = min(self.length, maxSample)
        
        
