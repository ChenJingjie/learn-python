# coding: utf-8
###################
# 习题11：提问
###################
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
 print "So，you`re %r old, %r tall and %r heavy." % (
 	age, height, weight) 

 # 笔记
 # 1. print加一个逗号，让输入在同一行
 # 2.raw_input()  接受控制台输入值