# -*- coding:utf-8 -*-
from datetime import datetime


def main():
    business_dir = 'D:/work/wiki/sql/w_sys_user01.sql'
    target_dir = 'D:/work/wiki/sql/w_sys_user_update.sql'

    # 存放数据
    a = {}
    b = {}


    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open(file=business_dir, mode='r', encoding='utf-8') as f_source:
        for line in f_source:
            a_list = line.split(',')
            a[a_list[10][23:]] = 'update w_sys_user set (password, salt)=(select '+a_list[13]+', '+a_list[14]+' from dual) where id= '+a_list[10][23:]+';'
    for k, v in a.items():
        print(v)
    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



if __name__ == "__main__":
    main()
