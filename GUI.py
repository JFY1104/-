import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import glob
import cv2
import create_CAPTCHA
import main

def delete():
    # 將after_img中圖片刪除
    after_img.configure( image=None)
    after_img.update_idletasks
    before_img.configure( image=None)
    before_img.update_idletasks

def create():
    global img2
    # 取產生驗證碼圖片
    create_CAPTCHA.createImg()
    img2 = Image.open('test.png')
    img2 = ImageTk.PhotoImage( img2)

    # 投影出圖片
    before_img.configure( image=img2)

def result():
    global img3
    
    img3 = Image.open('test1.png')
    # img3 = main.img
    # img3 = Image.open(main.img)
    img3 = ImageTk.PhotoImage( img3)

    after_img.configure( image=img3)

def press_button():
    global img2,img3
    
    if parse_text.get() == '產圖':
        parse_text.set('解析')

        delete()

        # 建立驗證碼
        create()
    else:
        parse_text.set('產圖')

        # 產生解析驗證碼結果
        result()




# 建立主視窗
root = tk.Tk()
root.title('驗證碼解析')
root.geometry('210x250')
root.minsize( 210, 250)

# 建立圖片放置位置
before_img = tk.Label( root, text='解析前', font=('15'))
before_img.place( relx=0, rely=0.0, relheight=0.4, relwidth=1.0)
after_img = tk.Label( root, text='解析後', font=('15'))
after_img.place( relx=0, rely=0.4, relheight=0.4, relwidth=1.0)

# 建立解析驗證碼之按鈕
parse_text = tk.StringVar()
parse_text.set('產圖')
parse = tk.Button( root, textvariable=parse_text, padx=5, pady=5, font=('15'))
parse.config( command=press_button)
parse.place( relx=0.5, rely=0.9, anchor='center')

# 分割線
sep1 = ttk.Separator( root, orient='horizontal').place( rely=0.4, relwidth=1)
sep2 = ttk.Separator( root, orient='horizontal').place( rely=0.8, relwidth=1)

# tkinter執行
root.mainloop()

cv2.destroyAllWindows()