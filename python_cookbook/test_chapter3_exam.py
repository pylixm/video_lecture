# coding: gbk
# ��Python Cookbook�������²�����Ŀ�������½ڲ���Ҫ��
#    3.5��������֮��Ĺ����� 116 
#    3.6�Զ���ѯ���� 118 
#    3.8�������ʱ�Ƿ�����ʵ�� 123 
#    3.9ʱ��ת�� 124 
#    3.13��ʮ���������ڻ��Ҵ��� 130 
#    3.14��Pythonʵ�ֵļ򵥼ӷ��� 133 
#    3.15������ÿ�У��� 136 
#    3.16�鿴���� 137 

from nose.tools import *

import datetime


def get_yc_ym(day):
    # ���ݴ�������ڣ���ȡ�������·ݵ��³�����ĩ
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
    # ���ݴ�������ڣ���ȡ�����ڼ��ȵļ�������ĩ
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
    # ���ݴ�������ڣ���ȡ��ǰ���ܼ�
    """
    week=day.weekday()
    if week == 0:
        return '��һ'
    if week == 1:
        return '�ܶ�'
    if week == 2:
        return '����'    
    if week == 3:
        return '����'
    if week == 4:
        return '����'
    if week == 5:
        return '����'
    if week == 6:
        return '����'
    """
    dict = {0: '��һ', 1: '�ܶ�', 2: '����', 3: '����', 4: '����', 5: '����', 6: '����'}
    weeknum = day.weekday()
    for i in dict.keys():
        if i == weeknum:
            return dict[i]


def days_between(begin, end):
    # ���ݴ������ֹ���ڼ�������������֮������
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
        return '��ȷ����ʼ�������ڽ�������'


def during(t, days=0, hours=0, minutes=0, seconds=0):
    """ ������ʼʱ��ͳ���ʱ�䣬�����ֹʱ��
        @param t        ��ʼʱ��
        @param days     ��������
        @param hours    ������Сʱ
        @param minutes  �����ķ���
        @param secodes  ��������
    
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
    # ���������dateת��Ϊdatetime.date���ͷ��ء���Ҫʹ��������dateutil
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
            return '�޷�ʶ������ڸ�ʽ'
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
                            return '�޷�ʶ������ڸ�ʽ'

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
    eq_(get_weekday(datetime.date(2011, 3, 21)), '��һ')
    eq_(get_weekday(datetime.date(2011, 3, 22)), '�ܶ�')
    eq_(get_weekday(datetime.date(2011, 3, 23)), '����')
    eq_(get_weekday(datetime.date(2011, 3, 24)), '����')
    eq_(get_weekday(datetime.date(2011, 3, 25)), '����')
    eq_(get_weekday(datetime.date(2011, 3, 26)), '����')
    eq_(get_weekday(datetime.date(2011, 3, 27)), '����')


def test_weeks_between():
    eq_(days_between(datetime.date(2011, 2, 1), datetime.date(2011, 3, 1)), 28)  # ���·�����
    eq_(days_between(datetime.date(2011, 1, 1), datetime.date(2011, 4, 1)), 90)  # һ��������
    eq_(days_between(datetime.date(2000, 1, 1), datetime.date(2000, 4, 1)), 91)  # һ��������
    eq_(days_between(datetime.date(2011, 2, 1), datetime.date(2011, 2, 1)), 0)  # ����
    eq_(days_between(datetime.date(2011, 4, 1), datetime.date(2011, 1, 1)), '��ȷ����ʼ�������ڽ�������')  # �쳣����


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
    eq_(format('20110327'), '�޷�ʶ������ڸ�ʽ')


def test_sched():
    """ ��ʱ����
    ÿʮ����ɨ��һ��ĳĿ¼�������ļ��������һ��txt�ļ���(��ʾ��DOS��tree����)���ļ���������ʽΪYYYYMMDDHHMISS�����浽�������·����
   
    schedule=sched.scheduler(time.time,time.sleep)
    schedule.enter(600,0,0,0)
    os.system('tree')
    schedule.run()
     """
    pass
