# 老师：杨淑娟；
# https://www.bilibili.com/video/BV1Z44y157pb?spm_id_from=333.999.0.0
# 开始时间：2022.01.25
x=20#直接赋值，将20赋值给y
y=10
x=x+y
print(x)
x+=y
print(x)
x-=y #x=x-y
print(x)
x*=y
print(x)
x/=y
print(x)
x%=2 #x=x%2
print(x)
z=3
y//=z#整除 y=y//z
print(y)

y**=2
print(y) #y=y**2 y的2次幂
#python支持链式赋值
a=b=c=100 #相当于执行了a=100，b=100，c=100
print(a,b,c)

#python支持系列解包赋值
a,b=10,20 #相当于执行a=10，b=20
print(a,b)

print('-----------------如何交换两个变量的值--------')
#emp=0
#emp=a #将a的值赋值给temp，temp的值为10
#=b    #将b的值赋值给a，a的值为20
#=temp#将temp的值赋值给b，b的值为10
#rint(a,b)

a,b=b,a #将a的值赋值给b，将b的值赋值给a
print(a,b)

