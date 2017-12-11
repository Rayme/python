#!/usr/bin/env python3
fahreheit = 0
print("fahreheit celsius")
while fahreheit <= 250:
    celsius = (fahreheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahreheit , celsius))
    fahreheit = fahreheit + 25
