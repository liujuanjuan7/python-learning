# 老师：杨淑娟；
# https://www.bilibili.com/video/BV1Z44y157pb?spm_id_from=333.999.0.0
# 开始时间：2022.01.25
lucky_number=8 #创建一个整型变量lucky_number，并为其赋值为8
my_name="刘娟"#字符串类型的变量
print (my_name)
print(my_name,"的幸运数字为：",lucky_number)
print('lucky_number的数据类型：',type(lucky_number))
#变量的值可以更改
lucky_number='北京欢迎你'
print('lucky_number的数据类型：',type(lucky_number))
#Python动态修改变量的数据类型，通过赋不同类型的值就可以修改了
no=number=1024 #python允许多个变量指向同一个值
print(no,number)
print(id(no))
print(id(number))