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


print('random forest')

clf=RandomForestClassifier(n_estimators=100)
clf.fit(x_train,y_train)

print('Done...')









#print("Kết quả dự đoán :")
#print(y_pred)
#print("Kết quả thực tế:")
#print(np.array(y_test))












import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 550, height = 300)
canvas1.pack()


l1 = tk.Label(root, text ='Số rồng team xanh ăn')
canvas1.create_window(100, 10, window=l1)       #canvas1.create_window(x, y, window=l1)
entry1 = tk.Entry (root) 
canvas1.create_window(230, 10, window=entry1)

l2 = tk.Label(root, text ='Số rồng team đỏ ăn')
canvas1.create_window(100, 40, window=l2)
entry2 = tk.Entry (root) 
canvas1.create_window(230, 40, window=entry2)

l3 = tk.Label(root, text ='Số lần team xanh afk')
canvas1.create_window(100, 70, window=l3)
entry3 = tk.Entry (root) 
canvas1.create_window(230, 70, window=entry3)

l4 = tk.Label(root, text ='Số lần team đỏ afk')
canvas1.create_window(100, 100, window=l4)
entry4 = tk.Entry (root) 
canvas1.create_window(230, 100, window=entry4)

l5 = tk.Label(root, text ='chênh vàng topland')
canvas1.create_window(100, 130, window=l5)
entry5 = tk.Entry (root) 
canvas1.create_window(230, 130, window=entry5)

l6 = tk.Label(root, text ='chênh vàng jungland')
canvas1.create_window(100, 160, window=l6)
entry6 = tk.Entry (root) 
canvas1.create_window(230, 160, window=entry6)

l7 = tk.Label(root, text ='chênh vàng midland')
canvas1.create_window(100, 190, window=l7)
entry7 = tk.Entry (root) 
canvas1.create_window(230, 190, window=entry7)

l8 = tk.Label(root, text ='chênh vàng adc')
canvas1.create_window(100, 220, window=l8)
entry8 = tk.Entry (root) 
canvas1.create_window(230, 220, window=entry8)

l9 = tk.Label(root, text ='chênh vàng sp')
canvas1.create_window(100, 250, window=l9)
entry9 = tk.Entry (root) 
canvas1.create_window(230, 250, window=entry9)



def dudoanrd ():  
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
    
    gg = clf.predict(l1)[0]

    print('RandomForestClassifier')
    if gg==100:
        label1 = tk.Label(root, text='Đội xanh thắng')
        print('doi xanh thang')
    else:
        label1 = tk.Label(root, text='Đội   đỏ thắng')
        print('doi do thang')
    
    canvas1.create_window(310, 290, window=label1)
    
button1 = tk.Button(text='Dự đoán team thắng', command=dudoanrd)
canvas1.create_window(200, 290, window=button1)

root.mainloop()