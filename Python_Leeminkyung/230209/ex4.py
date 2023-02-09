'''2023-02-09
판다스로 울릉도의 바람 세기 분석'''

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/data/weather.csv",encoding='cp949') #파일 열기

month=[0 for x in range(12)] #매달 풍속 저장 0으로 초기화
day=[0 for x in range(12)] #각 달마다 측정된 일수 0으로 초기화
df['month']=pd.DatetimeIndex(df['일시']).month #일시 열의 데이터에서 월만 추출

for i in range(12):
    month[i]=df[df['month']==i+1] #월 별 구분
    day[i]=month[i].mean()['평균풍속'] #개별 평균 풍속

plt.plot( day, 'red') #매월 풍속 데이터로 선형 차트 그리기
plt.show() #차트 출력