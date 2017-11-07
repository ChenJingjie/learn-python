# coding: utf-8
###################
# 习题15：读文件
###################

from sys import argv

script, filename = argv

txt = open(filename)

print "Here`s your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again"
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

# 笔记
# open(file)  打开文件
# 通过open获得的文件对象。 object.read()  读到文件的内容
# object.close()  最后要关闭