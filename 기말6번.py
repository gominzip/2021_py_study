text = '{"items":[{"title": "“방역패스 과태료 150만원, 문 닫으란 소리” 자영업자들 부글부글","link": "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=101&oid=023&aid=0003659355","description": "전국카페사장연합회, 한국코인노래연습장협회 등으로 구성된 한국자영업자협의회는 지난 12일 입장문을 내고 “방역패스는 <b>코로나</b>로 극심한 고통을 받고 있는 자영업자들에게 방역의 비용을 전가하는 후안무치한 조치”... "},{"title": "‘학교 찾아가는 접종’, 찾는 학부모는 30%뿐","link": "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=102&oid=023&aid=0003659354","description": "일선 학교로 보건소 인력이 방문해 <b>코로나</b> 백신을 접종하는 ‘찾아가는 백신 접종’은 학부모 10명 가운데... 지난 7일에는 <b>코로나</b> 사태 이후 처음으로 하루 1000명을 넘는 1007명 학생 확진자가 나왔다. 유은혜 교육부... "},{"title": "울산 배달음식 안전성 검사 결과 모두 안전","link": "https://www.usmbc.co.kr/article/69Lssr82gczrukQ","description": "<b>코로나</b>19 확산으로 음식 포장과 배달이 늘어난 가운데, 울산지역에서 올 한 해 실시한 배달 조리음식과 배달용기에 대한 각종 검사 결과는 모두 안전한 것으로 나타났습니다. 울산보건환경연구원은 올 한 해 동안... "}]}'

def string_filter(input_string):
    filter_data = {'<b>':'', '</b>':'', '&nbsp;':' ', '&lt;':'<', '&gt;':'>', '&quot;':'"', '&amp;':'&'}
    result = input_string
    for key, value in filter_data.items():
        result = result.replace(key, value)
    return result

for news in text["items"]:
    title=news['title']

    title = string_filter(title)
    
    print('제목:', data['title'])
