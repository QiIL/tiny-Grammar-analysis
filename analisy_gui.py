# -*- coding: UTF-8 -*-
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
from tiny_analisis import TAS
from tree import tree_list

#读取tiny文件
def readFile():
    root = Tk()
    root.filename = tkFileDialog.askopenfilename(title = "选择一个.tiny文件",filetypes = (("Tiny file","*.tny"),("all files","*.*")))
    f = open(root.filename, 'r')
    text_box.delete(1.0, END)
    text_box.insert(END, f.read())

def show_text():
    input = text_box.get(1.0, END)
    anatree = TAS(input)
    message_box.delete(1.0, END)
    if anatree.output():
        for i in tree_list:
            message_box.insert(END, i+'\n')
    else:
        message_box.insert(END, anatree.error_message[0])

root = Tk()
menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=readFile)
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

text_box = Text(root, width=80, height=15)
text_box.pack()

ana_button = Button(root, text='analisy', command=show_text)
ana_button.pack()

message_box = Text(root, width=80)
message_box.pack()

root.mainloop()