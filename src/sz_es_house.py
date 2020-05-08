class SzEsHouse:
    """
    深圳二手房成交信息汇总类
    """
    def __init__(self, ns, ft, lg, ba, lh, yt, sy, zz, qt, bg):
        self.ns = ns  # 南山
        self.ft = ft  # 福田
        self.lg = lg  # 龙岗
        self.ba = ba  # 宝安
        self.lh = lh  # 罗湖
        self.yt = yt  # 盐田

        self.sy = sy  # 商业
        self.zz = zz  # 住宅
        self.qt = qt  # 其他
        self.bg = bg  # 办公

    def insert_sql(self):
        return 'insert into sz_es_house (nsa,nsn,fta,ftn,lga,lgn,baa,ban,lha,lhn,yta,ytn,' \
               'sya,syn,zza,zzn,qta,qtn,bga,bgn) values ('+str(self.ns.acreage)+','+str(self.ns.number)+','\
               + str(self.ft.acreage)+','+str(self.ft.number)+','+str(self.lg.acreage)+','+str(self.lg.number)+','\
               + str(self.ba.acreage)+','+str(self.ba.number)+','+str(self.lh.acreage)+','+str(self.lh.number)+','\
               + str(self.yt.acreage)+','+str(self.yt.number)+','+str(self.sy.acreage)+','+str(self.sy.number)+','\
               + str(self.zz.acreage)+','+str(self.zz.number)+','+str(self.qt.acreage)+','+str(self.qt.number)+','\
               + str(self.bg.acreage)+','+str(self.bg.number)+')'


class Area:
    """
    区域成交面积与数量
    """
    def __init__(self, acreage, number):
        self.acreage = acreage  # 面积
        self.number = number    # 数量


class Form:
    """
    各类型成交面积与数量
    """
    def __init__(self, acreage, number):
        self.acreage = acreage  # 面积
        self.number = number    # 数量
