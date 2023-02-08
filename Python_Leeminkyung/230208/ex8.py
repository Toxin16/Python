'''2023-02-08
울릉도의 바람이 가장 강한 달 찾기'''

import csv

f=open("c:/data/weather.csv") #파일 열기
data=csv.reader(f) #파일 읽기
header=next(data) #열 머리글 행 제외

monthly_wind=[0 for x in range(12)] #매달 풍속 저장 0으로 초기화
days_counted=[0 for x in range(12)] #각 달마다 측정된 일수 0으로 초기화

for row in data:
    month=int(row[0][5:7]) #날짜 데이터에서 월에 해당하는 값 분리
    if row[3] !='': #풍속에 해당하는 데이터가 있다면
        wind=float(row[3]) #풍속 데이터 얻기
        monthly_wind[month-1]+=wind #해당 달에 풍속 데이터 추가
        days_counted[month-1]+=1 #해당 달의 일수가 1 증가

#print(monthly_wind)
#print(days_counted)

for i in range(12):
    monthly_wind[i] /= days_counted[i]

plt.plot(monthly_wind, 'blue') #매월 풍속 데이터로 선형 차트 그리기
plt.show() #차트 출력

#print(monthly_wind)
#print(days_counted)