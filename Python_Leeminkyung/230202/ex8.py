'''원하는 n각형 도형 그리기'''

import turtle #터틀 모듈 추가
t=turtle.Turtle()
t.shape("turtle")

s=int(turtle.textinput("n각형 그리기","원하는 도형 입력"))
#s=turtle.textinput("n각형 그리기","원하는 도형 입력")
#n=int(s) #입력받은 도형 전수로 변환

for i in range(s):
    t.forward(50)
    t.left(360/s) 

input()