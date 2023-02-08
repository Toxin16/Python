'''2023-02-08
csv파일 데이터 읽기'''

import csv

f=open("c:/data/weather.csv") #파일 열기
data=csv.reader(f) #파일 읽기
header=next(data) #열 머리글 행 제외

'''for row in data:
    print(row[3],end=',') #열 인덱스3에 해당하는 평균풍속만 출력'''

#울릉도의 지난 10년간 풍속 중 최대풍속 출력하기
max_wind=0.0 #최대풍속

for row in data:
    if row[2]=='': #풍속 데이터가 없는 경우
        wind=0
    else:
        wind=float(row[2]) #풍속 데이터를 실수형으로 변환

        if max_wind<wind: #max_wind와 풍속 데이터 비교
            max_wind=wind

print("지난 10년간 울릉도의 최대 풍속은:",max_wind, 'm/s')

f.close() #파일 닫기