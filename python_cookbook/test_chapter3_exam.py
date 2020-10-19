# coding: gbk
# 《Python Cookbook》第三章测试题目，以下章节不做要求：
#    3.5计算日期之间的工作日 116 
#    3.6自动查询节日 118 
#    3.8检查夏令时是否正在实行 123 
#    3.9时区转换 124 
#    3.13将十进制数用于货币处理 130 
#    3.14用Python实现的简单加法器 133 
#    3.15检查信用卡校验和 136 
#    3.16查看汇率 137 

from nose.tools import *

import datetime


def get_yc_ym(day):
    # 根据传入的日期，获取其所在月份的月初、月末
    month = day.month
    year = day.year
    if month in (1, 3, 5, 7, 8, 10, 12):
        startday = datetime.date(day.year, day.month, 1)
        endday = datetime.date(day.year, day.month, 31)
    if month in (4, 6, 9, 11):
        startday = datetime.date(day.year, day.month, 1)
        endday = datetime.date(day.year, day.month, 30)
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            startday = datetime.date(day.year, day.month, 1)
            endday = datetime.date(day.year, day.month, 29)
        else:
            startday = datetime.date(day.year, day.month, 1)
            endday = datetime.date(day.year, day.month, 28)
    return (startday, endday)


def get_jc_jm(day):
    # 根据传入的日期，获取其所在季度的季初、季末
    month = day.month
    if month >= 1 and month <= 3:
        startday = datetime.date(day.year, 1, 1)
        endday = datetime.date(day.year, 3, 31)
    if month > 3 and month < 7:
        startday = datetime.date(day.year, 4, 1)
        endday = datetime.date(day.year, 6, 30)
    if month >= 7 and month <= 9:
        startday = datetime.date(day.year, 7, 1)
        endday = datetime.date(day.year, 9, 30)
    if month >= 10 and month <= 12:
        startday = datetime.date(day.year, 10, 1)
        endday = datetime.date(day.year, 12, 31)
    return (startday, endday)


def get_weekday(day):
    # 根据传入的日期，获取当前是周几
    """
    week=day.weekday()
    if week == 0:
        return '周一'
    if week == 1:
        return '周二'
    if week == 2:
        return '周三'    
    if week == 3:
        return '周四'
    if week == 4:
        return '周五'
    if week == 5:
        return '周六'
    if week == 6:
        return '周日'
    """
    dict = {0: '周一', 1: '周二', 2: '周三', 3: '周四', 4: '周五', 5: '周六', 6: '周日'}
    weeknum = day.weekday()
    for i in dict.keys():
        if i == weeknum:
            return dict[i]


def days_between(begin, end):
    # 根据传入的起止日期计算这两个日期之间相差几天
    """
    startday=begin.day
    endday=end.day
    days=startday-endday
    return days
    """
    oneday = datetime.timedelta(days=1)
    count = 0;
    if begin <= end:
        while begin != end:
            begin += oneday
            count += 1
        return count
    else:
        return '请确保开始日期早于结束日期'


def during(t, days=0, hours=0, minutes=0, seconds=0):
    """ 根据起始时间和持续时间，计算截止时间
        @param t        起始时间
        @param days     持续的天
        @param hours    持续的小时
        @param minutes  持续的分钟
        @param secodes  持续的秒
    
    starttime=time.time(t)
    run_time=time.time(datetime.datetime(0,days,hours,minutes,seconds))
    endtime=(starttime-run_time)
    nowtime=datetime.datetime.now()
    """
    endday = t + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return endday


import time


def format(date):
    """
    # 将输入参数date转换为datetime.date类型返回。不要使用三方库dateutil
    time_list=date.split('-')
    if time_list!=[]:
        if len(time_list[0])==4:
            year=int(time_list[0])
            month=int(time_list[1])
            day=int(time_list[2])
        elif len(time_list[2])==4:
            year=int(time_list[2])
            month=int(time_list[1])
            day=int(time_list[0])
        return datetime.date(year,month,day)
    else:
        time_list=date.split('/')     
        if time_list!=[]:
            if len(time_list[0])==4:
                year=int(time_list[0])
                month=int(time_list[1])
                day=int(time_list[2])
            elif len(time_list[2])==4:
                year=int(time_list[2])
                month=int(time_list[1])
                day=int(time_list[0])
            return datetime.date(year,month,day)
        else:
            return '无法识别的日期格式'
     """
    time_tuple = ()
    try:
        time_tuple = time.strptime(date, '%Y-%m-%d')
    except:
        try:
            time_tuple = time.strptime(date, '%m-%d-%Y')
        except:
            try:
                time_tuple = time.strptime(date, '%d-%m-%Y')
            except:
                try:
                    time_tuple = time.strptime(date, '%Y/%m/%d')
                except:
                    try:
                        time_tuple = time.strptime(date, '%m/%d/%Y')
                    except:
                        try:
                            time_tuple = time.strptime(date, '%d/%m/%Y')
                        except:
                            return '无法识别的日期格式'

    return datetime.date(time_tuple[0], time_tuple[1], time_tuple[2])


# ----------------------------------------------------------
def test_get_yc_ym():
    eq_(get_yc_ym(datetime.date(2011, 3, 28)), (datetime.date(2011, 3, 1), datetime.date(2011, 3, 31)))
    eq_(get_yc_ym(datetime.date(2011, 2, 1)), (datetime.date(2011, 2, 1), datetime.date(2011, 2, 28)))
    eq_(get_yc_ym(datetime.date(2012, 2, 1)), (datetime.date(2012, 2, 1), datetime.date(2012, 2, 29)))
    eq_(get_yc_ym(datetime.date(2011, 12, 31)), (datetime.date(2011, 12, 1), datetime.date(2011, 12, 31)))


def test_get_jc_jm():
    eq_(get_jc_jm(datetime.date(2011, 3, 28)), (datetime.date(2011, 1, 1), datetime.date(2011, 3, 31)))
    eq_(get_jc_jm(datetime.date(2011, 4, 1)), (datetime.date(2011, 4, 1), datetime.date(2011, 6, 30)))
    eq_(get_jc_jm(datetime.date(2011, 8, 30)), (datetime.date(2011, 7, 1), datetime.date(2011, 9, 30)))
    eq_(get_jc_jm(datetime.date(2011, 12, 1)), (datetime.date(2011, 10, 1), datetime.date(2011, 12, 31)))


def test_get_weekday():
    eq_(get_weekday(datetime.date(2011, 3, 21)), '周一')
    eq_(get_weekday(datetime.date(2011, 3, 22)), '周二')
    eq_(get_weekday(datetime.date(2011, 3, 23)), '周三')
    eq_(get_weekday(datetime.date(2011, 3, 24)), '周四')
    eq_(get_weekday(datetime.date(2011, 3, 25)), '周五')
    eq_(get_weekday(datetime.date(2011, 3, 26)), '周六')
    eq_(get_weekday(datetime.date(2011, 3, 27)), '周日')


def test_weeks_between():
    eq_(days_between(datetime.date(2011, 2, 1), datetime.date(2011, 3, 1)), 28)  # 二月份天数
    eq_(days_between(datetime.date(2011, 1, 1), datetime.date(2011, 4, 1)), 90)  # 一季度天数
    eq_(days_between(datetime.date(2000, 1, 1), datetime.date(2000, 4, 1)), 91)  # 一季度天数
    eq_(days_between(datetime.date(2011, 2, 1), datetime.date(2011, 2, 1)), 0)  # 当天
    eq_(days_between(datetime.date(2011, 4, 1), datetime.date(2011, 1, 1)), '请确保开始日期早于结束日期')  # 异常输入


def test_during():
    t = datetime.datetime(2011, 3, 28, 17, 30, 0)
    eq_(during(t), t)
    eq_(during(t, days=1), datetime.datetime(2011, 3, 29, 17, 30, 0))
    eq_(during(t, days=1, hours=7), datetime.datetime(2011, 3, 30, 0, 30, 0))
    eq_(during(t, days=1, hours=7, minutes=-31), datetime.datetime(2011, 3, 29, 23, 59, 0))
    eq_(during(t, days=1, hours=7, minutes=-31, seconds=60), datetime.datetime(2011, 3, 30, 0, 0, 0))


def test_format():
    eq_(format('2011-03-27'), datetime.date(2011, 3, 27))  # YYYY-MM-DD
    eq_(format('27-3-2011'), datetime.date(2011, 3, 27))  # DD-MM-YYYY
    eq_(format('3-27-2011'), datetime.date(2011, 3, 27))  # MM-DD-YYYY
    eq_(format('2011/3/27'), datetime.date(2011, 3, 27))  # YYYY/MM/DD
    eq_(format('3/27/2011'), datetime.date(2011, 3, 27))  # DD/MM/YYYY
    eq_(format('27/03/2011'), datetime.date(2011, 3, 27))  # MM/DD/YYYY
    eq_(format('20110327'), '无法识别的日期格式')


def test_sched():
    """ 定时任务
    每十分钟扫描一次某目录的所有文件，输出到一个txt文件中(提示：DOS的tree命令)，文件名命名格式为YYYYMMDDHHMISS，保存到本程序的路径下
   
    schedule=sched.scheduler(time.time,time.sleep)
    schedule.enter(600,0,0,0)
    os.system('tree')
    schedule.run()
     """
    pass
