# -*- coding:utf-8 -*-
import os
from datetime import datetime
import cx_Oracle

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

cur = None
conn = None


def create_connect():
    global conn
    conn = cx_Oracle.connect('SXCRM/123456@127.0.0.1:1521/orcl')
    global cur
    cur = conn.cursor()
    try:
        cur.execute('select 0 from dual')
    except Exception as e:
        print(e)
        print("数据库链接失败")
    print("数据库初始化成功...")


def execute(sql):
    try:
        cur.execute(sql)
        conn.commit()
        print(str(datetime.now()) + "sql执行成功;")
    except Exception as e:
        print(e)
        print("写入失败")


def main():
    source_dir = 'D:/SXZQ/crm/split/crm6.sql'

    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open(file=source_dir, mode='r', encoding='utf-8') as f_source:
        sql = ''
        for line in f_source:
            line = line.strip().replace("\"", "\'")
            if line.startswith('-'):
                pass
            elif line.startswith(' '):
                pass
            elif line.endswith(';'):
                sql = sql + line
                print(str(datetime.now())+'---'+sql)
                execute(sql)
                sql = ''
            else:
                sql = sql + line+" "
    print("完成")


if __name__ == "__main__":
    create_connect()
    # sql = "DROP TABLE 'SXCRM'.'LMSP_REPORTWS_DEF';"
    # execute(sql)
    main()
    print("数据导入结束，关闭数据库连接...")
    cur.close()
    conn.close()
