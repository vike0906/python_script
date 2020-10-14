import requests

"""
导入用户账户
"""


def spider_info(data_map):

    server = 'http://localhost:8081/addUser'

    headers = {
        'AuthToken': '13d853406c02491089a0917c7b56f3e0',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    return requests.post(server, params=data_map, headers=headers).text


if __name__ == '__main__':

    dict_map = {'v_lgg':'李广广',
'v_tongjunxian':'仝钧衔',
'v_lb1':'梁班',
'v_lihaojie':'栗浩杰',
'v_yangxufeng':'杨旭峰',
'v_chenrui':'陈瑞',
'v_baijiang':'白江',
'v_zhaolina':'赵丽娜',
'v_sunzhiqiang':'孙志强'}

    for k, v in dict_map.items():
        params = dict(loginName=k, name=v)
        print(params)
        response = spider_info(params)
        print(response)

