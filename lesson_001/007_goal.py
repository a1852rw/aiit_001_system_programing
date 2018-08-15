#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def goal(count):
	if count >= 10:
		count = "many"
		return("Number of golals: " + count)
	else:
		return("Number of goals: " + str(count))

print(goal(4))
print(goal(9))
print(goal(10))
print(goal(99))

# 要件1：ゴールの数(count)を受け取って"Number of goals:<count>"を返すgoal関数を書く(<count>は受け取った値)
# 要件2：countが10以上の場合は実際の値の代わりに'many'を使う

# 出力1：Number of goals: 4
# 出力2：Number of goals: 9
# 出力3：Number of goals: many
# 出力4：Number of goals: many
