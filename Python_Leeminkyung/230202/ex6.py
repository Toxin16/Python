'''터틀모듈'''

import turtle #터틀 모듈 추가
t=turtle.Turtle()
t.shape("turtle")

t.forward(100) #앞으로 100만큼 이동
t.left(90) #왼쪽으로 90도 회전
t.forward(100)

t.penup() #펜 들기
t.forward(100)
t.pendown()
t.circle(100) #반지름이 100인 원 그리기

input()