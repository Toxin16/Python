'''1~10까지 합계 출력'''

sum=0 #합계
for i in range(1,11):
    sum += i
print("1~10까지 합계 : ",sum) #한 줄 띄우기

sum=0 #합계
for i in range(0,11,2):
    sum += i
print("1~10까지 합계 : ",sum) #한 줄 띄우기

sum=0 #합계
for i in range(1,11):
    if i%2==0: #선택 조건
        sum += i
print("1~10까지 짝수의 합계 : ",sum) #한 줄 띄우기

#while반복문
sum=0 
i=1 #반복 횟수 초기화
while i<=10: #반복 조건
    if i%2==0: #선택 조건
        sum += i #짝수만 더하기
    i+=1
print("1~10까지 짝수의 합계 : ", sum)

#리스트 활용 반복문
list1=[2,4,6,8,10] #리스트 자료형
for num in list1: #반복조건
    print(num, end=' ')