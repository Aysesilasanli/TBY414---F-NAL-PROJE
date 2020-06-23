import pandas as pd
import numpy as np
import matplotlib as plt

data = pd.read_csv(r'C:\Users\Buğra\Desktop\datasets_TCMB.csv',sep=";")
data=data.apply(lambda x:x.str.replace(",","."))
#
type(data.issizlik)
data.info()
data['enflasyon'] = data['enflasyon'].astype('float')
data['issizlik'] = data['issizlik'].astype('float')
data.describe()
print(data['issizlik'].mode())
print(data['issizlik'].median())
print(data['enflasyon'].mean())
print(data.mean(axis = 0, skipna = True))
print(data['enflasyon'].std())
print(data['issizlik'].std())
print(data.cov())
print(data.corr())
print('son 10 yılın ortalaması')