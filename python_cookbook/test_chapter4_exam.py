# coding: gbk
# ��Python Cookbook�������²�����Ŀ�������½ڲ���Ҫ��
#    4.18���Ѽ����������� 169 
#    4.19����һ�������ɸ�ֵ�Ͳ��� 171 
#    4.20����Python��ʹ��printf 174 
#    4.22���ڱ��ʽ�д����쳣 176 
#    4.23��ȷ�������Ѿ��ڸ���ģ���б����� 178 
from nose.tools import *

import copy


def func_copy(obj):
    # �������Ӷ���
    new_obj = copy.deepcopy(obj)
    return new_obj


def list_comprehensions(seq):
    # ������ʹ��for��������seq��Ԫ�ؽ��д���
    i = 0
    while i < len(seq):
        if str(seq[i]).isdigit():
            seq[i] = seq[i] * 10
        i += 1
    return seq


def get_value_from_index(seq, index):
    if index >= -len(seq) and index < len(seq):
        return seq[index]
    else:
        return '�Ƿ����±�'


def cycle(seq):
    a = ''
    b = ''
    for index, item in enumerate(seq):
        b = '%s %s\n' % (item, index)
        print
        b
        a = a + b
    return a


def multidimensional(col, row, default):
    return [['a' for c in range(col)] for r in range(row)]


def expand(seq):
    # ������ʹ��for
    """
    i=0
    lst=[]
    while i<len(seq):
        if isinstance(seq[i],(tuple,list)):
            expand(seq[i])
        else:
            lst.append(seq[i]) 
        i+=1
    return lst
    """
    return sum(seq, [])


def sort(seq):
    """  
    lst=[[in_lst=r[c] for c in r] for r in seq]
    in_lst.sort()
    return lst
    """
    for row in seq:
        row.sort(reverse=True)
    seq.
    return seq


def transposing(seq):
    lst = [[r[c] for r in seq] for c in range(len(seq[0]))]
    return lst


def revert(d):
    return dict([(k, v) for v, k in d.iteritems()])


def create_dict(seq):
    """
    dic={}
    key_list=[i for i in seq if i%5==0]
    value_list=[i for i in seq if i%5!=5]
    for key,value in zip(key_list,value_list):
        dic=dic.setdefault(key,[]).append(value)
    return dic
    """
    pass


def subset(d, ks, default=None):
    """
    dic=dict.fromkeys(ks,default)
    s1=set(d)
    s2=set(dic)
    if s1&s2!=[]:
        return dict()
    else:
        return dic
    
    dic=dict.fromkeys([x for x in d if x in ks ],default)
    return dict
    
    s1=set(d)
    s2=set(dic)
    inter=s1%s2
    if len(inter)>0:
        return dict(inter,)
    """
    return dict([(k, d.get(k, default)) for k in ks])


def union_intersection(d1, d2, type):
    if type == 'unicon':
        union_dic = dict(d1, **d2)
        return dict.fromkeys([x for x in unicon], None)
    if type == 'intersection':
        return dict.fromkeys([x for x in d1 if x in d2], None)
    # ----------------------------------------------------------


def test_func_copy():
    class A:
        def __init__(self):
            self.name = 'A'
            self.age = 30
            self.sex = 'M'

    a = A()
    b = func_copy(a)
    eq_(b.name == 'A', True)
    eq_(b.age == 30, True)
    eq_(b.sex == 'M', True)
    eq_(id(a) != id(b), True)

    lst1 = [{1: ['a', 'b', 'c']}, {2: ['d', 'e', 'f']}, {3: ['g', 'h', 'i']}]
    lst2 = func_copy(lst1)
    eq_(lst1 == lst2, True)
    lst1[0][1][0] = 'abc'
    eq_(lst2[0][1][0] == 'a', True)


def test_list_comprehensions():
    lst1 = [1, 2, 'a', 3, 'b']
    eq_(list_comprehensions(lst1), [10, 20, 'a', 30, 'b'])


def test_get_value_from_index():
    eq_(get_value_from_index([1, 2, 3], 0), 1)
    eq_(get_value_from_index([1, 2, 3], 3), '�Ƿ����±�')
    eq_(get_value_from_index([1, 2, 3], -1), 3)
    eq_(get_value_from_index([1, 2, 3], -3), 1)


def test_cycle():
    s = """a 0
b 1
c 2
"""
    eq_(cycle(['a', 'b', 'c']), s)


def test_multidimensional():
    lst = multidimensional(3, 3, 'a')
    eq_(lst, [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']])
    lst[1][1] = 'b'
    eq_(lst, [['a', 'a', 'a'], ['a', 'b', 'a'], ['a', 'a', 'a']])


def test_expand():
    eq_(expand([['a', 'b', 'c'], ['d'], ['e', 'f']]), ['a', 'b', 'c', 'd', 'e', 'f'])


def test_sort():
    lst = [[1, 2], [3, 4], [5, 6]]
    eq_(sort(lst), [[2, 1], [4, 3], [6, 5]])


def test_transposing():
    lst = [['����', '��', 32], ['����', 'Ů', 23], ['����', '��', 28]]
    eq_(transposing(lst), [['����', '����', '����'], ['��', 'Ů', '��'], [32, 23, 28]])


def test_revert():
    d = {'a': 1, 'b': 2, 'c': 3}
    eq_(revert(d), {1: 'a', 2: 'b', 3: 'c'})


def test_create_dict():
    lst = range(20)
    eq_(create_dict(lst), {0: [1, 2, 3, 4], 10: [11, 12, 13, 14], 5: [6, 7, 8, 9], 15: [16, 17, 18, 19]})


def test_subset():
    d = {0: [1, 2, 3, 4], 5: [6, 7, 8, 9], 10: [11, 12, 13, 14], 15: [16, 17, 18, 19]}
    eq_(subset(d, [5, 10]), {10: [11, 12, 13, 14], 5: [6, 7, 8, 9]})
    eq_(subset(d, [1, 2]), {1: None, 2: None})


def test_union_intersection():
    d1 = {1: 'a', 2: 'b', 3: 'c'}
    d2 = {2: '2', 3: '3', 4: '4'}
    eq_(union_intersection(d1, d2, 'union'), {1: None, 2: None, 3: None, 4: None})
    eq_(union_intersection(d1, d2, 'intersection'), {2: None, 3: None})
