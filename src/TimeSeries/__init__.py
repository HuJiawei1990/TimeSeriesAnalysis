#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file       __init__.py.py
@project    timeSeriesAnalysis
--------------------------------------
@author     hjw
@date       2018-01-03 14:11:15
@version    0.0.1.20180103
--------------------------------------
<enter description here>
"""

import sys
import logging
from .TimeSeries import TimeSeries

logging.basicConfig(filename='../logs/run.log',
                    format='%(asctime)s\t%(filename)s[%(lineno)d]\t%(levelname)s\t%(message)s',
                    #datefmt='[%Y-%m-%d %H:%M:%S]',
                    level=logging.INFO)
