'''
#练习疫情数据采集
#重点：列表，字典的数据操作应用
'''
import requests

import time

print('开始执行')
start = time.time()


"""

爬取课程的Json数据

:param index: 当前索引,从0开始

:return: Json数据

"""

url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"

payload = {

    #"modules": ["chinaDayList","chinaDayAddList","nowConfirmStatis","provinceCompare"],


}

headers = {



    "host": "api.inews.qq.com",

    "content-type": "application/x-www-form-urlencoded",

    "origin": "https://news.qq.com",

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"

}



response = requests.post(url, json=payload, headers=headers)

content_json = response.json()


# 获得请求数据

#print(content_json)
#print(content_json["data"])
d = content_json["data"]
#print(content_json["result"]["list"])
#d = content_json["result"]["list"]
print(type(d))
print(len(d))
kys = d.keys()
print(kys)
#print(d["chinaDayAddList"])
e = d["chinaDayAddList"]
print(type(e))
print(len(e))
print(e[0])
#e = d[0]
#print(type(d[0]))
#print(len(e))
#print(content_json["data"])
'''
e = content_json["data"]["data"]
print(e[0])
print(type(e[0]))
d = e[0]
kys = d.keys()
print(kys)
'''
#print(type(content_json["data"]))
#print(type(content_json))

#print(content_json["result"]["list"])

#print(content_json["list"])
#for k,v in e.items():
#    print(k,v)
'''
course_data = []

for item in content_json["data"]["data"]:
    course_value = (item['id'], item['courseName'], item['introduce'],

                    item['coverType'], item['cover'], item['studyNum'],

                    item['isFree'], item['showOrder'],

                    item['isShowName'], item['isShowIntroduce'],

                    item['learnType'], item['learnCardId'],

                    item['learnCardOrder'], item['isExpired'], item['courseType'],

                    item['waterNum'],item['newnum'],)

    course_data.append(course_value)
string_s = ('%s,' * 17)[:-1]
sql_course = f"insert into wm_courses values ({string_s})"
cur.executemany(sql_course, course_data)
db.commit()

db.close()

end = time.time()
print('执行结束')
print(f'程序执行时间是{end - start}秒。')
'''