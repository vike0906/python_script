from datetime import datetime

import pymysql
import xlrd
from xlrd import xldate_as_tuple
import uuid

"""
导入项目信息及项目动态
"""


def insert_db(sql):     # 连接数据库并执行SQL
    conn = pymysql.connect(host='106.13.222.152', port=9001, user='sxzq', password='sxzq123456.', database='wiki', charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        print('sql: '+sql+' 执行成功')
    except Exception as e:
        conn.rollback()
        print(e)


def input_user_info():
    # 读取文件
    data_xsls = xlrd.open_workbook("D:\\work\\项目动态测试数据.xlsx")
    sheet_name = data_xsls.sheets()[0]  # 进入第一张表
    print(sheet_name)
    count_nrows = sheet_name.nrows  # 获取总行数
    print(count_nrows)
    count_nocls = sheet_name.ncols  # 获得总列数
    for i in range(1, count_nrows):
        insert_sql = "INSERT INTO `w_sys_user_info` (`id`, `sys_user_id`, `name`, " \
                     "`area`, `position`, `group_id`, `is_official`, `education`, " \
                     "`status`, `birth_date`, `create_time`, `update_time`) VALUES ("

        value_sql = '\''+''.join(str(uuid.uuid4()).split("-"))+'\', \''
        value_sql = value_sql+ sheet_name.cell(i, 0)
        for j in range(0, count_nocls):
            ctype = sheet_name.cell(i, j).ctype
            cell = sheet_name.cell(i, j)
            if ctype == 2 and cell.value % 1 == 0.0:
                cell = int(cell.value)
            elif ctype == 3:
                date = datetime(*xldate_as_tuple(cell.value, 0))
                cell = '\''+date.strftime('%Y-%m-%d')+' 00:00:00\''  # ('%Y/%m/%d %H:%M:%S')
            else:
                cell = '\''+str(cell.value)+'\''
            insert_sql = insert_sql + str(cell) + ','
        insert_sql = insert_sql[:-1]+')'

        insert_db(insert_sql)

    # 解析excel
    # 封装sql并提交


if __name__ == '__main__':

    input_user_info()


