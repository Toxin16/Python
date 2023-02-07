'''2023-02-07
특정상표명 *로 대체하기'''

t='''[ARTICLE] 200820 BLACKPINK jennie is regarded to have
great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung 
galaxy Note 20( LG U+Mtstic Pink 30%, SKT Mystic Blue not disclosed)'''

#알파벳 소문자로 변경
t_low=t.lower()
t=' ' #공백 문자열 변수 생성
word=t_low.split('') #공백 기준으로 단어 분리

for word in t_low.split(''):
    if word=='kt'or word=='samsung'or word=='lg' or word=='skt':
        t2=t2+'*'
    else:
        t2=word +' '

print(t2)