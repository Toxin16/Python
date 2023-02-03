'''2023-02-03
텍스트 관련 메소드'''

'''
s='Monty python'
print(s[0]) #s에 저장된 문자열의 인덱스 0번 출력
print(s[6:10]) #s에 저장된 문자열의 인덱스 6~9까지 출력
s1=s[:-2] #s문자열의 처음부터 인덱스 1까지 슬라이싱(0부터 2의 앞 1까지)
s2=s[-2:] #s문자열의 인덱스 -2부터 끝까지 슬라이싱
print(s1+s2)
'''

#split()-문자열 자르기
ch='Welcome to python'
print(ch.split()) #ch문자열을 공백을 기준으로 나누기 한 후 리스트로 반환

ch2='Hello,World'
print(ch2.split(',')) #ch2문자열을 구분자(,)를 기준으로 나누기

#join()-문자열 연결하기
print('-'.join('010.1234.5678'.split('.'))) # .을 기준으로 분리 후 '-'으로 연결
print('010.1234.5678'.replace('.','-')) #'.'을 '-'으로 변경

#lower(), upper()-대소문자 변환
st='####Hello, World####'
print(st.strip('#')) #st에서 '#'제거
print(st.lower()) #st의 모든 문자를 소문자로 변환
print(st.upper()) #st의 모든 문자를 대문자로 변환
print(st.capitalize()) #st의 첫번째 문자만 대문자로 변환