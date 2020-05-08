import requests

"""
导入用户账户
"""


def spider_info(data_map):

    server = 'http://localhost:8081/addUser'

    headers = {
        'AuthToken': '55cb28fa53db456eb245abfcf5c45847',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    return requests.post(server, params=data_map, headers=headers).text


if __name__ == '__main__':

    dict_map = {'03225': '程龙', '03917': '任林峰', '02622': '赵荣明', '03693': '党频', '04000': '李禹汉', '02867': '罗锋', '04537': '孙垚',
            '03652': '段高斐', '03655': '任伊莎', '04637': '沈彦', '00094': '李长亮', '04542': '李威', '03684': '刘重阳', '03651': '陈磊',
            '03865': '林永峰', '03694': '赵诣甚', '03226': '孟珂', '03377': '梁继敏', '04557': '杨晓澎', '03685': '陆权', '03656': '岳磊',
            '03816': '杨丹', '04027': '穆婉青', '03228': '李颖', '03974': '丁艳霞', 'v_liushengli': '柳胜利', 'v_liumeifang': '刘梅芳',
            'v_niuhuixia': '牛慧霞', 'v_yangguohui': '杨国辉', 'v_chenlongchao': '陈龙超', 'v_zhangzhenfan': '张震凡',
            'v_wangxin': '王昕',  'v_longbing': '龙兵', 'v_guozhehong': '郭哲虹', '03821': '程彪'}

    for k, v in dict_map.items():
        params = dict(loginName=k, name=v)
        print(params)
        response = spider_info(params)
        print(response)

