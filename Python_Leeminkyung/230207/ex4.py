'''2023-02-07
학사코드 추출하기'''

import re

text='''101 COM PythonProgramming
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''

#s=re.findall('\d+',text) #text에서 숫자만 반복되는 패턴 모두 찾기
s=re.findall('[A-Z][A-Z][A-Z]',text) #text에서 알파벳 대문자 3개로 연결되는 패턴
s=re.findall('[A-Z]{3}',text) #text에서 알파벳 대문자 3개로 연결되는 패턴
