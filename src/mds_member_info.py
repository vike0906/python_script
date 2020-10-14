import xlrd
import requests

"""
向消息系统导入集团员工信息账号
"""


def input_account():

    name_wx_id = {}

    # 读取微信ID
    data_xsls = xlrd.open_workbook("D:\\work\\message\\山证科技通讯录.xlsx")
    sheet_name = data_xsls.sheets()[0]  # 进入第一张表
    print(sheet_name)
    count_nrows = sheet_name.nrows  # 获取总行数
    print(count_nrows)
    for i in range(9, count_nrows):
        name = str(sheet_name.cell(i, 0).value)
        wx_id = str(sheet_name.cell(i, 1).value)
        name_wx_id[name] = wx_id
    print(name_wx_id)


    init_sql = 'INSERT INTO `m_member` (`id`, `name`, `mark`, `wx_id`, `party`, `tag`, `mobile`, `email`, `status`, `is_delete`, `update_time`, `create_time`) VALUES '
	# ('1', '柳胜利', 'liushengli', 'jia', '1|2|5', '5|3', '13538200906', '123456789@qq.com', 1, 1, '2020-08-13 00:49:57', '2020-06-05 23:34:57');
    # 读取详细信息
    data_xsls1 = xlrd.open_workbook("D:\\work\\message\\哨兵测试账号.xlsx")
    sheet_name1 = data_xsls1.sheets()[0]  # 进入第一张表
    print(sheet_name1)
    count_nrows1 = sheet_name1.nrows  # 获取总行数
    print(count_nrows1)
    count_nocls1 = sheet_name1.ncols  # 获得总列数

    for i in range(1, count_nrows1):
        name = str(sheet_name1.cell(i, 0).value)
        mark = str(sheet_name1.cell(i, 1).value)
        mobile = str(int(sheet_name1.cell(i, 3).value))
        email = str(sheet_name1.cell(i, 4).value)
        # print(name+' '+mark+' '+ name_wx_id[name]+' '+mobile+' '+email)
        init_sql = init_sql+" ('"+str(i)+"', '"+name+"', '"+mark+"', '"+name_wx_id[name]+"', null, null, '"+mobile+"', '"+email+"', 1, 1, '2020-09-30 00:00:00', '2020-09-30 00:00:00'),\r\n"

    print(init_sql)
    # 解析excel
    # 封装http请求


if __name__ == '__main__':

    # input_project()

    input_account()

    # response = get_user_info()
    #
    # print(response)

