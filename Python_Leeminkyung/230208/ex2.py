'''2023-02-08
특정 문자를 대체하는 sub()'''

import re

tweet=input("트윗을 입력하세요:")
tweet=re.sub('RT','',tweet) #RT문자를 공백으로 대체
tweet=re.sub('#\S+','',tweet) #(#)다음에 오는 문자를 공백으로 대체
tweet=re.sub('@\S+','',tweet) #(@)다음에 오는 문자를 공백으로 대체