from tkinter import *
import random

root = Tk()
cv = Canvas(root, width = 256, height = 256)
cv.pack()

for n in range(1000):
	x = random.random() * 256
	y = random.random() * 256
	cv.create_oval(x - 2, y - 2, x + 2, y + 2)

root.mainloop()

# 乱数の出力をグラフィカルに出力することができる。画面上で出力がランダムかどうかを直感的に確認できる。
# UbuntuのCUI画面で動かすことができるかどうかはふめい
# 授業ではMacのコマンドライン画面で実行していた
