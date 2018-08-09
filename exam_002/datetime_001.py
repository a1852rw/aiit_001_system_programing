#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

print('Content-type: text/html; charset=UTF-8\r\n')

t1 = datetime.now().strftime('%H')
t2 = int(t1)

# print(t2)
# 動作確認用 不要なのでコメントアウトした

if 4 < t2 < 9:
	s1 = "おはようございます"
elif 9 <= t2 < 18:
	s1 = "こんにちは"	
elif 18 <= t2 < 23:
	s1 = "こんばんは"
elif 23 <= t2 <= 24:
	s1 = "おやすみなさい"
elif 0 <= t2 <= 4:
	s1 = "早く寝てください"

# print(s1)
# 動作確認用 不要なのでコメントアウトした

# 要件1：CGIスクリプトをPythonで書く
# 要件2：朝は「Good morning」など、現在の時間に従って挨拶を出力する
# 補足：Google App EngineのWebapp2(wsgi)を使っても構わない




