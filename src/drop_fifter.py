# -*- coding:utf-8 -*-
from datetime import datetime


def Main():
    clear_dir = 'D:/SXZQ/crm/drop/clear.sql'
    business_dir = 'D:/SXZQ/crm/drop/business.csv'
    target_dir = 'D:/SXZQ/crm/drop/'

    # 存放数据
    clear_list = []
    business_list = []
    drop_list = []
    un_drop_list = []

    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open(file=clear_dir, mode='r', encoding='utf-8') as f_source:
        for line in f_source:
            clear_list.append(line)

    with open(file=business_dir, mode='r', encoding='utf-8') as f_source:
        for line in f_source:
            business_list.append(line.upper().replace('\n', ';\n'))
    print(business_list)
    print(clear_list)

    for sql in clear_list:
        if sql[11:] not in business_list:
            print(sql[11:].replace('\n', '') + "可删除")
            drop_list.append(sql)
        else:
            print(sql[11:].replace('\n', '') + "不可删除")
            un_drop_list.append(sql[11:])

    with open(file=target_dir + "drop.sql", mode='w+', encoding='utf-8') as f_target:
        for data in drop_list:
            f_target.write(data)

    with open(file=target_dir + "unDrop.sql", mode='w+', encoding='utf-8') as f_target:
        for data in un_drop_list:
            f_target.write(data)

    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    Main()
