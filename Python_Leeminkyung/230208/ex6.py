'''2023-02-08
난수 생성하기'''

import numpy as np #numpy모듈의 별칭np

a=10
b=20

np.random.seed(100) #난수 발생을 위한 씨드
print('0~1보다 작은 범위의 난수:',np.random.rand(5))
print('0~1보다 작은 범위의 2차원 배열로 난수 생성:')
print(np.random.rand(5,3))
print("10~20사이의 실수 난수 생성")
print(a*np.random.rand(5)+a)

print('1~6사이의 정수 난수 생성:',np.random.randint(1,7,size=10))
print('1~`0사이의 2차원 배열 정수 난수 생성:',np.random.randint(1,11,size=(4,7)))