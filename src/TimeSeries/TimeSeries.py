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
import numpy as np

logger = logging.getLogger('datageek')


class TimeSeries(object):
    def __init__(self, index=None, value=None):
        if len(index) != len(value):
            logger.error('Index & Values series have different lengths.')
            logger.info("Index series length = [%i]" % len(index))
            logger.info("Value series length = [%i]" % len(value))
            raise Exception("Failed to created TimeSeries object.")
        else:
            self.index = list(index)
            self.value = value
            self._data = pd.DataFrame(data=self.value, columns=['value'])
            self._data.index = self.index
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
            
            aux.data = self._data.sort_index(ascending=ascending, inplace=inplace)
            aux.index = aux._data.index
            aux.value = aux._data.values

        logger.info("Time Series sorting process ends successfully.")
        
        if not inplace:
            return aux
        
        self = aux

    
    def getDataframe(self):
        """
        :return: pandas dataframe style of time series
        """
        return self._data
    
    
    def getStep(self, mode='auto', max_samples=100, alpha = 0.2):
        logger.info('Time Series is going to reset its step value.')


        if not self.isSorted:
            logger.info('--> Time Series is not sore')
            self.sort(ascending=True)
        max_samples = min(self.length, max_samples)
        ## compute the steps between two timestamps
        steps = [(self.index[i+1] - self.index[i]) for i in range(max_samples-1)]
        n_steps = len(steps)
        default_steps = list(range(1, 11)) + [15, 20, 30] + list(range(60, 3601, 60))

        step_avg = sum(steps) / n_steps
        step_std = sum([i*i for i in steps]) / n_steps - (sum(steps) / n_steps) ** 2

        if mode == 'auto':

            if step_std < alpha * step_avg:
                abs_diff = [abs(step_avg - default_step) for default_step in default_steps]
                self.step = default_steps[np.argmin(abs_diff)]
                logger.info('--> Time Series step is reset to %i' % self.step)
            else:
                self.step = 0
                logger.warning('--> Time Series step is not suggested to change. Reset to 0.')










        
        
