import xlrd
import requests

"""
导入集团员工账号
"""


def spider_info(data_map):

    server = 'https://wiki.sxzq.com/wiki/sb/addUser'

    headers = {
        'AuthToken': '39ca41b2386e42959265c7a770b100d8',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    return requests.post(server, params=data_map, headers=headers).text


def get_user_info():

    server = 'https://wiki.sxzq.com/wiki/sb/getUser'

    headers = {
        'AuthToken': '39ca41b2386e42959265c7a770b100d8',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    return requests.post(server, headers=headers).text


def input_account():
    # 读取文件
    data_xsls = xlrd.open_workbook("D:\\work\\wiki\\员工信息.xlsx")
    sheet_name = data_xsls.sheets()[0]  # 进入第一张表
    print(sheet_name)
    count_nrows = sheet_name.nrows  # 获取总行数
    print(count_nrows)
    count_nocls = sheet_name.ncols  # 获得总列数
    for i in range(3000, count_nrows):
        login_name = ''
        if sheet_name.cell(i, 0).ctype == 2 and sheet_name.cell(i, 0).value % 1 == 0.0:
            login_name = str(int(sheet_name.cell(i, 0).value))
        else:
            login_name = str(sheet_name.cell(i, 0).value)

        user_name = str(sheet_name.cell(i, 1).value)

        phone = ''
        if sheet_name.cell(i, 5).ctype == 2 and sheet_name.cell(i, 5).value % 1 == 0.0:
            phone = str(int(sheet_name.cell(i, 5).value))
        print('loginName: '+login_name)
        print('userName: ' + user_name)
        print('phone: ' + phone)
        params = dict(loginName=login_name, userName=user_name, phone=phone)
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

