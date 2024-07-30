# 老师：杨淑娟；
# https://www.bilibili.com/video/BV1Z44y157pb?spm_id_from=333.999.0.0
# 开始时间：2022.01.25
s='3.14+3'
print(s,type(s))
x=eval(s) #执行了加法运算
print(x,type(x))

#eval()函数经常和input（）函数一起使用，用来获取用户输入的数值型
age=eval(input('请输入你的年龄：'))#将字符串类型转成了int类型，相当于int（age）
print(age,type(age))

height=eval(input('请输入你的身高：')) #将字符串类型转成了float类型，相当于float（height）
print(height,type(height))
#hello='北京欢迎你'
#print(hello)
#使用eval报错的情况
print(eval('hello'))#NameError: name 'hello' is not defined. Did you mean: 'help'?

