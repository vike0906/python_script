# -*- coding:utf-8 -*-
from datetime import datetime


def Main():
    source_dir = 'D:/SXZQ/crm/split/crm6.sql'
    target_dir = 'D:/SXZQ/crm/split/'

    # 计数器
    flag = 0

    # 文件名
    name = 1

    # 存放数据
    dataList = []

    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open(file=source_dir, mode='r', encoding='utf-8') as f_source:
        for line in f_source:
            flag += 1
            dataList.append(line)
            if flag >= 500 and (';' in line):
                with open(file=target_dir + "crm6" + str(name) + ".sql", mode='w+', encoding='utf-8') as f_target:
                    for data in dataList:
                        f_target.write(data)
                name += 1
                flag = 0
                dataList = []

    # 处理最后一批行数少于500行的
    with open(file=target_dir + "crm6" + str(name) + ".sql", mode='w+', encoding='utf-8') as f_target:
        for data in dataList:
            f_target.write(data)

    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    Main()
