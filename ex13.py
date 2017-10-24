# coding: utf-8
#####################
# 习题13: 参数，解包，变量
#####################

# 另外一种将变量传递给脚本的方法

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "YOur third variable is:", third

# 笔记
# 1.python引入模块的方法  from sys import argv
# 2.运行脚本输入
# python ex13.py first second third