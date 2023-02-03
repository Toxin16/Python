'''2023-02-03
워드클라우드'''

import wikipedia
from wordcloud import Wordcloud

wiki=wikipedia.page('Aritifical intelligence') #위키백과에서 AI가 제목일 페이지 가져오기
text=wiki.content #wiki에서 텍스트만 분리

WordCloud=Wrodcloud(width=2000, height=1500).generate() #워드클라우드 생성 코드