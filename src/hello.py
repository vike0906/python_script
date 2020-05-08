import requests
from pyquery import PyQuery as pq


class HouseInfo:
    def __init__(self, image_url, desc, door_model, area, floor, built_year, community_name,
                 location, tag, total_price, unit_price):
        self.image_url = image_url
        self.desc = desc
        self.door_model = door_model
        self.area = area
        self.floor = floor
        self.built_year = built_year
        self.community_name = community_name
        self.location = location
        self.tag = tag
        self.total_price = total_price
        self.unit_price = unit_price

    def to_string(self):
        result = self.desc+'\t '+self.door_model+'\t '+self.area+'\t '+self.floor+'\t '+self.built_year+'\t '+self.community_name\
                 +'\t '+self.location+'\t '+self.tag+'\t '+self.total_price+'\t '+self.unit_price+'\t '+self.image_url
        return result


def parse(item):
    # 房屋图片链接
    image_url = item.find('.item-img img').attr('src')
    print(image_url)
    # 房屋描述
    desc = item.find('.house-details .house-title a').text()
    print(desc)
    # 房源细节信息
    details = item.find('.details-item').text()
    print(details)
    details = details.split()  # 空格分隔
    detail_info = details[0].split('|')  # |分隔
    # 户型
    door_model = detail_info[0]
    print(door_model)
    # 面积
    area = detail_info[1]
    print(area)
    # 楼层
    floor = detail_info[2]
    print(floor)
    # 建造年份
    built_year = detail_info[3][0:4]
    print(built_year)
    # 小区名
    community_name = details[1]
    print(community_name)
    # 地理位置
    location = details[2]
    print(location)
    # 标签
    tag = item.find('.tags-bottom').text()
    print(tag)
    # 总价
    total_price = item.find('.pro-price .price-det').text().replace('万', '')
    print(total_price)
    # 均价
    unit_price = item.find('.pro-price .unit-price').text().replace('元/m²', '')
    print(unit_price)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!!!!!!!!!!!!!!!!!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    house_info = HouseInfo(image_url, desc, door_model, area, floor, built_year, community_name,
                           location, tag, total_price, unit_price)
    return house_info


AJK = 'https://zhengzhou.anjuke.com/sale/erqic/p'
# AJK = 'https://shenzhen.anjuke.com/sale/futian/p'

# request_web(AJK)
flag = True
page_num = 1
while flag:
    int_2_str = str(page_num)
    AJK_URL = str(AJK+int_2_str)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.169 Safari/537.36'
    }
    print(AJK_URL)
    html = requests.get(AJK_URL, headers=headers).text
    doc = pq(html)
    house_items = doc('.list-item').items()
    for house_item in house_items:
        house_info_detail = parse(house_item)
        print(house_info_detail.to_string())
        file = open('house_info.txt', 'a', encoding='utf-8')
        file.write(house_info_detail.to_string() + '\n')
        file.close()
        if str(house_info_detail.location).startswith('二七'):
            pass
        else:
            print(house_info_detail.location)
            print(page_num)
            flag = False
            break
    page_num = page_num + 1


