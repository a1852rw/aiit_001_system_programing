#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

t1 = datetime.now().strftime('%H')
t2 = int(t1)

print(t2)



if 4 < t2 < 9:
	print("おはようございます")
elif 9 <= t2 < 18:
	print("こんにちは")	
elif 18 <= t2 < 23:
	print("こんばんは")	
elif 23 <= t2 <= 24:
	print("おやすみなさい")
elif 0 <= t2 <= 4:
	print("早く寝てください")


# 要件1：CGIスクリプトをPythonで書く
# 要件2：朝は「Good morning」など、現在の時間に従って挨拶を出力する
# 補足：Google App EngineのWebapp2(wsgi)を使っても構わない




