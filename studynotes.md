# Learn python the hard way 学习笔记
> Exercise note

## Exercise 1
可以通过将某句话用#变成comments让python打印时无视它
也可以通过制造list将要打印的所有项目放进list里，然后通过print(list[0:X])打印前X项的项目。

## Exercise 2
用 # comments 来让python无视某句话，同时comments也可以方便programmer理解某段code的含义。

## Exercise 3
- a % b用来算a除以b的余数
- 输入一个等式（带有=，> or <), python会根据等式是否正确直接返回true或者false.
- 在数字后面加 .0 可以让结果精确到后一位小数，但好像用 .00 不能精确到后两位小数，为什么？

## Exercise 4
- 可以通过 = 来给variable 赋值，也能通过variable A = variable B来建立两个变量的联系。

## Exercise 5
%s 是用来格式化某变量为字符串； %d 格式化某变量为整数；%f 则可以用来格式化变量并显示floating
在探索如何显示小数并控制小数位的地方折腾了一段时间，一开始试着直接除3位的小数，发现结果还是不对,后来上网搜索发现用**%.Xf**来控制显示X位小数。

## Exercise 6
- 通过formatter, 可以很好的在print strings时将其他变量放入string内。
- %r 可以用来打印raw data,
>如 print "%r, %r" % ('one', 'two') --> 'one','two'
print "%s, %s" % ('one', 'two') --> one, two.

## Exercise 7
- 在print时可以用“,”将分隔的字符串打印在一行
- 通过乘号“\*n"来print语句n遍
- 通过加号“\+”来连续print多个字符，并可以通过comma","来把这些字符放在同一行

## Exercise 8
- %r 会打印raw data而保留完整的原始数据
- 在print字符时，双引号内字符若不带单引号，则结果会显示为单引号内带字符，如果双引号字符
内有单引号，则结果会显示为双引号内带字符。

## Exercise 9
- """ 用三引号可以打印多段字符
- """ 和 ''' 作用一样，看个人偏好。
- \\ 是 backlash, 可以用来忽略命令符而直接print出来。\n可以用来另起一行Linefeed

## Exercise 10
- 用 \r 可以缩进（即tab)。\r和\n可以连在一起使用“\r\n”

## Exercise 11
- 利用raw_input()可以向用户要输入数据 **这是2.7版本python有raw_input()和input(),前者将所有输入视作字符串并输出，后者只接受数字并输出数字类型**
- python3已将raw_input()与input()整合，统一使用input(),接受任意输入，输出为字符串。

## Exercise 12
- 可以直接通过raw_input("括号内放入指导语")的指导用户输入指定数据，而不用每次要完
数据print指导语

## Exercise 13
- python 文件是个脚本，然后调用sys即python本身带有的模块argv可以存几个变量，然后在提取出来。

## Exercise 14
- 这个exercise主要还是回顾input()的用法以及怎样更高效地给出指导语，也就是先将指导语放入一个变量里，后一直用这个变量就行了，而不是每次都打入。

## Exercise 15
- pydoc file用不了, read()的pydoc是上网搜input&output的相关文档看到的，另外读txt文件还有readline()命令，也就是一行一行读。还可以list(file),或者f.readlines. [pydoc Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

## Exercise 16
- 查了下官方文档，"w"写入模式在文件已经存在的情况下就会truncate这个文件，所以后面的truncate是多余的。truncate()可以改写文件至指定大小，所以也不一定是用来删除所有内容。
- 后面一行target.write()打印方法还挺多的，可以直接用“+”将几行与"\\n"结合在一起，也可以用formatter。

## Exercise 17
- ```cat test.txt``` cat is short for concatenate. 是用来读取文件内容常用的一个命令。
- 从os.path调用的exists功能可以用来快速检测某个文件是否存在。

## Exercise 18
- “\*args”里的"\*"相当于是说将后面给出的variable都放进args里作为一个list。
- 写function的时候经常忘记“：”，特别写high了的时候这些细节就容易漏，写个checklist还是很有实践意义的，配合atom本身自带的indent还是能快速查出问题的。

## Exercise 19
- 这个小结练习主要想说明函数里面的参数可以非常多样，可以是某个variable,可以是math,也可以是variable和math的集合。组合方式很多，具体情况可以具体分析。

## Exercise 20
- .read()是读取文件所有内容，也可加入参数.read(size),读取指定字符数。
- .seek()则是将文档移动到指定位置，若参数为0，则是移动到起始位置。
- .readline()则是一行一行进行读取，读完一行，下一次读取会读取下一行内容，直到读取返回是空值，则说明内容已经读取完。
- "+="是in-place operators, 虽然 a += 1 的结果与 a = a + 1相同，但是"+="的做法是直接更改老的变量，而a = a + 1这个重新赋值的方法，则是变成一个新的值，原本的a值没有改变，和 b = a + 1的形式相同。
[10.3.2. Inplace Operators](https://docs.python.org/3/library/operator.html) [Stack Overflow](https://stackoverflow.com/questions/41446833/what-is-the-difference-between-i-i-1-and-i-1-in-a-for-loop)

## Exercise 21
- 写这节的时候出现了一个 Nonetype的报误，有一行的数据有问题，但是仔细检查那一行并没有发现什么问题，把%d改成%r之后再跑一次就发现了问题，问题不在那一行，而是开头乘法的function忘了return数值了，看来debugging用%r真是一个不错的选择。
- return给我的感觉像是赋值，但是是给函数的结果赋值。
- function也可以进行多重嵌套，虽然一行就解决，不过看起来还是挺复杂的，实践中还是需要comments进行解释吧。

## Exercise 24
- 这节题目主要是回顾，包括"\\"escapes,还有function的组合，值得注意的是funtion也可以直接和formatter组合在一起，而不用一个一个去写每个变量，方便快捷。

## Exercise 25
- funtion里面通过```"""help sentence"""```来给funtion进行功能解说与注明，如```def sort_words(words):
    """Sorts the words."""
    return sorted(words)```
后续可以通过help()来查看所有funtion以及funtion的注明功能，非常方便和清晰。
- 在python里，一般起始数字是0，而不是1，除非特殊情况规定从1到n开始数时，1才是起始数字。而倒数第一则是-1。
- python里调用funtion可以通过script.funtion()进行，也可以直接先```from ex25 import *```来把所有funtion都调用进来，这样使用的时候就不需要```ex25```的前缀了。

## Exercise 26
- 这题主要考察ex24和ex25的知识点，以及检查问题关注细节的能力。
- 拼写错误比较好抓，反着读code比较容易找，但有些时候还是会忽略标点的问题，如function之后“：”就漏了。
- 66行 ```jelly_beans, jars, crates = secret_formula(start_point)``` 里只能用"=",而不能用“==”,而且函数必须在后面不能放在前面，报错信息是```SyntasError: can't assign to funtion call```,根据错误信息反思了一下，函数不能赋值，也就是被赋值的项目必须放在前面。
- 虽然 \\t 可以让字符串里缩进，但是读取的时候不是当做' '空格读取的，所以后面分割句子的时候就不能很好的完成。

## Exercise 27 - 28
- 逻辑部分还算熟练，值得注意的是所有operator其实都是有个python自带函数的。详情见[Operators](https://docs.python.org/3/library/operator.html)
- 几个不是很熟的operator

Operators | funtion | 作用
----------|---------|----------
a // b   | floor division | 地板除，得到不到于结果的最大整数值
a ^ b | bitwise exclusive | 只要input相同，则返回“1”，否则返回“0”
a & b| bitwise and | 返回 a and b 的逻辑值
a \| b | bitwise or | 返回 a or b 的逻辑值


## Exercise 29
