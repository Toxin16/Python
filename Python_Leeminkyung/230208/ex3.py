'''2023-02-08
넘파이 활용'''

import numpy as np #numpy모듈의 별칭np

mid_score=np.array([10,20,30]) #중간고사 성적
final_score=np.array([70,80,80]) #기말고사 성적
total=mid_score+final_score #중간, 기말 성적 합계

print("성적의 합계:",total)
print("성적의 평균:",total/2)