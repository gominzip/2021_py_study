import os
import sys
import urllib.request
client_id = "jaAFtQE8ZBGWJKZSztZe"
client_secret = "IXoFyrxjEN"

def string_filter(input_string):  #replace로 필요없는 부분 없애기
    filter_data = {'<b>':'', '</b>':'', '&nbsp;':' ', '&lt;':'<', '&gt;':'>', '&quot;':'"', '&amp;':'&'}
    result = input_string
    for key, value in filter_data.items(): #딕셔너리의 key/value쌍으로 구성된 튜플의 리스트
        result = result.replace(key, value)
    return result


keyword = input('뉴스 검색할 단어를 입력하세요 : ')
encText = urllib.parse.quote(keyword)

url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

import json
j = json.loads(response_body)

for data in j['items']:
    print('제목:', data['title']) #기사 제목만 프린트, 12장 24p 참고
    print('내용:', data['description'])
    print('-----------------------------------')

