# coding: gbk
# ��Python Cookbook���ڶ��²�����Ŀ�������½ڲ���Ҫ��
#    2.7���������/��� 70 
#    2.8�����������ȡ�ļ� 71 
#    2.10�������ַ����е�zip�ļ� 74 
#    2.11�����ļ����鵵��һ��ѹ����tar�ļ� 76 
#    2.12�������������ݷ��͵�Windows�ı�׼��� 77 
#    2.13��ʹ��C++����iostream�﷨ 78 
#    2.14�����������ļ������ 80 
#    2.15�������ļ�����������ʵ�ļ����� 83 
#    2.22������Ŀ¼������·�� 91 
#    2.23����ƽ̨�ض�ȡ�޻�����ַ� 93 
#    2.24����Mac OS Xƽ̨��ͳ��PDF�ĵ���ҳ�� 94 
#    2.25����Windowsƽ̨���޸��ļ����� 95 
#    2.26����OpenOffice.org�ĵ�����ȡ�ı� 96 
#    2.27����΢��Word�ĵ��г�ȡ�ı� 97 
#    2.28��ʹ�ÿ�ƽ̨���ļ��� 98 
#    2.29�����汾�ŵ��ļ��� 100 
#    2.30������CRC-64ѭ��������У�� 102 
from nose.tools import *

def fun1( fn ):
    # ���ڴ�ռ�����ٵķ�ʽ��ͳ���ļ�������
    # �ԡ�#����ͷ��ע���У��Լ����ж���ͳ��
    f=open(fn,'r')
    co=0
    for i in f:
        if i[0] == '#' or i.isspace():
            continue
        else:
            co=co+1
    return co        
        

def fun2( fn ):
    # �����ٵĴ���������ͳ���ļ�������
    # �ԡ�#����ͷ��ע���У��Լ����ж���ͳ��
    f=open(fn)
    s_list=f.readlines()
    """
    for i in s_list:
        if i[0]=='#' or i.isspace():
            s_list.pop(s_list.index(i))
           
    return len(s_list)
    return len([line for line in open(fn).readlines() if len(line.strip())>0 and not line.startswith('#')])
    """
    s_list=[i for i in s_list if i[0]!='#' and len(i.strip())>0]
    return len(s_list) 
    
def fun3( zfn, fn ):
    # ��ȡѹ���ļ�zfn�е�fn�ļ����ݣ�������
    import zipfile
    z=zipfile.ZipFile(zfn,"r")
    if fn in z.namelist():
        s=z.read(fn)
    return s
        
    

import os
import fnmatch
def os_walk( path=os.sep.join(__file__.split( os.sep )[:-1]), patterns='*', through=True ):
    """ ʹ��os.walk()��������Ŀ¼������ָ�����ļ�
        @param path�������Ҹ�Ŀ¼��Ĭ��Ϊ������ǰĿ¼(������д����·��)
        @param patterns��������ģʽ��Ĭ��Ϊ�����ļ�������ָֻ��һ������ģʽ
        @param through�����Ƿ�͸��Ŀ¼��Ĭ��Ϊ��͸
    """

    lst=[]
    patterns = patterns.split(';')
    for pathname,subdirs,files in os.walk(path):
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name,pattern):
                    lst.append(name)
                    break
        if not through:
            break
    lst.sort()
    return lst

import glob
def glob_glob( path=os.sep.join(__file__.split( os.sep )[:-1]), patterns='*', through=True ):
    """ ʹ��glob.glob()��������Ŀ¼������ָ�����ļ�
        @param path�������Ҹ�Ŀ¼��Ĭ��Ϊ������ǰĿ¼(������д����·��)
        @param patterns��������ģʽ��Ĭ��Ϊ�����ļ�������ָֻ��һ������ģʽ
        @param through�����Ƿ�͸��Ŀ¼��Ĭ��Ϊ��͸
    """
 
    lst=[]
    for path1 in os.walk(path):
        for match in glob.glob(os.path.join(path1[0],patterns)):
            if os.path.isfile(match):
                lst.append(match.split('\\')[-1])
        if not through:
            break
    lst.sort()
    return lst

import sys,os
def fun4( pathname, add=False ):
    """ ����ָ��ģ���Ƿ������PythonĬ�ϵ�����·����
        @param pathname   Ҫ���ҵ�ģ��·��
        @param add        �����ڵ�����£��Ƿ�����뵽PythonĬ�ϵ�����·����
    """
    """
    flag=False
    re_str=False
    if not os.path.exists(pathname):
        print '��������ȷ��·��'

    else:
        #pathname = os.path.abspath(pathname)
        
        #x = os.path.abspath(x)
        if pathname in sys.path:
            re_str=True
        else:
            flag=True
            re_str=False
                
    
        if add and flag:
            sys.path.append(pathname)
            print '++++++++++=' 
            re_str=True   
    return re_str
    """
    if pathname in sys.path:
        return True
    else:
        if add:
            if os.path.exists(pathname):    
                sys.path.append(pathname)
                print '+++++++++++++++++'
                return True 
    
    return False
# ----------------------------------------------------------
def test_fun1():
    eq_( fun1( 'test1.txt' ), 10 )
    eq_( fun2( 'test1.txt' ), 10 )

def test_fun3():
    content = """I'm test2.txt's content."""
    eq_( fun3( 'data.zip', 'test2.txt' ), content )

def test_os_walk():
    eq_( os_walk( patterns='*.txt' ), ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt' ] )
    eq_( os_walk( patterns='*.txt', through=False ), ['test1.txt', 'test2.txt' ] )
    eq_( os_walk( path=r'D:/ch02_test/testdir' ), [ 'test3.txt', 'test4.txt', 'test5.txt' ] ) # path������ֵ���Լ�ʵ������޸�
    eq_( os_walk( path=r'D:/ch02_test/testdir', through=False ), [ 'test3.txt', 'test4.txt' ] )

def test_glob_glob():
    eq_( glob_glob( patterns='*.txt' ), ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt' ] )
    eq_( glob_glob( path=r'D:/ch02_test/testdir' ), [ 'test3.txt', 'test4.txt', 'test5.txt' ] )
    eq_( glob_glob( patterns='*.txt', through=False ), [ 'test1.txt', 'test2.txt' ] )
    eq_( glob_glob( path=r'D:/ch02_test/testdir', patterns='*.txt', through=False ), [ 'test3.txt', 'test4.txt' ] )

def test_fun4():
    eq_( fun4( r'D:\tmp' ), False )
    eq_( fun4( r'D:\tmpN' ), False )
    eq_( fun4( r'D:\tmp', add=True ), True ) # D:\tmpĿ¼����
    eq_( fun4( r'D:\tmpN', add=True ), False ) # D:\tmpNĿ¼������