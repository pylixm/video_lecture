# coding:gbk
"""
 ��Python Cookbook����һ�£������½ڲ���Ҫ��
    1.9�����ַ�����translate������ʹ��
    1.10�������ַ����в�����ָ�����ϵ��ַ�
    1.11�����һ���ַ������ı����Ƕ�����
    1.15����չ��ѹ���Ʊ��
    1.17���滻�ַ����е��Ӵ�
    1.22���ڱ�׼����д�ӡUnicode�ַ�
    1.23����Unicode���ݱ��벢����XML��HTML
    1.25����HTML�ĵ�ת��Ϊ�ı���ʾ��UNIX�ն���
"""
from nose.tools import *

def translate( s ):
    """ ��Ӣ����ĸת�ɶ�Ӧ��ASCII���� """
    a=[]
    flag=0
    for i in s:
        if i.isalpha():
           a.append(str(ord(i)))
        else:
            flag=1
            break
    if flag:
        return "����ֻ����Ӣ����ĸ"
    else:
        return ''.join(a)
        


def hierarchy( inst, cls ):
    """ �ж�������ϵ�ļ̳й�ϵ """
    return isinstance(inst,cls)
    

def align( s, length ):
    """ �������str��ָ���ĳ��Ⱦ�����ʾ """
    return s.center(length,'x')

def format( s ):
    """ ���������sǰ��������ַ�ȥ�� """
    return s.strip(" 123456789")

def format2( s, sep ):
    """ sΪԴ�����ָ���sepȥ�����������s���� """
    lst=s.split(sep)
    a=[]
    b=''
    for i in lst:
        b=i.strip()
        a.append(b)
    return ''.join(a)



def gencharacter():
    """ һ�д��뷴������26��Ӣ����ĸ """
    a=[chr(i) for i in range(97,123)]
    a.reverse()
    return ''.join(a)



def handle( s, sep ):
    """ ���������s��ָ�������ӷ�sep��������  """
    li=list(s)
    li.reverse()
    return sep.join(li)
def contains( s, items ):
    """ sΪԴ����items��ÿһ�������s�У��򷵻�True��items��ֻҪ��һ�������s�У��ͷ���False """
    for i in items:
        if i not in s:
            return False
    return True
        

def case( s ):
    """ ������������Ҫ�󣬽�s���д�Сд��ת�� """
    return s.title()
        
import re
def rep( s, d ):
    """ sΪԴ��dΪ�滻�ֵ䣬��s�г�����d�е�key�滻Ϊvalue """
    rx = re.compile('| '.join(map(re.escape,d)))
    def one_keys(match):
        return d[match.group(0)]
    return rx.sub(one_keys,s)          
            
            
            
            
            
            
            

def search( s ):
    """ sΪԴ�����ݲ�����������ʾ������s��ָ���У�����ȥ���ظ��Ľ����ע������ """
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
    eq_( translate('12abc'), '����ֻ����Ӣ����ĸ' )

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
        'one': 'һ',
        'two': '��',
        'three': '��',
    }
    eq_( rep( 'one two three', d ), 'һ �� ��' )

def test_search():
    s = """
1|1048230100002752|05|2011-01-29T12:53:18|2011-01-29|1|ǩԼ����|01
2|1048230100002753|03|2011-01-29 11:26:31||1|�û�ǩԼ|01
3|1048230100002754|03|2011-01-29 11:28:48||1|�ӿ�|01
4|1048230100002752|03|2011-01-28 17:05:24|2011-01-29|1|�û�ǩԼ|01
31|1048230100002753|04|2011-02-22T10:20:01||1|�ѷ��͸���|01
32|1048230100002754|04|2011-02-22T10:20:01||1|�ѷ��͸���|01
27|1048230100002753|04|2011-02-20T20:58:17||1|�ѷ��͸���|01
28|1048230100002754|04|2011-02-20T20:58:17||1|�ѷ��͸���|01
29|1048230100002753|04|2011-02-21T17:30:01||1|�ѷ��͸���|01
30|1048230100002754|04|2011-02-21T17:30:01||1|�ѷ��͸���|01
33|1048230100002753|04|2011-02-23T10:50:01||1|�ѷ��͸���|01
34|1048230100002754|04|2011-02-23T10:50:01||1|�ѷ��͸���|01
"""
    result = [
                '1048230100002754',
                '1048230100002753',
                '1048230100002752',
             ]
    eq_( search( s ), result )