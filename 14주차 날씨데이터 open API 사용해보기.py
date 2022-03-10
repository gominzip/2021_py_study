import urllib.request as URL

api="http://api.openweathermap.org/data/2.5/weather?"

city = "Seoul"
mode = "json"
appid = "26262cbdee846b1b4d9d79bf51995b53"

api = api+'q='+city
api = api+'&mode='+mode
api = api+'&appid='+appid

data = URL.urlopen(api) #url을 전송해 open api 호출

result = data.read() #결과 읽기

import json

j = json.loads(result)
weather = j['weather']
current = weather[0]['main']

main = j['main']
current_temp = main['temp'] - 273.15 #절대온도>섭씨온도

wind = j['wind']
speed = wind['speed']

print('%s의 현재 날씨 : %s' %(city, current))
print('현재온도 : %.1f' %current_temp)
print('현재풍속 : %.1f' %speed)
