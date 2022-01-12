import pandas as pd
import numpy as np
import scipy as sci
import matplotlib as plt

data_csv=pd.read_csv('./Bdd/credit_immo/credit_immo.csv',sep=',')
print(data_csv)

data_json=pd.read_json('./Bdd/credit_immo/credit_immo.json')
print(data_json)

data_xls=pd.read_excel('./Bdd/credit_immo/credit_immo.xls')
print(data_xls)