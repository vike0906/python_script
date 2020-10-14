# 连接mysql并写入数据
# -*- coding: UTF-8 -*-
import json


def response_result(data):
    """返回脚本执行结果
    如果消息模板为多人统一消息，响应结果应为：
    {"$1": arg1, "$2": arg2, "$3": arg13...}
    如果消息模板为多人各自定义消息，响应结果应为：
    {"user1":{"$1": arg1, "$2": arg2, "$3": arg13...},
    "user2":{"$1": arg1, "$2": arg2, "$3": arg13...},
    "user3":{"$1": arg1, "$2": arg2, "$3": arg13...}}
    """
    print('RESULT_BEGIN')
    print(json.dumps(data, ensure_ascii=False))
    print('RESULT_END')
