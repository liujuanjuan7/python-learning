# 老师：杨淑娟；
# https://www.bilibili.com/video/BV1Z44y157pb?spm_id_from=333.999.0.0
# 开始时间：2022.01.25
fp=open('../.idea/note.txt', 'w')#打开文件 w-->write
print('北京欢迎你',file=fp) #输出到文件中
fp.close()#关闭文件

'''第二种方式，使用文件读写操作'''
with open('D:/python learning file/test1.txt','w') as file:
    file.write('奋斗成就更好的你')
