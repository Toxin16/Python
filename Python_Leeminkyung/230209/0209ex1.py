'''2023-02-09
판다스로 시리즈, 데이터프레임 생성하기'''

import numpy as np
import pandas as pd #pd변수 사용

name_series=pd.Series(['김수안','김수정','박동윤','강이안','강지안'])
age_series=pd.Series([19,23,22,19,16])
sex_series=pd.Series(['여','여','남','여','남'])
grade_series=pd.Series([4.23, 4.35, 4.25, 4.37, 4.25])

print(name_series, age_series, sex_series, grade_series)

df=pd.DataFrame({'이름':name_series,'나이':age_series,'성별':sex_series,'평점':grade_series}) #열이름

