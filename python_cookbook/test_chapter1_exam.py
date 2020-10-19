# coding:gbk
"""
 《Python Cookbook》第一章，以下章节不做要求：
    1.9　简化字符串的translate方法的使用
    1.10　过滤字符串中不属于指定集合的字符
    1.11　检查一个字符串是文本还是二进制
    1.15　扩展和压缩制表符
    1.17　替换字符串中的子串
    1.22　在标准输出中打印Unicode字符
    1.23　对Unicode数据编码并用于XML和HTML
    1.25　将HTML文档转化为文本显示到UNIX终端上
"""
from nose.tools import *

def translate( s ):
    """ 将英文字母转成对应的ASCII数字 """
    a=[]
    flag=0
    for i in s:
        if i.isalpha():
           a.append(str(ord(i)))
        else:
            flag=1
            break
    if flag:
        return "参数只能是英文字母"
    else:
        return ''.join(a)
        


def hierarchy( inst, cls ):
    """ 判断类层次体系的继承关系 """
    return isinstance(inst,cls)
    

def align( s, length ):
    """ 将传入的str按指定的长度居中显示 """
    return s.center(length,'x')

def format( s ):
    """ 将传入参数s前后的无用字符去除 """
    return s.strip(" 123456789")

def format2( s, sep ):
    """ s为源，将分隔符sep去除后，重新组合s返回 """
    lst=s.split(sep)
    a=[]
    b=''
    for i in lst:
        b=i.strip()
        a.append(b)
    return ''.join(a)



def gencharacter():
    """ 一行代码反序生成26个英文字母 """
    a=[chr(i) for i in range(97,123)]
    a.reverse()
    return ''.join(a)



def handle( s, sep ):
    """ 将传入参数s以指定的连接符sep连接起来  """
    li=list(s)
    li.reverse()
    return sep.join(li)
def contains( s, items ):
    """ s为源，若items中每一项都存在于s中，则返回True；items中只要有一项不存在于s中，就返回False """
    for i in items:
        if i not in s:
            return False
    return True
        

def case( s ):
    """ 按测试用例的要求，将s进行大小写的转换 """
    return s.title()
        
import re
def rep( s, d ):
    """ s为源，d为替换字典，将s中出现于d中的key替换为value """
    rx = re.compile('| '.join(map(re.escape,d)))
    def one_keys(match):
        return d[match.group(0)]
    return rx.sub(one_keys,s)          
            
            
            
            
            
            
            

def search( s ):
    """ s为源，跟据测试用例的提示，查找s中指定列，返回去除重复的结果。注意排序 """
    str1= s.split("\n")
    a=[]
    for i in range(1,len(str1)-1):
        str_list=str1[i].split("|")
        a.append(str_list[1])
    a=list(set(a))
    a.sort(reverse=True)
    return a
    
# ---------------------------------------------------------
def test_translate():
    eq_( translate('abc'), '979899' )
    eq_( translate('12abc'), '参数只能是英文字母' )

def test_hierarchy():
    class A( object ): pass
    class B( object ): pass
    class C( A ): pass
    eq_( hierarchy(A(),A), True )
    eq_( hierarchy(A(),B), False )
    eq_( hierarchy(C(),A), True )

def test_align():
    s1 = """
*
***
*****
***
*
"""
    s2 = """
  *  
 *** 
*****
 *** 
  *  """
    eq_( align(s1, 5), s2 )

def test_format():
    eq_( format('123only letters321'), 'only letters' )
    eq_( format('987 only letters654'), 'only letters' )
    eq_( format(' 432   only letters  123 '), 'only letters' )

def test_format2():
    eq_( format2('a b   c d     e', ' '), 'abcde' )
    eq_( format2('a,b  , c ,   d,e', ','), 'abcde' )

def test_gencharacter():
    eq_( gencharacter(), 'zyxwvutsrqponmlkjihgfedcba' )

def test_handle():
    eq_( handle( '12345', '+' ), '5+4+3+2+1' )
    eq_( handle( 'abcde', '_' ), 'e_d_c_b_a' )

def test_contains():
    eq_( contains( 'This is a Simple Example Statement', ('is', 'Statement', 'a') ), True )
    eq_( contains( 'This is a Simple Example Statement', ('is', 'Statement', 'a', 'an') ), False )

def test_case():
    s = '''cmp( x, y)
compare the two objects x and y and return an integer according to the outcome. the return value is negative if x < y, zero if x == y and strictly positive if x > y.'''
    s2 = """Cmp( X, Y)
Compare The Two Objects X And Y And Return An Integer According To The Outcome. The Return Value Is Negative If X < Y, Zero If X == Y And Strictly Positive If X > Y."""
    eq_( case( s ), s2 )

def test_rep():
    d = {
        'one': '一',
        'two': '二',
        'three': '三',
    }
    eq_( rep( 'one two three', d ), '一 二 三' )

def test_search():
    s = """
1|1048230100002752|05|2011-01-29T12:53:18|2011-01-29|1|签约激活|01
2|1048230100002753|03|2011-01-29 11:26:31||1|用户签约|01
3|1048230100002754|03|2011-01-29 11:28:48||1|加卡|01
4|1048230100002752|03|2011-01-28 17:05:24|2011-01-29|1|用户签约|01
31|1048230100002753|04|2011-02-22T10:20:01||1|已发送高速|01
32|1048230100002754|04|2011-02-22T10:20:01||1|已发送高速|01
27|1048230100002753|04|2011-02-20T20:58:17||1|已发送高速|01
28|1048230100002754|04|2011-02-20T20:58:17||1|已发送高速|01
29|1048230100002753|04|2011-02-21T17:30:01||1|已发送高速|01
30|1048230100002754|04|2011-02-21T17:30:01||1|已发送高速|01
33|1048230100002753|04|2011-02-23T10:50:01||1|已发送高速|01
34|1048230100002754|04|2011-02-23T10:50:01||1|已发送高速|01
"""
    result = [
                '1048230100002754',
                '1048230100002753',
                '1048230100002752',
             ]
    eq_( search( s ), result )