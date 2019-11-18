# -*- coding:utf-8 -*-
 
from Tkinter import * # python 3 是tkinter
import tkMessageBox
import requests
import re
from PIL import Image
 
 
def download():
  start_url = 'http://www.uustv.com/'
  name = entry.get().encode('utf-8')
  if not name:
    tkMessageBox.showinfo('提示', '请输入姓名再设计！')
    return
  data = {
    'word': name,
    'sizes': '60',
    'fonts': 'jfcs.ttf',
    'fontcolor': '#000000'
  }
  result = requests.post(start_url, data=data).content
  reg = '<div class="tu">﻿<img src="(.*?)"/></div>'
  img_url = start_url + re.findall(reg, result)[0]
  response = requests.get(img_url).content
  # 将生成的签名图片下载到本地
  with open('{}.gif'.format(name.decode('utf-8').encode('gbk')), 'wb') as f:
    f.write(response)
  try:
    im = Image.open('{}.gif'.format(name.decode('utf-8').encode('gbk')))
    im.show()
  except:
    print '自己打开看吧'
 
 
root = Tk()
root.title('个性签名设计')
root.geometry('+800+300') # 设置窗口出现在屏幕上面的位置
Label(root, text='姓名', font=('微软雅黑', 15)).grid() # 布局方法不要混用
entry = Entry(root, font=('微软雅黑', 15))
entry.grid(row=0, column=1)
button = Button(root, text='设计签名', font=('微软雅黑', 15), width='15', height=1, command=download)
button.grid(row=1, column=1)
root.mainloop()

