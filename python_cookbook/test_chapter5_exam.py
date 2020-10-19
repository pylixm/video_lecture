# coding: gbk
# ��Python Cookbook�������²�����Ŀ�������½ڲ���Ҫ��
#    5.7��������Ԫ��ʱ�������е�˳��
#    5.8����ȡ��������С�ļ���Ԫ��
#    5.9����������ϵ�������Ѱ��Ԫ��
#    5.14�����ֵ�����������������
#    5.15�������յ�����ĸ����������ͷ���
from nose.tools import *
    
def func1( d ):
    dic_list=[(i,v) for v,i in d.items()]
    dic_list.sort()
    return dic_list
    

def func2( l ):
    dic_list=[(getattr(v,'age'),i,v) for i,v in enumerate(l)]
    dic_list.sort(reverse=True)
    return [(a[-1].name,a[-1].age) for a in dic_list]
    

def func3( l ):
    l_sort=[(s.lower(),s) for s in l]
    l_sort.sort()
    return [s[-1] for s in l_sort]
    
    #��  return sorted(l,key=lambda x:x.lower())
    
    
import re
#�����������������ִ��ַ����з��룬��������
def helpdef(s):
    re_str=re.compile(r'(\d+)')
    lst=re_str.split(s)
    lst[1:-1]=map(int,lst[1:-1])
    return lst
    
def func4( l ):
    lst_l=[(helpdef(s),s) for s in l]
    lst_l.sort()
    return [s for i,s in lst_l ]
    """
    re_str=re.compile(r'(\d+)')
    for substr in l:
        lst=re_str.split(substr)
        lst[1::2]=map(int,lst[1::2])
    str_l_dic=dict(zip(lst[1::2],l))   
    str_l_list=list(str_l_dic)
    str_l_list.sort()
    return str_l_list 
    """

# ----------------------------------------------------------
def test_func1():
    d = { 3:'a', 1:'b', 2:'c'}
    eq_( func1( d ), [ ('a',3), ('b',1), ('c',2) ] )
    d = { 'a':3, 'b':1, 'c':2 }
    eq_( func1( d ), [ (1,'b'), (2,'c'), (3,'a') ] )

def test_func2():
    class A( object ):
        def __init__( self, name, age ):
            self.name = name
            self.age = age
    l = [ A('����', 29), A('����', 31), A('����', 28) ]
    eq_( func2( l ), [ ('����', 31), ('����', 29), ('����', 28) ] )

def test_func3():
    l = [ 'c', 'A', 'b', 'D' ]
    eq_( func3( l ), ['A', 'b', 'c', 'D'] )

def test_func4():
    l = [ 'ch9.txt', 'ch10.txt', 'ch1.txt', 'ch3.txt', 'ch11.txt' ]
    eq_( func4( l ), [ 'ch1.txt', 'ch3.txt', 'ch9.txt', 'ch10.txt', 'ch11.txt' ] )