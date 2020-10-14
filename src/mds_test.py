# -*- coding: UTF-8 -*-
import json
import sys


def send_template_params(data):
    """返回脚本执行结果
    如果消息模板为多人统一消息，响应结果应为：
    {"$1": arg1, "$2": arg2, "$3": arg13...}
    如果消息模板为多人各自定义消息，响应结果应为：
    {
    "user1":{"$1": arg1, "$2": arg2, "$3": arg13...},
    "user2":{"$1": arg1, "$2": arg2, "$3": arg13...},
    "user3":{"$1": arg1, "$2": arg2, "$3": arg13...}
    }
    """
    sys.stdout.write('RESPONSE_RESULT_BEGIN')
    sys.stdout.write(json.dumps(data, ensure_ascii=False))
    sys.stdout.write('RESPONSE_RESULT_END')


def test():
    v1 = {'$1': '睡觉', '$2': '吃饭', '$3': '上班'}
    v2 = {'$1': '喝水', '$2': '坐地铁', '$3': '购物'}
    data = {'liushengli': v1, 'yangguohui': v2}
    send_template_params(data)


if __name__ == '__main__':
    test()
