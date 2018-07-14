from tkinter import *

root = tk()

def click(str):
	return lambda: msg.set(str)
msg = StringVar()
msg.set("Howdy")
label = Label(root, textvariable = msg)
left = Button(root, text = 'Click me', command = click('Left!'))
right = Button(root, text = 'Click me', command = click('Right!'))

left.pack(side=LEFT, ipadx=5, ipady=5)
label.pack(side=LEFT, ipadx=5, ipady=5)
right.pack(side=LEFT, ipadx=5, ipady=5)

root.mainloop()

# 2行目の「Tk」をPython3にあわせて「tk」に書き換えた
# このプログラムを実行するとボタンが表示される(授業中に実演しているのをみた)
# UbuntuのCUI画面でもボタンが表示できるかどうかは不明
