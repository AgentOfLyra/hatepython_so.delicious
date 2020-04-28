'''
彩票的号码有 6 位数字，若一张彩票的前 3 位上的数之和等于后 3 位上的数之和，则称这张彩票是幸运的。本题就请你判断给定的彩票是不是幸运的。

输入格式：
输入在第一行中给出一个正整数 N（≤ 100）。随后 N 行，每行给出一张彩票的 6 位数字。

输出格式：
对每张彩票，如果它是幸运的，就在一行中输出 You are lucky!；否则输出 Wish you good luck.。

输入样例：
2
233008
123456
输出样例：
You are lucky!
Wish you good luck.
'''

# re = []
# N = int(input())
# for i in range(N):
#     char = input()
#     a = int(char[0])+int(char[1])+int(char[2])
#     b = int(char[3])+int(char[4])+int(char[5])
#     if a == b:
#         re.append("You are lucky!")
#     else :
#         re.append("Wish you good luck.")
# for i in re:
#     print(i,end="")
#     print("\n")


import switch as switch

'''
小鲁家的院子里有一棵苹果树，每到秋天树上就会结出10个苹果。苹果成熟的时候，小鲁就会跑去摘苹果（不如我们去帮他吃掉）。
小鲁有个30厘米高的板凳，当他不能直接用手摘到苹果的时候，就会踩到板凳上再试试。 
现在已知10个苹果到地面的高度，以及小鲁把手伸直的时候能够达到的最大高度，请帮小鲁算一下他能够摘到的苹果的数目。假设他碰到苹果，苹果就会掉下来。（苹果很配合哦）

输入格式:
输入包括两行数据。 第1行包含10个100到200之间（包括100和200）的整数（以厘米为单位）分别表示10个苹果到地面的高度，两个相邻的整数之间用一个空格隔开。
 第2行只包括一个100到120之间（包含100和120）的整数（单位：厘米），表示小鲁把手伸直的时候能够达到的最大高度。

输出格式:
输出包括一行，这一行只包含一个整数，表示小鲁能够摘到的苹果的数目。

输入样例:
100 200 150 140 129 134 167 198 200 111
110
输出样例:
5
'''
# import re
# line1 = input()
# apple_height_list = re.split(r'\s+',line1)
# kid_height = int(input())
# re = 0
# for apple in apple_height_list:
#     apple_height = int(apple)
#     if kid_height + 30 >= apple_height:
#         re += 1
# print(re)
'''
下面是一个图书的单价表： 
 计算概论 28.9 元/本 数据结构与算法 32.7 元/本 数字逻辑 45.6元/本 C++程序设计教程 78 元/本 人工智能 35 元/本 计算机体系结构 86.2 元/本 编译原理 27.8元/本 操作系统 43 元/本 计算机网络 56 元/本 JAVA程序设计 65 元/本 
给定每种图书购买的数量，编程计算应付的总费用。

输入格式:
输入一行，包含10个整数(大于等于0，小于等于100)，
分别表示购买的《计算概论》、《数据结构与算法》、《数字逻辑》、《C++程序设计教程》、《人工智能》、《计算机体系结构》、《编译原理》、《操作系统》、《计算机网络》、《JAVA程序设计》
的数量（以本为单位）。每两个整数用一个空格分开。

输出格式:
输出一行，包含一个浮点数，表示应付的总费用。精确到小数点后一位。

输入样例:
1 5 8 10 5 1 1 2 3 4
输出样例:
2140.2
'''
# import re
# sum = 0
# book =  '计算概论 28.9 元/本 数据结构与算法 32.7 元/本 数字逻辑 45.6元/本 C++程序设计教程 78.0 元/本 人工智能 35.0 元/本 计算机体系结构 86.2 元/本 编译原理 27.8元/本 操作系统 43.0 元/本 计算机网络 56.0 元/本 JAVA程序设计 65.0 元/本 '
# book_price_list = re.findall('\d+',book)
# print(book_price_list)
# num = re.split(r'\s+',input())
# for i in range(0, 10):
#     sum = float(book_price_list[i]) * float(num[i]) + sum
# print(float(sum))

'''
给定一个日期，输出这个日期是该年的第几天。

输入格式:
包含三个整数，表示年、月、日。

输出格式:
输出一行，表示该日期是当年的第几天。

输入样例:
2018 2 2
输出样例:
33
'''
# import re,date
# dat = re.split(r'\s+',input())
# year = int(dat[0])
# month = int(dat[1])
# day = int(dat[2])
# print(date.year_time(year,month,day).the_dayth())
'''
在一个序列（下标从1开始）中查找一个给定的值，输出第一次出现的位置。

输入格式:
第一行包含一个正整数n，表示序列中元素个数。1 <= n <= 10000。 第二行包含n个整数，依次给出序列的每个元素，相邻两个整数之间用单个空格隔开。 第三行包含一个整数x，为需要查找的特定值。

输出格式:
若序列中存在x，输出x第一次出现的下标；否则输出"not found"。

输入样例:
5
2 3 6 7 3
3
输出样例:
2
'''

'''
过年了，村里要庆祝一下。村长对村民说：村里有一笔钱作为奖金。
让每个人写一个纸条上来，谁写的数与奖金最接近，就算猜中，这笔奖金就归谁，如果有多个人猜中，则平分这笔钱。
现在让我们来写一段程序算算都有哪些人得到了奖金？得到多少？

输入格式:
第一行包含2个整数 n,m，分别表示村民人数和村里的奖金总数。 第二行包含n个整数，整数之间以一个空格分开。表示1号,2号，。。。，n号村民猜测的奖金数。（1<=n<=5000）

输出格式:
输出分两行。 第一行包含若干整数，表示得到奖金的村民编号， 第二行包含一个实数（保留1位小数），表示人均奖金金额。

输入样例:
10 100
50 60 70 80 90 90 110 120 130 140
输出样例:
在这里给出相应的输出。例如：

5 6 7
33.3
'''
# import re
# i1 = input()
# list_po_mon = re.split(r'\s+',i1)
# po = int(list_po_mon[0])
# mon = int(list_po_mon[1])
# inp2 = input()
# list_guess = re.split(r'\s+',inp2)
# cnt = 0
# err = []
# ret = []
# min = mon
# for i in range(0,po):
#     err.append(abs(int(list_guess[i]) - mon))
#     if err[i] < min:
#         min = err[i]
#
# for i in range(po):
#     if min == int(err[i]):
#         cnt += 1
#         ret.append(i+1)
# mon /= cnt
# for i in range(0,cnt):
#     if i <cnt-1:
#         print(ret[i],end=" ")
#     if i == cnt-1:
#         print(ret[i],end="")
# print(end="\n")
# print(round(mon,1),end="")
'''
输入一行字符，统计出其中数字字符的个数。
输入格式:
一行字符串，总长度不超过255。
输出格式:
输出为1行，输出字符串里面数字字符的个数。
输入样例:
Peking University is set up at 1898.
输出样例:
在这里给出相应的输出。例如：
4
'''
# import re
# word = input()
# num_list = re.findall(r'\d+', word)
# cnt = 0
# for num in num_list:
#     for i in num:
#         cnt += 1
# print(cnt)
'''
为防止情报被截获，一般要对情报加密。
一种简单的的加密方法是这样的，
对给定一个字符串，把其中从A-Y，a-y的字母用其后继字母替代，把z和Z用a和A替代，其他字符不变，从而得到一个加密字符串。

输入格式:
包含一个字符串，长度小于80个字符。

输出格式:
输出每行字符串的加密字符串。

输入样例:
Hello! How are you!
输出样例:
Ifmmp! Ipx bsf zpv!
'''
#      字符和ascii相互转换
# 用户输入字符
# c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: "))
#
# print(c + " 的ASCII 码为", ord(c))
# print(a, " 对应的字符为", chr(a))
# import  sys
#  !/usr/bin/env python3
# word = sys.stdin.readline()
# for letter in word:
#     if ord(letter) == 90 or ord(letter) == 122:
#         print(chr(ord(letter)-25), end='')
#     elif (ord(letter) >= 65 and ord(letter) <= 89) or (ord(letter) >= 97 and ord(letter) <= 121):
#         print(chr(ord(letter)+1), end='')
#     else:
#         print(letter, end='')


'''
身份证的最后一位是根据前17位数字计算出来的检验码。
计算方法是：将身份证号码前17位数分别乘以不同的系数。
从第1位到第17位的系数分别为：7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2；
将乘积之和除以11，余数可能为0 1 2 3 4 5 6 7 8 9 10。
则根据余数，分别对应的最后一位身份证的号码为1 0 X 9 8 7 6 5 4 3 2。编写程序，输入身份证号码前17位，输出对应的检验码。

输入格式:
包含身份证号码的前17位

输出格式:
对应的检验码

输入样例:
34052419800101001
输出样例:
X
'''
# class identify_surer(object):
#     __modulus = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
#     __no = ['1', '0', "X", '9', '8', '7', '6', '5', '4', '3', '2']
#     def __init__(self, number):
#         self.numlist = []
#         self.modsum = 0
#         self.number = number
#         for i in self.number:
#             self.numlist.append(int(i))
# #         self.long = len(self.numlist)
# #     def caculater(self):
# #         for i in range(0, self.long):
# #             self.modsum += self.__modulus[i] * self.numlist[i]
# #         self.modsum %= 11
# #         return self.modsum
# #     def surer(self):
# #         print(self.__no[self.caculater()])
#
# num = input()
# identify_surer(num).surer()

'''
为了获知基因序列在功能和结构上的相似性，
经常需要将几条不同序列的DNA进行比对，以判断该比对的DNA是否具有相关性。 
现比对两条长度相同的DNA序列。
首先定义两条DNA序列相同位置的碱基（表示为一个字符）为一个碱基对，
如果一个碱基对中的两个碱基相同的话，则称为相同碱基对。接着计算相同碱基对占总碱基对数量的比例，
如果该比例大于等于给定阈值时则判定该两条DNA序列是相关的，否则不相关。

输入格式:
有三行，第一行是用来判定出两条DNA序列是否相关的阈值，随后2行是两条DNA序列（长度不大于500）。

输出格式:
若两条DNA序列相关，则输出“yes”，否则输出“no”。

输入样例:
0.85
ATCGCCGTAAGTAACGGTTTTAAATAGGCC
ATCGCCGGAAGTAACGGTCTTAAATAGGCC
输出样例:
yes
'''
#ox = float(input())
# a = input()
# b = input()
# long = len(a)
# cnt = 0
# for i in range(0,long):
#     if a[i] == b[i]:
#         cnt += 1
# cnt /= long
# if cnt >= ox:
#     print("yes")
# else:
#     print("no")
'''
“扫描识别”你知道是怎么回事吧？它的意思就是：
先用扫描仪把纸上的文字扫描成一个图片，再用识别软件把那个图片中的文字识别出来，最后生成一个文本文件。
这对于需要把大量的纸稿录入成电子文档的人来说，当然是非常方便的。 以现有的技术，扫描效果是比较理想的，
但识别效果还不十分另人满意，经常会出现错误，尤其是当两个字形状特别接近的时候，而且，这种错误是很难用眼睛看出来的。 
我们的纸稿上有一个数字串，识别之后得到的字符串保存在输入文件中，这个串可能有识别错误。
已知，可能出现的错误有如下几种： 
1、把数字0错误地识别为大写字母O； 
2、把数字1错误地识别为小写字母l； 
3、把数字2错误地识别为大写字母Z； 
4、把数字5错误地识别为大写字母S； 
5、把数字6错误地识别为小写字母b； 
6、把数字8错误地识别为大写字母B； 
7、把数字9错误地识别为小写字母q。 
你的改正方案是：如果字符串中出现了上述字母，请替换为原来的数字。最后把改正之后的数字串输出。

输入格式:
只有一个字符串，表示识别后得到的字符串。串的长度不超过100。

输出格式:
只有一个数字串，表示改正后的数字串。

输入样例:
在这里给出一组输入。例如：

321lO88BqS
输出样例:
在这里给出相应的输出。例如：

3211088895
'''
# 1、把数字0错误地识别为大写字母O；
# 2、把数字1错误地识别为小写字母l；
# 3、把数字2错误地识别为大写字母Z；
# 4、把数字5错误地识别为大写字母S；
# 5、把数字6错误地识别为小写字母b；
# 6、把数字8错误地识别为大写字母B；
# 7、把数字9错误地识别为小写字母q。
# numlist = input()
# chrlist = ['O','l','Z','','','S','b','','B','q']
# for num in numlist:
#     if (ord(num) >= 65 and ord(num) <= 90) or (ord(num) >= 97 and ord(num) <= 122):
#         for i in range(len(chrlist)):
#             if num == chrlist[i]:
#                 num = str(i)
#     print(num,end="")

'''
本题要求编写程序，求一个给定的m×n矩阵各行元素之和。

输入格式：
输入第一行给出两个正整数m和n（1≤m,n≤6）。随后m行，每行给出n个整数，其间

以空格分隔。

输出格式：
每行输出对应矩阵行元素之和。

输入样例：
3 2
6 3
1 -8
3 12
输出样例：
9
-7
15
'''


# i = 0
# m,n = input().split(" ")
# sum = 0
# douqr = []
# while i < int(m):
#     a = input().split(" ")
#     douqr.append(a)
#     i += 1
# for l in range(len(douqr)):
#     for n in douqr[l]:
#         sum += int(n)
#     print(sum)
#     sum = 0
'''
上三角矩阵指主对角线以下的元素都为0的矩阵；主对角线为从矩阵的左上角至右下角的连线。

本题要求编写程序，判断一个给定的方阵是否上三角矩阵。

输入格式：
输入第一行给出一个正整数T，为待测矩阵的个数。接下来给出T个矩阵的信息：每个矩阵信息的第一行给出一个不超过10的正整数n。随后n行，每行给出n个整数，其间以空格分隔。

输出格式：
每个矩阵的判断结果占一行。如果输入的矩阵是上三角矩阵，输出“YES”，否则输出“NO”。

输入样例：
2
3
1 2 3
0 4 5
0 0 6
2
1 0
-8 2
输出样例：
YES
NO
'''
# class square(object):
#     def __init__(self, k):
#         self.cnt = 0
#         self.ret = []
#         # 二维数组
#         self.sq = []
#         # 输入一维数组
#         self.a = []
#         # 阶次
#         self.k = k
#     def square_input(self):
#         for i in range(self.k):
#
#             self.a = input().split(" ")
#             self.sq.append(self.a)
#
#     def caculater(self):
#         for i in range(self.k):
#             for n in self.sq[1]:
#                 if n == '0':
#                     self.cnt += 1
#                 if self.cnt != i:
#                     self.ret.append(0)
#                 else:
#                     self.ret.append(1)
#                 self.cnt = 0
#     def check(self):
#         self.cnt = 0
#         for i in range(len(self.ret)):
#             if self.ret[i] == 0:
#                 self.cnt = 1
#                 break
#         if self.cnt == 0:
#             print("YES")
#         else:
#             print("NO")
#     def main(self):
#         self.square_input()
#         self.caculater()
#         self.check()
# if __name__ == '__main__':
#     a = int(input())
#
#     for i in range(a):
#         k = int(input())
#         square(k).main()



# n = input()
# flag = 0
# m = input().split(" ")
# for i in range(len(m)-1):
#     if(int(m[i+1])>int(m[i])):
#         flag = 1
#         print("No")
#         break
#     else:
#         flag = 0
# if(flag == 0):
#     print("Yes")


'''
输入一个整数矩阵，计算位于矩阵边缘的元素之和。所谓矩阵边缘的元素，就是第一行和 最后一行的元素以及第一列和最后一列的元素。

输入格式:
第一行分别为矩阵的行数m和列数n（m < 100，n < 100），两者之间以一个空格分开。 接下来输入的m行数据中，每行包含n个整数，整数之间以一个空格分开。

输出格式:
输出对应矩阵的边缘元素和。

输入样例:
3 3
3 4 1
3 7 1
2 0 1
输出样例:
在这里给出相应的输出。例如：

15
'''
# import re
# line = []
# row = []
# sum1 = 0
# m1,n1= input().split(" ")
# m = int(m1)
# n = int(n1)
# for i in range(m):
#     line.append(re.split(r"\s+",input()))
# row.extend(line[0])
# if m >= 2:
#     for i in range(1, m-1):
#         if n >= 2:
#             row.append(line[i][0])
#             row.append(line[i][-1])
#         else:
#             row.append(line[i][0])
#     row.extend(line[-1])
# if m == 1:
#     for i in range(1, m):
#         row.extend(line[i])
# for i in range(len(row)):
#     sum1 += int(row[i])
# print(sum1)
'''
int p; //这是一个普通的整型变量  
int *p; 
//首先从P 处开始,先与*结合,所以说明P 是一个指针,然后再与int 结合,说明指针所指向的内容的类型为int 型.所以P是一个返回整型数据的指针  
int p[3]; 
//首先从P 处开始,先与[]结合,说明P 是一个数组,然后与int 结合,说明数组里的元素是整型的,所以P 是一个由整型数据组成的数组  
int *p[3]; //首先从P 处开始,
先与[]结合,因为其优先级比*高,所以P 是一个数组,然后再与*结合,说明数组里的元素是指针类型,然后再与int 结合,说明指针所指向的内容的类型是整型的,
所以P 是一个由返回整型数据的指针所组成的数组  
int (*p)[3]; //首先从P 处开始,先与*结合,说明P 是一个指针然后再与[]结合(与"()"这步可以忽略,只是为了改变优先级),
说明指针所指向的内容是一个数组,然后再与int 结合,说明数组里的元素是整型的.所以P 是一个指向由整型数据组成的数组的指针  
int **p; //首先从P 开始,先与*结合,说是P 是一个指针,然后再与*结合,说明指针所指向的元素是指针,然后再与int 结合,说明该指针所指向的元素是整型数据.
由于二级指针以及更高级的指针极少用在复杂的类型中,所以后面更复杂的类型我们就不考虑多级指针了,最多只考虑一级指针.  
int p(int); //从P 处起,先与()结合,说明P 是一个函数,然后进入()里分析,说明该函数有一个整型变量的参数,然后再与外面的int 结合,说明函数的返回值是一个整型数据  
Int (*p)(int); //从P 处开始,先与指针结合,说明P 是一个指针,然后与()结合,说明指针指向的是一个函数,
然后再与()里的int 结合,说明函数有一个int 型的参数,再与最外层的int 结合,说明函数的返回类型是整型,所以P是一个指向有一个整型参数且返回类型为整型的函数的指针  
int *(*p(int))[3]; //可以先跳过,不看这个类型,过于复杂从P 开始,
先与()结合,说明P 是一个函数,然后进入()里面,与int 结合,说明函数有一个整型变量参数,然后再与外面的*结合,说明函数返回的是一个指针,,
然后到最外面一层,先与[]结合,说明返回的指针指向的是一个数组,然后再与*结合,说明数组里的元素是指针,然后再与int 结合,
说明指针指向的内容是整型数据.所以P 是一个参数为一个整数据且返回一个指向由整型指针变量组成的数组的指针变量的函数. 
以后，每遇到一个指针，都应该问问：这个指针的类型是什么？指针指的类型是什么？该指针指向了哪里？（重点注意）
'''




