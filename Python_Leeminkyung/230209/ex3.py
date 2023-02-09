'''2023-02-09
판다스로 데이터 분석하기'''

import numpy as np
import pandas as pd

df=pd.read_csv('c:/data/weather.csv',index_col=0, encoding='cp949')
print(df.describe)