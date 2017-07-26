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
- 
