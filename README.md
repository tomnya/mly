#This is a simple lex implemented by python.

##对于test.pl文件格式的说明:
test.pl对标准的.l文件的一个简单的python处理，  
它只支持Tompson正则及一些简单的扩展表示，因此所用的元字符十分有限，列举如下：  

\*	：	闭包运算(出现0次或任意多次)   
|	：	或运算  
\ 	：	如ab, 连接运算(两个正则之间不加运算符时，默认就是连接运算)   
()	:	用来表示一个子表达式   

//事实上以上四类元字符，已经可以完整地表达正则的语义   
//以下的元字符只是为了表示的方便   
A 	:	表示一个任意字母，相当于(a|b|c|...|x|y|z|A|B|C...|X|Y|Z)   
B  	:	表示一个空白字符，相对于(\b|\n)   
D 	: 	表示一个任意数字，相当于(0|1|2|3|4|5|6|7|8|9)   
\	: 	转义元字符，当使用以上元字符本身时，可用\进行转义，如\A, 表示纯粹的字符A    

2013.8.6试一下
