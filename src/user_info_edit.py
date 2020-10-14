import xlrd
import requests

"""
转换员工信息
"""


def user_info_edit():
    # 读取文件
    file_dir = "D:\\work\\wiki\\data_2020-08-11 09_48_04 AM.csv"
    education_map = {1: '本科', 2: '硕士', 3: '博士', 4: '专科'}
    position_map = {1: 'CTO', 2: '副总经理', 3: '技术总监', 4: '产品设计', 5: '大数据', 6: '后台开发', 7: '客户端开发', 8: '前端开发',
                    9: '项目经理', 10: '测试', 11: '运维', 12: '副总裁', 13: '实习生'}
    with open(file=file_dir, mode='r', encoding='utf-8') as source_file:
        source_file.readline()
        for line in source_file:
            info = line.split(",")
            name = info[7]
            birthday = info[2]
            age = str(2020-int(birthday.split("-")[0]))
            position = position_map[int(info[8])]
            education = education_map[int(info[4])]
            use_info = {'姓名': name, '年龄': age, '职位': position, '学历': education}
            print(name+",\t"+age+",\t\t"+position+",\t\t"+education)


if __name__ == '__main__':

    user_info_edit()


