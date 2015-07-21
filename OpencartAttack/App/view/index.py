#coding:utf-8
import os
from Tkinter import *

#TODO 文本框滑动条 frame布局
class Index(object):
    def __init__(self,initdir=None):
        self.top=Tk()
        self.top.title("Web Logic vulnerability")
        self.top.geometry('800x600')
        
        #标签的设置
        self.label=Label(self.top,text='这是一个空白的标签').grid(row=0)
        
        #进度条
        self.scale=Scale(self.top,
                         from_=0,to=100,
                         orient=HORIZONTAL,
                         )
        self.scale.set(12)
        self.scale.grid(row=0,column=1)

        #输入框的初始化和控制
        self.entryhingy=Entry(self.top)
        
        self.contents=StringVar()
        self.contents.set("the value of URL is")
        self.entryhingy.config(textvariable=self.contents)
        #设置文本框输入回车键的响应事件
        self.entryhingy.bind('<Key-Return>', self.print_message)
        self.entryhingy.grid(row=1  )
    
        self.quit=Button(self.top,
                         text="输入框的输入",
                         width=30,height=2,
                         borderwidth=0,
                         bg='green',
                         activebackground='red',
                         command=self.print_button_message
                         ).grid(row=1,column=1,columnspan=2)
    
        #文本框的初始化和控制
        self.text=Text()
        for i in range(1,10):
            self.text.insert(1.0,'hello\n')
        self.text.grid(row=2    )

        self.textInput=Button(self.top,
                              text="文本框的输入",
                              bg='green',
                              activebackground='red',
                              command=self.input_button_text
                              ).grid(row=2,column=1)
    
    def print_message(self,event):
        print('input the text-->',self.contents.get())
    
    def print_button_message(self):
        print('input the text-->',self.contents.get())
    
    def input_button_text(self):
        #光标的当前点
        self.text.insert(INSERT, ' 这是你光标的闪烁点  ')
        #鼠标的当前点
        self.text.insert(CURRENT,'这是你鼠标的位置')
        #文章的最后
        self.text.insert(END,'这是文章的最后')


def main():
    index=Index(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
    pass