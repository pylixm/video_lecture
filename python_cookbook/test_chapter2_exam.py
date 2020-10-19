# coding: gbk
# 《Python Cookbook》第二章测试题目，以下章节不做要求：
#    2.7　随机输入/输出 70 
#    2.8　更新随机存取文件 71 
#    2.10　处理字符串中的zip文件 74 
#    2.11　将文件树归档到一个压缩的tar文件 76 
#    2.12　将二进制数据发送到Windows的标准输出 77 
#    2.13　使用C++的类iostream语法 78 
#    2.14　回退输入文件到起点 80 
#    2.15　用类文件对象适配真实文件对象 83 
#    2.22　计算目录间的相对路径 91 
#    2.23　跨平台地读取无缓存的字符 93 
#    2.24　在Mac OS X平台上统计PDF文档的页数 94 
#    2.25　在Windows平台上修改文件属性 95 
#    2.26　从OpenOffice.org文档中提取文本 96 
#    2.27　从微软Word文档中抽取文本 97 
#    2.28　使用跨平台的文件锁 98 
#    2.29　带版本号的文件名 100 
#    2.30　计算CRC-64循环冗余码校验 102 
from nose.tools import *

def fun1( fn ):
    # 以内存占用最少的方式，统计文件的行数
    # 以“#”开头的注释行，以及空行都不统计
    f=open(fn,'r')
    co=0
    for i in f:
        if i[0] == '#' or i.isspace():
            continue
        else:
            co=co+1
    return co        
        

def fun2( fn ):
    # 以最少的代码行数，统计文件的行数
    # 以“#”开头的注释行，以及空行都不统计
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
    # 读取压缩文件zfn中的fn文件内容，并返回
    import zipfile
    z=zipfile.ZipFile(zfn,"r")
    if fn in z.namelist():
        s=z.read(fn)
    return s
        
    

import os
import fnmatch
def os_walk( path=os.sep.join(__file__.split( os.sep )[:-1]), patterns='*', through=True ):
    """ 使用os.walk()函数遍历目录、查找指定的文件
        @param path：“查找根目录”默认为本程序当前目录(不允许写绝对路径)
        @param patterns：“查找模式”默认为所有文件，可以只指定一种配置模式
        @param through：“是否穿透子目录”默认为穿透
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
    """ 使用glob.glob()函数遍历目录、查找指定的文件
        @param path：“查找根目录”默认为本程序当前目录(不允许写绝对路径)
        @param patterns：“查找模式”默认为所有文件，可以只指定一种配置模式
        @param through：“是否穿透子目录”默认为穿透
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
    """ 检验指定模块是否存在于Python默认的搜索路径中
        @param pathname   要查找的模块路径
        @param add        不存在的情况下，是否将其加入到Python默认的搜索路径中
    """
    """
    flag=False
    re_str=False
    if not os.path.exists(pathname):
        print '请输入正确的路径'

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
    eq_( os_walk( path=r'D:/ch02_test/testdir' ), [ 'test3.txt', 'test4.txt', 'test5.txt' ] ) # path参数的值视自己实际情况修改
    eq_( os_walk( path=r'D:/ch02_test/testdir', through=False ), [ 'test3.txt', 'test4.txt' ] )

def test_glob_glob():
    eq_( glob_glob( patterns='*.txt' ), ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt' ] )
    eq_( glob_glob( path=r'D:/ch02_test/testdir' ), [ 'test3.txt', 'test4.txt', 'test5.txt' ] )
    eq_( glob_glob( patterns='*.txt', through=False ), [ 'test1.txt', 'test2.txt' ] )
    eq_( glob_glob( path=r'D:/ch02_test/testdir', patterns='*.txt', through=False ), [ 'test3.txt', 'test4.txt' ] )

def test_fun4():
    eq_( fun4( r'D:\tmp' ), False )
    eq_( fun4( r'D:\tmpN' ), False )
    eq_( fun4( r'D:\tmp', add=True ), True ) # D:\tmp目录存在
    eq_( fun4( r'D:\tmpN', add=True ), False ) # D:\tmpN目录不存在