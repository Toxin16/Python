'''터틀 도형 그리기'''

#한 변의 길이가 50인 직사각형 그리기(반복문 활용)

import turtle #터틀 모듈 추가
t=turtle.Turtle()
t.shape("turtle")

for i in range(4):
    t.forward(50)
    t.left(90) 

input()