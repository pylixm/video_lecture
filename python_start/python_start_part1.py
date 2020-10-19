1Python最大的语法特点是什么？
答:简单，程序书写规范

●Python是编译型语言还是解释型语言？
答:解释型

●Python支持面向过程开发吗？支持面向对象开发吗？
答：python是面向对象开发的，不支持面向过程
    # 点评：除了面向对象，还面向过程。

●Python是强类型语言还是弱类型语言？
答：强类型语言

●在Windows环境下，在按装了Python之后，如果想支持以“python a.py”的方式运行Python脚本，需要设置什么？
答：在环境变量 Path中加入Python安装目录

●10除以3商为3，余数为1，如何一个表达式得到商和余数？
答：divmod（10，3）
●10/3的结果是什么？
答：3
●如何求正整数N的平方根？
答：N**2
    # 点评：这是求平方，平方根用math函数的方法
●以下表达式的结果是什么？
True and False or True
答：False
    # 点评：为何返回False呢？通过Pyshell自己试一下。

●将以下语句用一个表达式实现(使用两种方式)：
if exp1:
    return False
else:
    if exp2:
        return 1
    else:
        return 0
答：
if exp1:
    return False
elif exp2:
    return 1
else:
    return 0
    # 点评：一下方法仅供参考
        # False if exp1 else 1 if exp2 else 0


●假设lst是一个list结构，以下操作是否正确，说明原因。
lst = []
lst.append( 'a' ).append( 'b' )
答：
错误 append为list的方法，而lst.append并不是list

●假设lst为：
lst = range(10)
要获取子序列[2, 3, 4, 5, 6]，应如何操作？
答：range（2，7，1）
    # 点评：括号是中文状态下的，这个得注意，以后在项目中这种错误不好查找，所以要细心；

●假设lst为：
lst = [ 1, 2, 3 ]
至少写出三种方法将lst反序输出，方法越多越好。
答：lst.sort()
    # 点评：知识不够扎实
        # 1.sort()行数的倒叙，是通过一个参数控制的；
        # 2.还有list的一些其知识，没有理解到，例如pop，或者通过下标的方式。

●两个list可以相加吗？可以相减吗？
答：可以 不可以相减

●list.pop()可以弹出list中最后一个item，也可以这样调用：
lst.pop( param )
其中param是index还是value？
答：index
    # 点评：lst不是list会报错

●以下语句的结果是什么？为什么会是这样的结果？
>>> a = range(10)
>>> for i in a:
...     a.remove(i)
...
>>> print a
答：[]
第二行代码为i遍历a中每一个元素的index，remove（）方法把index为i的a的项删除。所以最后为空list
    # 点评，结果不正确，应该为：[1, 3, 5, 7, 9]
    # 原因：在循环时a的值在变化。这种方式不提倡用。

●如何通过下标方式复制一个list？复制出来的list，与原list是同一个对象，还是一个新对象？
答：
a=[1,2,3,4,5]
b=[]
for i in a:
    b[i]=a[i]
复制出来的list与原list是同一个对象
    # 点评：不正确
        # 1.首先不是一个对象；
        # 2.b[i]这样使用是有问题的，会报”index out of range“错误。

●假设lst为：
>>> lst = [ 1, 'a', 2, 'b', 3, 'c' ]
要求一行代码得到如下结果：
['d', 97, 'e', 98, 'f', 99]
提示：
>>> ord('a')
97
>>> chr(97)
'a'
>>>
答：chr(97+k) for k in lst if k.isdigit() ; return ord(k)
 # 点评：要观察它们之间的关系、规则
        # 参考答案：[ ord(i) if type(i)==str else chr(i+99) for i in lst ]

●假设lst为：
lst = range(10)
要获取子序列[1, 2, 3, 4, 5]，应如何操作？
答：range(1,6,1)
    # 点评：也可以通过下表截取的方式，可以通过pyshell试试。
    a[1:6]
●假设有以下操作：
l = [1,2]
l.extend( [ [3,4], [5,6] ] )
写出l的最终结果。
答：[1,2,[3,4],[5,6]]

●假设lst为：
lst = [ 1, 1, 2, 2, 3, 3 ]
写出lst.index( 2, 3 )的结果。
答：3

●假设有以下操作：
lst = [ 1, 1, 2, 2, 3, 3 ]
print lst.pop(3)
print lst
写出以上两步的结果。
答：
2
[1,1,2,3,3]

●假设有以下操作：
lst = [1, 1, 2, 2, 3, 3]
lst.remove( 2 )
写出lst的结果。
答：[1,1,2,3,3]
●假设lst为：
lst = [ ('张三', 20), ('李四', 19), ('王五', 21) ]
使用list.sort()按每人的年龄排序。
答：list.sort(lst.items[1])
    #　点评：不正确，没有ｉｔｅｍｓ属性
        #　参考答案：lst.sort( key = lambda x:x[1] , reverse=True )



●一行代码获取N(含N)之前的所有偶数，N为自然数。方法越多越好。
答：range(2,N,2)
    # 点评：此方法不错，是否可以写出更多的来
        #　参考答案：[i for i in range(N+1) if i%2 != 1]，看是否可以写出其他的方法来。
●以下代码：
>>> 'abc' \
...     'def'
???
>>> 'abc' + 'def'
???
>>>
结果一样吗？含义一样吗？为什么？
答：结果一样 含义不一样
 第一种、表示一个字符串。第二种表示两个字符串链接


●使用最简短的代码打印乘法表，要求输出格式为：
1*1=1
1*2=2	2*2=4
1*3=3	2*3=6	3*3=9
1*4=4	2*4=8	3*4=12	4*4=16
1*5=5	2*5=10	3*5=15	4*5=20	5*5=25
1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36
1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49
1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64
1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81
答：
i,j=0,0
for i<10:
    for j<=i:
      print j,"*",i,"=",i*j,"\t"
    print "\n"
    # 点评：
        # 1.为啥for后面跟的是个结果为boolen型的数据呢？
        # 2.参考答案："\n".join([" ".join(["%s*%s=%s"%(x,y,x*y)for y in range(1,x+1)])for x in range(1,10)])
●补全以下代码，使输出符合既定要求：
>>> print '金额为:???' % 1.2345
金额为:1.23
>>>
答：
print '金额为：%3.2f'% 1.12345
    # 点评：
        # 正确答案：print '金额为：%3.2f'% 1.12345

●补全以下代码，要求识别用户的任一一种退出指令：
>>> i = raw_input( '输入Quit/quit/Q/q退出:' )
输入Quit/quit/Q/q退出:q
>>> if ???:
...     sys.exit(0)
...
>>>
答：if i==quit or Quit or q
    # 点评：这个题目应该不难
    """
    方法一：
        if i in ['Quit','quit','Q','q']:
            sys.exit(0)
    方法二：使用正则 
        import re
        if re.findall('Quit|quit|q|Q',i):
            sys.exit(0)
    方法三：   
        if i=='q' or i=='Quit' or i=='quit' or i=='Q':
            sys.exit(0)
    """
●写出以下操作的结果：
>>> s = 'abcdefg'
>>> print s[1:].find( 'cde' )
>>> print s[1:4].find( 'cde' )
答：
1
1
    # 点评：
    # 正确答案：
        1
        -1

●写出以下操作的结果：
>>> s = 'abcabcabc'
>>> print s.rfind( 'abc' )
答：6

●补全以下代码：
>>> for i in range(1, 11, 2):
...     print ???
...
    *
   ***
  *****
 *******
*********
>>>
答：print center("*"*(i-1),9)
    # 点评：center的使用方法，这个再思考一下。

●假设s为：
s = '***a b c**'
一行代码返回'abc'。
答：k for i in s if s.isalpha()
    # 点评：这个逻辑正确吗？不大明白呢！！








●以下操作是否正确？如果正确，写出结果；如果不正确，说明原因：
(1,3) + ('a', 'b')
答：正确 （1,3,'a','b'）

●假设有以下代码：
>>> a = ( 0, 1, 2, 3, 4 )
>>> for i in range( 5, 10 ):
...     a.append( i )
以上操作是否正确，为什么？
答：不正确 i 为 index 不可以作为a的元素
    # 点评：不正确，因为a是元组，是常量，不可更改，只可以使用。

●Python内置的高级数据结构中，“序列”有哪些？“散列”有哪些？这些数据类型哪些是可变的，哪些是不可变的？
答：序列：string、tuple、list     散列：dictionary
  string 不可变 tuple、list、dictionary可变
  # 点评：
        # 正确答案：1、序列：tuple，str，list   2、散列：dict，set
        # 哪些可变哪些不可变，自己通过pyshell试试。

●哪些数据类型可以作为dict的key？哪些数据类型可以作为dict的value？
答：integer、string 可以作为key  value ：任何类型都行
    # 点评：
        # 字典的键必须是不可改变的类型，如：str，int，float，tuple
        # 任何可更改的数据类型可以作为value

●假设有以下dict变量：
>>> d = {'name':2, 'sex':1, 'age':3 }
如何按value排序输出？用尽可能短的代码、尽可能多的方法实现。

    #点评：变成list输出即可：
    """
        lst = d.items()
        lst.sort(key = lambda x:x[1],reverse=False)
        或者：
        sorted(d.items(),key = lambda x:x[1],reverse=False)
        或者：
        lst = d.items()
        lst.reverse()
    """




●如何一行代码将{'a':1,'b':2}反置为{1:'a',2:'b'}？
    # 点评：
        # 参考答案：dict((v,k) for k, v in d.iteritems())




●取用dict中不存在的key时会抛出KeyError Exception：
>>> d = {}
>>> print d['a']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'a'
>>>
如何避免发生这种错误？
答：d.get(key,default)
    # 点评，不错
        # 还有其他的方法
        """
            方法一：不用的d['a']这种方式，使用d.get('a')没有查找到值，不会抛出异常。
            方法二：
                if a in d:
                    print d['a']
            方法三：
                try 
                    print d['a']
                except KeyError:      
                    pass
        """
●如果有双层循环，内层的break能否跳出两层循环？
不能
    # 点评：写出原因。


●以下语句段：
>>> for i in range(3):
...     if i < 2: print i
...     else: break
... else:
...     print 'abc'
'abc'会否被输出？说明原因。
答：不会 循环没有全部循环
    """ 正确答案：
        不会。因为本for循环正常应执行三次，当for循环每一次都执行了，没有被break，会执行后面的else语句，
        而本for循环当执行到第三次是执行了break语句，不满足执行else的条件，所以不会输出'abc'
    """

●以下程序逻辑中：
if exp1:
    do()
elif exp2:
    do()
else:
    do()
其中elif分支是必须的吗？else分支是必须的吗？
答：elif 不是必须的  else 是必须的
    # 点评：都不是必须的。


●如果要得到
lst=['s', 'h', 'a', 'n', 'g', 'j', 'i', 'e'], 如何写表达式？
（或者说用另外的几种方式表达上述赋值表达式， ）
答：lst="shangjie"
    """ 点评：不对
        参考答案：
        >>>lst = list( "shangjie" )
        >>>print lst
        >>>['s', 'h', 'a', 'n', 'g', 'j', 'i', 'e']
        
        >>>lst = [ c for c in "shangjie" ]
        >>>print lst
        >>>['s', 'h', 'a', 'n', 'g', 'j', 'i', 'e']
        
        >>>lst = map( lambda x:x, "shangjie" )
        >>>print lst
        >>>['s', 'h', 'a', 'n', 'g', 'j', 'i', 'e']
    """



●有两个字符串 small1="we are "
               small2="pythoner"
 如何得到small="we are pythoner"
 答：small1+""+small2
    """点评：尽量多的去运用你学到的只是去实现，灵活使用。
     参考答案：
        >>> small=small1+small2
        >>> small
        'we are pythoner'
        
        >>> small=''.join( [small1, small2] )
        >>> small
        'we are pythoner'
        
        >>> small = "%s%s" % (small1, small2)
        >>> small
        'we are pythoner'
        
        >>> small=""
        >>> for s in [small1, small2]:
        ...     small+=s
        ...     
        >>> small
        'we are pythoner'
        
        >>> import operator
        >>> small = reduce( operator.add, [small1, small2] )
        >>> small
        'we are pythoner'
        >>> 
     """