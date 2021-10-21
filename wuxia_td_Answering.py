#coding=utf-8
import time
import sys
from PIL import Image,ImageGrab
import os,win32gui, win32ui, win32con, win32api
import cv2
import requests
import re
import _tkinter
import tkinter
from tkinter import StringVar, IntVar
from tkinter import Tk, Checkbutton, Label,Text,Button,PhotoImage
from tkinter.messagebox import showinfo
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
import io
import base64
import config
from tiku import tk
from tiku import img
#from tkinter import  *
#以上为导入的python库




def get_file_content(filePath):   #读取截图方法
  with open(filePath, 'rb') as fp:
    return fp.read()


def window_capture():  #截图方法
 
  hwnd = win32gui.FindWindow("GEMAINWINDOWCLASS","天涯明月刀")
  hwndDC = win32gui.GetWindowDC(hwnd)      #从句柄获取全屏DC
  mfcDC=win32ui.CreateDCFromHandle(hwndDC)  #创建DC句柄
  saveDC=mfcDC.CreateCompatibleDC()        
  saveBitMap = win32ui.CreateBitmap()  #创建Bitmap图像
  MoniterDev=win32api.EnumDisplayMonitors(None,None) 
  w = MoniterDev[0][2][2] 
  h = MoniterDev[0][2][3] 
  #print w,h　　　#图片大小 
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)  
  saveDC.SelectObject(saveBitMap)  
  saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY) 
  #cc=time.gmtime() 
  bmpname='flush.bmp'    #设置截图名称
  saveBitMap.SaveBitmapFile(saveDC, bmpname) #保存Bitmap图像





def findtext(buttongj,ck): #初次匹配题库

  
   
    pth = "flush.bmp"
    image = cv2.imread(pth)     #读取截图

    if buttongj['state'] == 'disabled' and ck['state'] == 'normal': #国际版+全屏
        cropImg = image[310:333,135:242]  #裁剪截图
        cv2.imwrite("b.jpg",cropImg)   #保存裁剪
    elif buttongj['state'] == 'disabled' and ck['state'] == 'disabled': #国际版+窗口

        cropImg = image[300:323,135:242]  #裁剪截图
        cv2.imwrite("b.jpg",cropImg)   #保存裁剪

    elif buttongj['state'] == 'normal'and ck['state'] == 'normal' : #国服+全屏

        cropImg = image[276:296,135:242]  #裁剪截图
        cv2.imwrite("b.jpg",cropImg)   #保存裁剪
    elif buttongj['state'] == 'normal'and ck['state'] == 'disabled' :#国服+窗口
        cropImg = image[268:291,135:242]  #裁剪截图
        cv2.imwrite("b.jpg",cropImg)   #保存裁剪

    image = get_file_content("b.jpg") #打开裁剪

    try:
        txt = client.basicGeneral(image) #识别裁剪
        words_result = txt['words_result'] #读取识别
        words_result = words_result[0] #优化识别
        words = words_result['words']
        words = words.replace(",","，")  #优化识别
        words = words.replace(".","。")  #优化识别
        words = words.replace(":","：")  #优化识别
        for x in tk: #匹配识别
            searchObj = re.search(words,x)
            if searchObj!= None:
                return x  #匹配成功
            
    except: #识别异常处理
        return None 
  


def sb2(buttongj,ck): #二次匹配题库 同上
 

   
    pth = "flush.bmp"

    


    try:
        image = cv2.imread(pth) 

        if buttongj['state'] == 'disabled' and ck['state'] == 'normal': #国际版+全屏
            cropImg = image[310:333,180:250]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪
        elif buttongj['state'] == 'disabled' and ck['state'] == 'disabled': #国际版+窗口

            cropImg = image[300:323,180:250]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪

        elif buttongj['state'] == 'normal'and ck['state'] == 'normal' : #国服+全屏

            cropImg = image[276:296,180:250]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪
        elif buttongj['state'] == 'normal'and ck['state'] == 'disabled' :#国服+窗口
            cropImg = image[268:291,180:250]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪

        image = get_file_content("b.jpg")
        txt = client.basicGeneral(image)
        words_result = txt['words_result']
        words_result = words_result[0]
        words = words_result['words']
        words = words.replace(",","，")
        words = words.replace(".","。")
        words = words.replace(":","：")
        for x in tk:
            searchObj = re.search(words,x)
            if searchObj!= None:
                return x
    except:
        return None


def sb3(buttongj,ck): #三次匹配题库 同上
  
   
    pth = "flush.bmp"
    try:
        image = cv2.imread(pth) 



        


        if buttongj['state'] == 'disabled' and ck['state'] == 'normal': #国际版+全屏
            cropImg = image[310:333,230:280]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪
        elif buttongj['state'] == 'disabled' and ck['state'] == 'disabled': #国际版+窗口

            cropImg = image[300:323,230:280]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪

        elif buttongj['state'] == 'normal'and ck['state'] == 'normal' : #国服+全屏

            cropImg = image[276:296,230:280]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪
        elif buttongj['state'] == 'normal'and ck['state'] == 'disabled' :#国服+窗口
            cropImg = image[268:291,230:280]  #裁剪截图
            cv2.imwrite("b.jpg",cropImg)   #保存裁剪

        image = get_file_content("b.jpg")
        txt = client.basicGeneral(image)
        words_result = txt['words_result']
        words_result = words_result[0]
        words = words_result['words']
        words = words.replace(",","，")
        words = words.replace(".","。")
        words = words.replace(":","：")
        for x in tk:
            searchObj = re.search(words,x)
            if searchObj!= None:
                return x
    except:
        return None

        


    
   
def test(text,button,buttongj,ck):  #绑定按钮事件 校验密码
    
    r = requests.get('https://www.nekous.cn/td/tuzipass.psg') #利用request方法获得密码
    a = r.text
    if a == text :  #对比密码
        button.grid_forget()

        win.after(300,start(buttongj,ck))  #验证成功 进入功能方法
    else: #验证失败  显示提示
        text1.delete(0.0,tkinter.END)  
        text1.insert(tkinter.INSERT,"密码错误，请加群获取密码。")
        text1.update()

   

def start(buttongj,ck):
    
    window_capture()       #生成截图方法
    textx = findtext(buttongj,ck)     #识别文字方法

    if textx==None: #多重匹配
        textx=sb2(buttongj,ck)
    if textx==None:
        textx=sb3(buttongj,ck)
    if textx==None:
        textx="未匹配到" #匹配失败

    text1.delete(0.0,tkinter.END)
    text1.insert(tkinter.INSERT,textx) #显示匹配结果
    text1.update()

    win.after(500,start(buttongj,ck))  #递归调用自身 重复识别

def set_btn_gf(buttongf,buttongj):
    buttongf['state'] = 'disabled'
    buttongj['state'] = 'normal'
    

def set_btn_gj(buttongf,buttongj):
    buttongj['state'] = 'disabled'
    buttongf['state'] = 'normal'
    
def set_ck(qp,ck):
    ck['state'] = 'disabled'
    qp['state'] = 'normal'

def set_qp(qp,ck):
    qp['state'] = 'disabled'
    ck['state'] = 'normal'

def resize(w, h, w_box, h_box, pil_image):
    '''''
    resize a pil_image object so it will fit into
    a box of size w_box times h_box, but retain aspect ratio
    对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
    '''
 
    f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    # print(f1, f2, factor) # test
    # use best down-sizing filter
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)

def zanzhu():
    #showinfo(title = '赞助')
    imgurl= "https://www.nekous.cn/td/z.png"
    w_box = 800
    h_box = 300

    image_bytes = urlopen(imgurl).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    w, h = pil_image.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    tk_image = ImageTk.PhotoImage(image = pil_image)

    #photoopen = PhotoImage(file=pil_image)

    zan = tkinter.Toplevel()
    zan.title('赞助')
    tmp = open("tmp.ico","wb+")  
    tmp.write(base64.b64decode(img))
    tmp.close()
    zan.iconbitmap("tmp.ico") #设置图标
    os.remove("tmp.ico") 
    zan.attributes("-topmost",True)  #窗口优先级最高
    zan.geometry("700x320+500+300")  #窗口大小位置
    lab = tkinter.Label(zan,text="如果可以的话，请兔子喝一杯奶茶也喜欢呀~")
    lab.pack()
    
    label = tkinter.Label(zan, image=tk_image, width=w_box, height=h_box)

    label.pack(padx=5, pady=5)

    zan.mainloop()

def on_closing():
    try:
        os.remove("flush.bmp") 
    except:
        a=0
    try:
        os.remove("b.jpg") 
    except:
        a=0

    win.destroy()

if __name__ == '__main__':  #模拟主函数 从这里启动
    win = tkinter.Tk()  #创建tk窗口
    win.title('猫尾兔子 --帝王州美少女战士收人--群号：852074565')  #窗口标题
    win.attributes("-alpha",0.85)   #透明度30%
    win.geometry("520x135+120+90")  #窗口大小位置
    win.attributes("-topmost",True)  #窗口优先级最高
    tmp = open("tmp.ico","wb+")  
    tmp.write(base64.b64decode(img))
    tmp.close()
    win.iconbitmap("tmp.ico") #设置图标
    os.remove("tmp.ico") 
    #win.iconbitmap(pil_image)
    #fm = Frame(win)
    r = requests.get('https://www.nekous.cn/td/gonggao.psg') #利用request方法获得密码
    
    gg = tkinter.Label(win,text=r.text)
    gg.grid(column=0,row=0)
    text1 = tkinter.Text(win,width=50,height=3)  #初始化文本框
    text1.grid(column=0,row=1)
    
    buttongf=tkinter.Button(win,text="国服UI",state='normal',command=lambda:set_btn_gf(buttongf,buttongj))
    buttongf.grid(column=1,row=0)
    buttongj=tkinter.Button(win,text="国际UI",state='disabled',command=lambda:set_btn_gj(buttongf,buttongj))
    buttongj.grid(column=2,row=0)

    ck=tkinter.Button(win,text="窗口",state='normal',command=lambda:set_ck(qp,ck))
    ck.grid(column=1,row=1)
    qp=tkinter.Button(win,text="全屏",state='disabled',command=lambda:set_qp(qp,ck))
    qp.grid(column=2,row=1)


    zz=tkinter.Button(win,text="赞助",command=zanzhu)
    zz.grid(column=3,row=0)

    button=Button(win,text="验证",command = lambda:test(text1.get('0.0','end'),button,buttongj,ck))   #初始化校验密码按钮
    button.grid(column=3,row=1)
   

    win.protocol("WM_DELETE_WINDOW", on_closing)

    win.mainloop() #展示窗口 进入消息循环
 
  
