import pymysql


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


def read_test_data():   # 读取测试数据
    file_dir = 'C:/Users/vike0906/Documents/WeChat Files/liujialonglove/FileStorage/File/2020-04/wiki_menu.txt'
    source_data = []
    with open(file=file_dir, mode='r', encoding='utf-8') as source_file:
        for line in source_file:
            line = '\''+line.replace('\t', '\', \'', 1).replace('\t', '\', ', 1)
            line = line.replace('\t', ', \'', 1).replace('\t', '\', \'', 2)
            line = line.replace('\t', '\', ', 1).replace('\t', ', ', 1)
            line = line.replace('\t', ', \'', 1).replace('\t', '\', \'', 1)+'\''
            line = line.replace('\\N', '')
            # line = line.replace('\t', ', ', 7).replace('\\N', '\'\'')
            # line = line.replace('\t', ', \'', 1).replace('\t', '\', \'')+'\''
            source_data.append(line)
    return source_data


if __name__ == '__main__':
    data = read_test_data()
    while len(data) > 0:
        insert_sql = 'insert into w_menu values '
        if len(data) > 100:
            for i in range(100):
                insert_sql = insert_sql+'('+data.pop(0)+'), '
        else:
            for i in range(len(data)):
                insert_sql = insert_sql + '(' + data.pop(0) + '), '
        # print(insert_sql[:-2])
        insert_db(insert_sql[:-2])
