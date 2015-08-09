#-*-coding:utf-8-*
import os
from Tkinter import *
import App.view
from App.view import getHtml
from App.view import get_URL

#TODO 文本框滑动条 frame布局
class Index(object):
    def __init__(self,initdir=None):
        self.top=Tk()
        self.top.title("Web Logic vulnerability")
        self.top.geometry('600x450')
        
        #标签的设置
        self.label=Label(self.top,text='这里输入一个URL').grid(row=0)
        
        #进度条
        self.scale=Scale(self.top,
                         from_=0,to=100,
                         orient=HORIZONTAL,
                         )
        self.scale.set(12)
        self.scale.grid(row=0,column=1)

        self.urlLabel=Label(self.top,text='这里输入一个URL').grid(row=1,sticky=E)
        #输入框的初始化和控制
        self.entrythingy=Entry(self.top)
        
        self.contents=StringVar()
        self.contents.set("http://www.freebuf.com/")
        self.entrythingy.config(textvariable=self.contents)
        #设置文本框输入回车键的响应事件
        self.entrythingy.bind('<Key-Return>', self.print_message)
        self.entrythingy.grid(row=1,column=1,sticky=W)
    
        self.quit=Button(self.top,
                         text="查看网页链接",
                         width=30,height=2,
                         borderwidth=0,
                         bg='green',
                         activebackground='red',
                         command=self.input_button_text
                         ).grid(row=1,column=2,columnspan=2)
    
        #文本框的初始化和控制
        self.text=Text()
        self.text.grid(row=2,columnspan=3)

        self.textInput=Button(self.top,
                              text="clean",
                              activebackground='red',
                              width=15,height=2,
                              command=self.clean
                              ).grid(row=3,column=2,sticky=E)
    
    def print_message(self,event):
        print('input the text-->',self.contents.get())
    
    def print_button_message(self):
        print('input the text-->',self.contents.get())
    
    def input_button_text(self):
        #光标的当前点
        #self.text.insert(INSERT, ' 这是你光标的闪烁点  ')
        #鼠标的当前点
        #self.text.insert(CURRENT,'这是你鼠标的位置')
        #文章的最后
        #self.text.insert(END,'这是文章的最后')
        #链接页面的url
        self.clean()
        for i in get_URL(getHtml(self.contents.get())):
            self.text.insert(END,i +"\n")

    def clean(self):
        self.text.delete(0.0, END)

def main():
    index=Index(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
    pass