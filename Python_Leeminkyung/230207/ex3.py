'''2023-02-07
정규식 이용하기'''

import re #정규식 이용을 위한 모듈

f=open('c/data/udhr.txt') #파일오픈

for line in f:
    line=line.rstrip() #문장의 오른쪽 공백 제거
    if re.search('^[0-9]+',line): #line에서 정규식(숫자로 시작하는)검색
        print(line)