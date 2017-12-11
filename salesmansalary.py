#!/usr/bin/env python3
basic_salary = 25000
bonus_rate = 200
commision_rate = 0.02
numberofcamera = int(input("camera sold: "))
price = float(input("total prices: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)
print("bonus = {:6.2f}".format(bonus))
print("commision = {:6.2f}".format(commision))
print("gross salary = {:6.2f}".format(basic_salary + bonus + commision))
