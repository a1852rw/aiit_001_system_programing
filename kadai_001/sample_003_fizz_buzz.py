#! /usr/bin/env python3

# 関数はできたのでif文をそうでないものに書き換える
def fb(i):
#    if i % 15 == 0: return "fizzbuzz"
#    elif i % 3 == 0: return "fizz"
#    elif i % 5 == 0: return "buzz"
#    else: return i

# 比較演算子を使って置き換えることに成功

    return (i % 3 == 0)*"fazz" + (i % 5 == 0)* "buzz"

i = 1
while i <= 200:
    print(i,fb(i))
    
    i = i + 1

