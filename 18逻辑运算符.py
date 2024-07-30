# 老师：杨淑娟；
# https://www.bilibili.com/video/BV1Z44y157pb?spm_id_from=333.999.0.0
# 开始时间：2022.01.25
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('----------------------------')
print(8>7 and 6>5) #True and True
print(8>7 and 6<5)  #True and False)
print(8<7 and 6>5) #False and True
print(8<7 and 10/0)  #当第一个表达式为False时，不计算第二个表达式
print(8<7 and 6<5)#False and False

print('------------------------------')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(8>7 or 10/0) #当第一个表达式为True时，不执行第二个表达式

print('------------')
print(not True)
print(not False)
print( not 8>7)