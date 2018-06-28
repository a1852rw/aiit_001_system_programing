#! /usr/bin/env python3

def fb(i):
    if i % 15 == 0: return "fizzbuzz"
    elif i % 3 == 0: return "fizz"
    elif i % 5 == 0: return "buzz"
    else: return i

i = 1
while i <= 200:
    print(i,fb(i))
    
    i = i + 1

