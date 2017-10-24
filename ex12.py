# coding: utf-8
###################
# 习题12：提示别人
################### 
# raw_input(promote). raw_input() 用法

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("how much do you weight")

print "So, you`re %r old, %r tall and %r heavy." % (age, height, weight) 

# pydoc raw_input  命令行输入，可以看该函数用法