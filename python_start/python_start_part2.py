1.假设lst为：
>>> lst = range(10)
要获取子序列[2, 3, 4, 5, 6]，应如何操作？(使用尽可能多的方法实现)
range(2,7,1)
lst[2:7]
8.假设lst为：
>>> lst = [ 1, 2, 3 ]
至少写出三种方法将lst反序输出，方法越多越好。
lst.reverse()
lst.sort(reverse=True)
    """ 可以参考一下下面的方法：
        方法一：使用list自带的sort()对lst排序（修改lst本身结构）
            def print_list(lst):
                lst.sort(reverse=True)
                for k in lst:
                    print k,
                
        方法二：使用list自带的rever()对lst进行反转（修改lst本身结构）
            def print_list(l):
                l.reverse()
                for k in l:
                    print k,
        
        方法三：使用内置函数sorted（）对lst进行倒序（不修改lst本身结构）
            def print_list(l):
            for k in sorted(l,reverse=True):
                print k,
        
        方法四：使用列表的负下标
            def print_list(l):
                print lst[::-1]
        
        方法五：使用list.pop()
            def print_list(l):
                while len(lst):
                    print lst.pop(),
    """

10.两个set可以相加吗？可以相减吗？
可以相加  可以相减

13.一行代码获取N(含N)之前的所有偶数，N为自然数。方法越多越好。
range(2,N,2)
[i for i in range(N+1) if i%2 ==0]
14.假设lst为：
>>> lst = [ 1, 'a', 2, 'b', 3, 'c' ]
要求一行代码得到如下结果：
['d', 97, 'e', 98, 'f', 99]
实现方法越多越好。
答:
    [ ord(i) if type(i)==str else chr(i+99) for i in lst ]
 或 [chr(99+i)if type(i)==int else ord(i) for i in lst]
16.使用最简短的代码打印乘法表，要求输出格式为： 方法越多越好
1*1=1	7
1*2=2	2*2=4	
1*3=3	2*3=6	3*3=9	
1*4=4	2*4=8	3*4=12	4*4=16	
1*5=5	2*5=10	3*5=15	4*5=20	5*5=25	
1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36	
1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49	
1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64	
1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81	

答：
       for i in range(1,10):
          a=''
          b=''
          for j in range(1,i+1):
            a="%d*%d=%d"%(i,j,i*j)
            b=b+" "+a
          print b
    "\n".join([" ".join(["%s*%s=%s"%(i,j,i*j) for j in range(1,i+1)]) for i in range(1,10)])
19.假设s='abc'，要求一个循环输出对应“下标”及其“值”：
>>> for ???:
...     print ???
...     
0 a
1 b
2 c
>>> 
方法越多越好。
 for i in s:
     print i.index(),"",i
    # 点评：
        # 基础的只是没有掌握好，不能使i.index(),可以是s.find( i )
         s.index(i)
   for i in range(len(s)):
     print "%d %s"%(i,s[i])
     
i=0
while i<len(s):
    print "%d %s"%(i,s[i])
    i=i+1

20.假设有以下代码：
>>> import datetime
>>> today = datetime.date.today().strftime( '%Y-%m-%d' )
>>> today   
'2011-03-21'
>>> 
要求将today格式化为'20110321'，用尽可能短的代码、尽可能多的方法实现。
today=datetime.date.today().strftime('%Y%m%d')
 today="%s%s%s"datetime.date.today()
 # 点评:字符串传值的语法没有记住，应该是'%s' %('hello')
        """
        方法一：
            today = datetime.date.today().strftime( '%Y%m%d')
       方法二：
            today = today.replace( '-', '' )
       方法三：
            today = ''.join( today.split( '-' ) )
        """
today=''.join(str(datetime.date.today()).split('-'))
today=datetime.date.today().strftime('%Y%m%d')

24.假设有以下dict变量：
>>> d = {'name':2, 'sex':1, 'age':3 }
如何按value排序输出？用尽可能短的代码、尽可能多的方法实现。
    lst=[]
    lst=d.items()
    lst.sort(key=lambda x:x[1])
    sorted(d.items(),key=lambda x:x[1])
    #点评：不错
    
27.根据以下对函数f()的调用结果，编写f()函数：
>>> f( 'abc' )
abc

>>> f( 'abc', 1 )
abc
1
>>> f( 'abc', 1, 2, 3 )
abc
1 2 3
>>> f( 'abc', 1, 2, 3, x=1 )
abc
1 2 3
x 1
>>> f( 'abc', 1, 2, 3, x=1, y=2, z=3 )
abc
1 2 3
x 1
y 2
z 3
>>> 
def f(str1,*arg,**keywords):
    a=''
    b=''
    print str1
    for i in arg:
        a=str(i)
        b=b+""+a
    print b
    for k in keywords.keys():
        print "%s %s"%(k,keywords[k])

28.写出以下代码的输出，并说明为什么？
>>> i = 1
>>> def f(): i = 2
...     
>>> f()
>>> print i
 1 因为i=2的name space是局部的只在函数里起作用，而输出的i为全局范围的所以应输出1
    # 点评：就是考察变量的作用域的问题
29.简述function、class、module、package的区别和关系。
   class 中可以包含functions 
   functions中不可以包含class
   module和class 都是独立的name space
   module 中包含class 、functions等
   package是module的集合 
    # 点评：总体来讲还是可以的，参考下面的答案：
        # function是这四个对象中的最小变量，一个小功能的代码块。
        # class是属性和function的集合。
        # module是一个独立的py程序，不仅可以包含function，也可以包含class，甚至可以平铺直叙的直接写代码
        # package是联系性强的py文件的集合。

30.你编写了一个module：C:\MyTest\HelloWorld.py，其中有一个printHelloWorld() function，如何在IDLE中调用它？
 HelloWorld.py中内容：
 """
 This is a module.
 """
 def printHelloWorld():
     print 'HelloWorld!'
 if '__name__'=='__main__'
    printHelloWorld()
 调用：
  import HelloWorld
  HelloWorld.printHelloWorld()
    # 点评：这个就是考察模块之间如何引用的问题,如何把访问路径成为python的默认路径
    # 答案：
    """
        import sys
        sys.path.append( r'C:\MyTest' )
        from HelloWorld import printHelloWorld 
    """  
    
    
    
    
    
    
31.如何识别一个目录是否为package？
 可以查看目录中文件是否为module文件，若是，则为包，若不是，则不是包
    # 点评：正确答案（python中的package必须包含一个__init__.py的文件）。
32.按照如下输出结果，编写一个class：
>>> mike = MyClass( 'mike', '19850321' )
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 7, in __init__
RuntimeError: 生日格式必须为YYYY-MM-DD
>>> mike = MyClass( 'mike', '1985-03-21' )
>>> print mike.getAge()

答：方法一：
    import datetime,re
    class Myclass( object ):
        def __init__(self, name, birthday):
            self.name=name
            if not re.match(ur"\d{4}-\d{2}-\d{2}",birthday):
                raise RuntimeError, u'YYYY-MM-DD'
            self.birthday=birthday
        def getAge(self):
            d1 = datetime.datetime.now()  
            birthday = self.birthday.split('-')
            d2 = datetime.datetime(int(birthday[0]),int(birthday[1]),int(birthday[2]))   
            return (d1 - d2).days/365
    方法二：
    import datetime
    class MyClass( object ):
        def __init__( self, name, birthday ):
            self.name = name
            try:
                self.birthday = datetime.datetime.strptime( birthday, '%Y-%m-%d' )
            except:
                raise RuntimeError( '生日格式必须为YYYY-MM-DD' )
        def getAge( self ):
            return datetime.date.today().year - self.birthday.year

26.取用dict中不存在的key时会抛出KeyError Exception：
>>> d = {}
>>> print d['a']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'a'
>>> 
如何避免发生这种错误？
d.get('a',default)

33.根据以下输出，用最少的代码编写A、B、C类层次体系：
>>> b = A.createObj('B')
>>> c = A.createObj('C')
>>> print isinstance( b, B )
True
>>> print isinstance( c, C )
True
>>>
import sys
class A:
    class B:
        pass
    class C:
        pass
    def createObj(str)
    if str=='B'
      return B()
    elif str=='C'
      return C()
      











35.有文件a.txt，内容为“abc”；现在要求将其内容改为“123abc”，请写出最简洁的代码。

f=open("/a.txt",w)
f.write("123abc")
f.close()
    # 点评：
        # 1.第一行代码的w要加上引号；
f=open("/a.txt","w")
f.write("123abc")
f.close()

a=''
a=a+open("a.txt","r")
f=open("a.txt","w")
f.write(a)
f.close()
36.简述python语言中， str() 函数和repr() 函数的作用， 两者的相同和不同之处
str()将对象转化成字符串
repr()返回str字符串
