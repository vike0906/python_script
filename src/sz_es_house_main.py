import requests
from pyquery import PyQuery as pq
import pymysql
import json
from sz_es_house import Area, Form, SzEsHouse
"""
深圳市二手房成交信息
Source 深圳市房地产信息平台 http://zjj.sz.gov.cn:8004/
"""


def spider_info():
    data_area = 'http://zjj.sz.gov.cn:8004/api/marketInfoShow/getEsfCjxxGsData'
    data_type = 'http://zjj.sz.gov.cn/ris/szfdc/showcjgs/esfcjgs.aspx'
    headers_area = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'pgv_pvi=7131804672; pgv_si=s6733273088; ftzjjszgovcn=0; '
                  'Hm_lvt_ddaf92bcdd865fd907acdaba0285f9b1=1571104274; '
                  'Hm_lpvt_ddaf92bcdd865fd907acdaba0285f9b1=1571104274; '
                  'zlpt-session-id_test=0235fd3c-819a-4644-a387-93ca6b5d994c; '
                  'BIGipServerpool_192.168.2.76_9003_192.168.80.78_8080=1275242688.12067.0000; '
                  'insert_cookie=40523542; ASP.NET_SessionId=kgsnn5ud2melbjqe1ocqunny',
        'Host': 'zjj.sz.gov.cn:8004',
        'Origin': 'http://zjj.sz.gov.cn:8004',
        'Referer': 'http://zjj.sz.gov.cn:8004/marketInfoShow/Esfcjxxgs.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.120 Safari/537.36',
    }
    headers_type = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'pgv_pvi=7131804672; pgv_si=s6733273088; ftzjjszgovcn=0; '
                  'Hm_lvt_ddaf92bcdd865fd907acdaba0285f9b1=1571104274; '
                  'Hm_lpvt_ddaf92bcdd865fd907acdaba0285f9b1=1571104274;'
                  ' zlpt-session-id_test=0235fd3c-819a-4644-a387-93ca6b5d994c; '
                  'BIGipServerpool_192.168.2.76_9003_192.168.80.78_8080=1275242688.12067.0000; insert_cookie=40523542; '
                  'ASP.NET_SessionId=kgsnn5ud2melbjqe1ocqunny',
        'Host': 'zjj.sz.gov.cn',
        'Referer': 'http://zjj.sz.gov.cn:8004/marketInfoShow/Esfcjxxgs.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.120 Safari/537.36',
    }
    # 各区域成交面积与套数
    print(data_area)
    response = requests.post(data_area, headers=headers_area).text
    json_str = json.loads(response)
    data = json_str['data']
    data_mj = data['dataMj']
    data_ts = data['dataTs']

    area_list = list(range(6))
    for i in range(6):
        print(str(data_mj[i]) + str(data_ts[i]))
        area = Area(data_mj[i]['value'], data_ts[i]['value'])
        area_list[i] = area

    # 各类型成交面积与套数
    print(data_type)
    html = requests.post(data_type, headers=headers_type).text
    doc = pq(html)

    table_white = list(doc('.table-white').items())[0]
    form_list = list(range(4))

    tr = list(table_white.find('tr').items())

    for j in range(1, 5):
        print(tr[j].find('td').text())
        td = list(tr[j].find('td').items())
        form = Form(td[1].text(), td[2].text())
        form_list[j - 1] = form

    sz_es_house = SzEsHouse(area_list[0], area_list[1], area_list[2], area_list[3], area_list[4], area_list[5],
                            form_list[0], form_list[1], form_list[2], form_list[3])
    print(sz_es_house.insert_sql())
    return sz_es_house.insert_sql()


def insert_db(sql):
    conn = pymysql.connect(host='106.13.222.152', port=9001, user='vike0906', password='v123456.', database='vike', charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        print('信息采集成功')
    except Exception as e:
        conn.rollback()
        print(e)
