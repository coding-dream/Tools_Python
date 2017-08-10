#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import tkinter


def open():
    print('open a file')


def about():
    label = tkinter.Label(root, text='Limitless\n QQ:爱技术，爱分享！', fg='black', bg='white')
    label.pack(expand=tkinter.YES, fill=tkinter.BOTH)


root = tkinter.Tk()
menubar = tkinter.Menu(root)  # 菜单条

"""将tearoff设置为1以后，就是表明这个菜单是可以独立出来的 多出来一条线(意义不大)"""
fileMenu = tkinter.Menu(menubar, tearoff=0)  # 文件
aboutMenu = tkinter.Menu(menubar, tearoff=0)  # 关于

menubar.add_cascade(label='文件', menu=fileMenu)
menubar.add_cascade(label='关于', menu=aboutMenu)

fileMenu.add_command(label='打开', command=open)
fileMenu.add_command(label='保存')
fileMenu.add_separator()  # 添加分割线
fileMenu.add_command(label='退出', command=root.quit)

aboutMenu.add_command(label='关于作者', command=about)

root.config(menu=menubar)
root.geometry('500x500')
root.mainloop()
