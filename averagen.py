#!/usr/bin/env python3
print("please enter count number: ")
N = int(input())
# N = 10
sum = 0
count = 0
print("please enter",N,"numbers: ")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("average = {:.2f}".format(average))
