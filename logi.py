from cProfile import label
from importlib.metadata import entry_points
import pandas as pd
import os
from skimage.transform import resize
from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter
from sklearn.model_selection import train_test_split
from tkinter import filedialog
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from tkinter import messagebox
from PIL import ImageTk, Image
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.utils import check_array



menu = pd.read_csv("archive/matches_800full.csv")


#print(menu)
#menu1 =[]
#menu1.append(menu.loc[:,'topGoldDiff'])
#menu1.append(menu.loc[:,'team1Top'])
#
#print(menu1)


menu1 = menu.loc[:,'winloss']
#print(menu1)



menu2 = menu.loc[:, ['t1Dragons','t2Dragons','t1Rift','t2Rift','topGoldDiff','jgGoldDiff','midGoldDiff','adcGoldDiff','suppGoldDiff']]
#print(menu2)

x_train,x_test,y_train,y_test=train_test_split(menu2,menu1,test_size=0.20,random_state=130,stratify=menu1)


print('LR')

x_trainn = x_train.values
x_testt = x_test.values

model = LogisticRegression()

model = model.fit(x_trainn, y_train)

print('done')






y_predsvm=model.predict(x_testt)

#print("Kết quả dự đoán :")
#print(y_pred)
#print("Kết quả thực tế:")
#print(np.array(y_test))
cxptsvm = accuracy_score(y_predsvm,y_test)*100

print(f"Độ chính xác: {accuracy_score(y_predsvm,y_test)*100}% ")




#print(gg)
#print(ff)

#l = [[1,0,1,0,4981,3913,131,-83,226]]
#gg = model.predict(l)[0]
#
#print('svm')
#if gg==100:
#    print('doi xanh thang')
#else:
#    print('doi do thang')










import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 550, height = 300)
canvas1.pack()


l1 = tk.Label(root, text ='Số rồng team xanh ăn')
canvas1.create_window(80, 10, window=l1)       #canvas1.create_window(x, y, window=l1)
entry1 = tk.Entry (root) 
canvas1.create_window(230, 10, window=entry1)

l2 = tk.Label(root, text ='Số rồng team đỏ ăn')
canvas1.create_window(80, 40, window=l2)
entry2 = tk.Entry (root) 
canvas1.create_window(230, 40, window=entry2)

l3 = tk.Label(root, text ='Số lần team xanh ăn sứ giả')
canvas1.create_window(80, 70, window=l3)
entry3 = tk.Entry (root) 
canvas1.create_window(230, 70, window=entry3)

l4 = tk.Label(root, text ='Số lần team đỏ ăn sứ giả')
canvas1.create_window(80, 100, window=l4)
entry4 = tk.Entry (root) 
canvas1.create_window(230, 100, window=entry4)

l5 = tk.Label(root, text ='chênh vàng topland')
canvas1.create_window(80, 130, window=l5)
entry5 = tk.Entry (root) 
canvas1.create_window(230, 130, window=entry5)

l6 = tk.Label(root, text ='chênh vàng jungland')
canvas1.create_window(80, 160, window=l6)
entry6 = tk.Entry (root) 
canvas1.create_window(230, 160, window=entry6)

l7 = tk.Label(root, text ='chênh vàng midland')
canvas1.create_window(80, 190, window=l7)
entry7 = tk.Entry (root) 
canvas1.create_window(230, 190, window=entry7)

l8 = tk.Label(root, text ='chênh vàng adc')
canvas1.create_window(80, 220, window=l8)
entry8 = tk.Entry (root) 
canvas1.create_window(230, 220, window=entry8)

l9 = tk.Label(root, text ='chênh vàng sp')
canvas1.create_window(80, 250, window=l9)
entry9 = tk.Entry (root) 
canvas1.create_window(230, 250, window=entry9)









def dudoan ():  
    if entry1.get() == '':
        x1 = 0
    else:
        x1 = entry1.get()
    if entry2.get() == '':
        x2 = 0
    else:
        x2 = entry2.get()
    if entry3.get() == '':
        x3 = 0
    else:
        x3 = entry3.get()
    if entry4.get() == '':
        x4 = 0
    else:
        x4 = entry4.get()
    if entry5.get() == '':
        x5 = 0
    else:
        x5 = entry5.get()
    if entry6.get() == '':
        x6 = 0
    else:
        x6 = entry6.get()
    if entry7.get() == '':
        x7 = 0
    else:
        x7 = entry7.get()
    if entry8.get() == '':
        x8 = 0
    else:
        x8 = entry8.get()
    if entry9.get() == '':
        x9 = 0
    else:
        x9 = entry9.get()
    


    l1 = [[x1,x2,x3,x4,x5,x6,x7,x8,x9]]

    gg = model.predict(l1)
    #ff = clf.predict(l1)[0]

    print('Logistic Regression.')
    if gg==100:
        label1 = tk.Label(root, text='Đội xanh thắng')
        print('doi xanh thang')
    else:
        label1 = tk.Label(root, text='Đội   đỏ thắng')
        print('doi do thang')
    l10 = tk.Label(root, text ='Theo Logistic Regression.')
    canvas1.create_window(400, 40, window=l10)
    canvas1.create_window(400, 70, window=label1)



    
    
button1 = tk.Button(text='Dự đoán team thắng', command=dudoan)
canvas1.create_window(200, 290, window=button1)

#button2 = tk.Button(text='Tỷ lệ chính xác', command=tylechinhxac)
#canvas1.create_window(400, 290, window=button2)





root.mainloop()
