import xlrd
import requests
from xlrd import xldate_as_tuple
from datetime import datetime

"""
导入集团员工账号
"""


def spider_info(data_map):

    server = 'https://wiki.sxzq.com/wiki/sb/addUser'

    headers = {
        'AuthToken': 'a1ff2a8f76184f8789d94ce0f5821d6b',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    return requests.post(server, params=data_map, headers=headers).text



def input_account():
    # 读取文件
    data_xsls = xlrd.open_workbook("D:\\work\\wiki\\成员信息.xlsx")
    sheet_name = data_xsls.sheets()[0]  # 进入第一张表
    print(sheet_name)
    count_nrows = sheet_name.nrows  # 获取总行数
    print(count_nrows)
    count_nocls = sheet_name.ncols  # 获得总列数
    for i in range(2, count_nrows):
        login_name = ''
        if sheet_name.cell(i, 0).ctype == 2 and sheet_name.cell(i, 0).value % 1 == 0.0:
            login_name = str(int(sheet_name.cell(i, 0).value))
        else:
            login_name = str(sheet_name.cell(i, 0).value)

        user_name = str(sheet_name.cell(i, 1).value)

        area = 0
        if sheet_name.cell(i, 2).ctype == 2 and sheet_name.cell(i, 2).value % 1 == 0.0:
            area = int(sheet_name.cell(i, 2).value)
        position = 0
        if sheet_name.cell(i, 3).ctype == 2 and sheet_name.cell(i, 3).value % 1 == 0.0:
            position = int(sheet_name.cell(i, 3).value)
        isOfficial = 0
        if sheet_name.cell(i, 4).ctype == 2 and sheet_name.cell(i, 4).value % 1 == 0.0:
            isOfficial = int(sheet_name.cell(i, 4).value)
        education = 0
        if sheet_name.cell(i, 5).ctype == 2 and sheet_name.cell(i, 5).value % 1 == 0.0:
            education = int(sheet_name.cell(i, 5).value)
        # print(sheet_name.cell(i, 6).ctype)
        date = datetime(*xldate_as_tuple(sheet_name.cell(i, 6).value, 0))
        birth_date = date.strftime('%Y-%m-%d')  # ('%Y/%m/%d %H:%M:%S')
        print('loginName: ' + login_name)
        print('userName: ' + user_name)
        print('area: ' + str(area))
        print('position: ' + str(position))
        print('isOfficial: ' + str(isOfficial))
        print('education: ' + str(education))
        print('birth_date: ' + birth_date)
        # area, position, isOfficial, education, birth_date
        params = dict(loginName=login_name, userName=user_name, area=area, position=position, isOfficial=isOfficial,
                      education=education, birth_date=birth_date)
        response = spider_info(params)
        print(response)

    # 解析excel
    # 封装http请求


if __name__ == '__main__':

    # input_project()

    input_account()

    # response = get_user_info()
    #
    # print(response)

