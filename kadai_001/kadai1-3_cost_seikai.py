import time
import random

sum = 0

before = time.clock()
for i in range(1000000):
        sum = sum + random.randint(1, 100)
gaptime = time.clock() - before

print("gaptime:", gaptime, flush=True)

# 1⾏⽬: パッケージは1つづつimportする。
# 3⾏⽬: ⼆項演算⼦の両側には空⽩⽂字をいれる。
# 6⾏⽬: :の直前の空⽩⽂字を取る。
# 7⾏⽬: インデント（字下げ）を4つの空⽩⽂字にする。
# 10⾏⽬: ,の直前の空⽩⽂字を取る。
# 10⾏⽬: ()のすぐ内側の空⽩⽂字を取る。
# 10⾏⽬: 引数の=の両側の空⽩⽂字を取る。


#import time, random

#sum=0

#before = time.clock()
#for i in range(1000000) :
#        sum = sum + random.randint(1,100)
#gaptime = time.clock() - before

#print ( "gaptime:" , gaptime , flush = True)
