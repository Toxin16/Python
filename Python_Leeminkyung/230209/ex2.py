'''2023-02-09
판다스에서 csv파일 처리하기'''

import numpy as np
import pandas as pd #pd변수 사용

df=pd.read_csv('C:/data/countries.csv',index_col=0) #countries.csv파일의 0번 열을 인덱스로 지정
print(df)
'''
print(df[['capital','population']]) #특정 열에 해당하는 데이터만 추출

print() #한 줄 띄우기
print(df.head()) #[o:5]와 동일한 의미
print(df[:3]) #0~2까지 슬라이싱
print(df.loc['KR']) #행레이블이 KR에 해당하는 모든 열 정보
'''

df['density']=df['population']/df['area']
print(df)