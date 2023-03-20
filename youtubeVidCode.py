''' 
install packages (command line):
! USE PIP OR PIP3 DEPENDING ON PYTHON VERSION INSTALLED (JUST USE EITHER ONE THAT WORKS LOL)

pip/pip3 install wrds
pip/pip3 install swig
pip/pip3 install git+https://github.com/AI4Finance-Foundation/FinRL.git
'''

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')
import datetime

%matplotlib inline
from finrl.config_tickers import DOW_30_TICKER
from finrl.meta.preprocessor.yahoodownloader import YahooDownloader
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.meta.env_stock_trading.env_stocktrading import StockTradingEnv
from finrl.agents.stablebaselines3.models import DRLAgent,DRLEnsembleAgent
from finrl.plot import backtest_stats, backtest_plot, get_daily_return, get_baseline

from pprint import pprint

import sys
sys.path.append("../FinRL-Library")

import itertools