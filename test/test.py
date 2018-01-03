#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file       test.py
@project    timeSeriesAnalysis
--------------------------------------
@author     hjw
@date       2018-01-03 12:38:26
@version    0.0.1.20180103
--------------------------------------
<enter description here>
"""

import sys
import pandas as pd
import numpy as np
import TimeSeries


def main():
    ## reading test data
    data_file = '../data/o_10631'
    data_df = pd.read_csv(data_file, header=None)
    # re-define columns' name
    data_df.columns = ['timestamp', 'value', 'host_id']
    
    #print(ts_df.sample(10))
    data_ts = TimeSeries.TimeSeries(data_df.timestamp, data_df.value)
    data_test = data_ts.getDataframe()
    
    print(data_test.head(10))
    #pass


if __name__ == '__main__':
    main()
