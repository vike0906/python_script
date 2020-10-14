
"""
解析已存在账号信息
"""
import json


def input_account():
    # 读取文件
    with open("D:\\work\\wiki\\userInfo.json", 'r', encoding='utf-8') as re:
        loads = json.load(re)
        for r in range(0, len(loads['content'])):
            print(loads['content'][r]['name'])


if __name__ == '__main__':

    # input_project()

    input_account()

    # response = get_user_info()
    #
    # print(response)

