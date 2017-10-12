# coding:utf-8
#######################
# 习题8：打印，打印
#######################
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn`t sing.",
		"So I said goodnight."
	)
print formatter % (u"我",u"是",u"小",u"寒")