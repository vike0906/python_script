import datetime
import sz_es_house_main as sh
from apscheduler.schedulers.blocking import BlockingScheduler

"""
1.interval 间隔调度（每隔多久执行）
weeks (int) – number of weeks to wait
days (int) – number of days to wait
hours (int) – number of hours to wait
minutes (int) – number of minutes to wait
seconds (int) – number of seconds to wait
start_date (datetime|str) – starting point for the interval calculation
end_date (datetime|str) – latest possible date/time to trigger on
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
eg：
表示每隔3天17时19分07秒执行一次任务
scheduler.add_job(my_job, 'interval', days=03, hours=17, minutes=19, seconds=07)
间隔3秒钟执行一次
scheduler.add_job(job3, 'interval', seconds=3)

2.date 定时调度（作业只会执行一次）
run_date (datetime|str) – the date/time to run the job at  -（任务开始的时间）
timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already
eg:
在指定的时间，只执行一次
scheduler.add_job(tick, 'date', run_date='2016-02-14 15:01:05')　　
The job will be executed on November 6th, 2009
scheduler.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
The job will be executed on November 6th, 2009 at 16:30:05
scheduler.add_job(my_job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])

3.cron定时调度（某一定时时刻执行）
(int|str) 表示参数既可以是int类型，也可以是str类型
(datetime | str) 表示参数既可以是datetime类型，也可以是str类型
year (int|str) – 4-digit year -（表示四位数的年份，如2008年）
month (int|str) – month (1-12) -（表示取值范围为1-12月）
day (int|str) – day of the (1-31) -（表示取值范围为1-31日）
week (int|str) – ISO week (1-53) -（格里历2006年12月31日可以写成2006年-W52-7（扩展形式）或2006W527（紧凑形式））
day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun) - （表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示）
hour (int|str) – hour (0-23) - （表示取值范围为0-23时）
minute (int|str) – minute (0-59) - （表示取值范围为0-59分）
second (int|str) – second (0-59) - （表示取值范围为0-59秒）
start_date (datetime|str) – earliest possible date/time to trigger on (inclusive) - （表示开始时间）
end_date (datetime|str) – latest possible date/time to trigger on (inclusive) - （表示结束时间）
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone) -（表示时区取值）
eg:
表示2017年3月22日17时19分07秒执行该程序
scheduler.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)
表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
scheduler.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
scheduler.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')
表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
scheduler.add_job(my_job, 'cron',second = '*/5')
"""


def house_transaction_info():
    """
    深圳市二手房成交信息
    Source 深圳市房地产信息平台 http://zjj.sz.gov.cn:8004/
    """
    print('开始采集深圳市二手房成交信息:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    sql = sh.spider_info()
    sh.insert_db(sql)


if __name__ == '__main__':
    ap_scheduler = BlockingScheduler()
    ap_scheduler.add_job(house_transaction_info, 'cron', second=10)
    print('任务调度开始')
    ap_scheduler.start()
