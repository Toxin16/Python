#range() 함수-순차적인 숫자를 생성하는 함수

range(5) #0~4까지 순차적 숫자 생성
range(1,11) #1~10까지 1씩 증가하는 순차적 숫자 생성
range(1,11,2) #1~10까지 2씩 증가하는 순차적 숫자 생성
range(10, 0, -1) #10~1까지 1씩 감소하는 순차적 숫자 생성

for i in range(5): #i는 반복횟수, range(5)는 반복조건
    print(i,end=' ') #i출력. 파이썬에서 print는 무조건 줄바꿈후 출력. 옵션(,end)
print() #한 줄 띄우기

for i in range(1,11):
    print(i,end=' ')
print() #한 줄 띄우기

for i in range(1,11,2):
    print(i,end=' ')
print() #한 줄 띄우기

for i in range(10,0,-1):
    print(i,end=' ')
print() #한 줄 띄우기