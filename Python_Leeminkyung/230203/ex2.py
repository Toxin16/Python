'''2023-02-03
string 모듈'''

import string
st1=string.ascii_lowercase #알파벳 소문자
st2=string.ascii_uppercase #알파벳 대문자

print("알파벳 소문자:",st1)
print("알파벳 대문자:",st2)

#알파벳 한 자리씩 이동하기
print(st2[1:]+st2[:1]) #st2에서 알파벳 한 자리씩 이동