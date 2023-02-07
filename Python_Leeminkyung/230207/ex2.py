'''2023-02-07
1회용 비밀번호 생성하기'''

import random

digit=int(input("몇 자리의 비밀번호를 원하십니까?")) #입력받은 숫자를 정수로 처리
opt='' #생성된 비밀번호를 저장하기 위한 변수 생성

for i in range(digit):
    otp=opt+str(random.randrange(0,10)) #0~9사이의 랜덤 수 생성 후 opt에 저장

print(opt)