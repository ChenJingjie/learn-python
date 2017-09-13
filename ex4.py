# coding: utf-8
#####################
# 习题4：变量和命名
#####################
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_no_driven = cars - drivers  # 没司机的车数量
cars_driven = drivers	# 有司机的车的数量
carpool_capacity = cars_driven * space_in_a_car	# 所有能走的车加起来的座位数量
average_passengers_per_car = passengers / cars_driven # 每辆车平均人数

print "There are", cars, "cars available." # 这里有100量车可以用
print "There are only", drivers, "drivers availabe." # 这里有30个司机可以用
print "There will be", cars_no_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"


