'''2023-02-03
카이사르 암호 만들기'''

'''import string
st=string.ascii_uppercase #알파벳 대문자
a=st[3:]+st[:3]

def ciper(a): #암호화 코드를 만드는 함수
    idx = st.index(a)
    return a[idx]

src = input('문장을 입력하시오: ')
print('암호화된 문장: ', end='')

for ch in src:
    if ch in st:
        print(ciper(ch), end='')
    else:
        print(ch, end='')
print()'''

import string
src_str=string.ascii_uppercase #알파벳 대문자
dst_str=src_str[3:]+src_str[:3]

def ciper(a): #암호화 코드를 만드는 함수
    idx = src_str.index(a)
    return dst_str[idx]

src = input('문장을 입력하시오: ')
print('암호화된 문장: ', end='')

for ch in src:
    if ch in src_str:
        print(ciper(ch), end='')
    else:
        print(ch, end='')
print()