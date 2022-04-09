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


print('SVM')
model=svm.SVC(probability=True)
print('Model is training..............')
model.fit(x_train,y_train)
print('Done!!!\n')

clf=RandomForestClassifier(n_estimators=100)
clf.fit(x_train,y_train)







y_predsvm=model.predict(x_test)
y_predrd=clf.predict(x_test)
#print("Kết quả dự đoán :")
#print(y_pred)
#print("Kết quả thực tế:")
#print(np.array(y_test))
cxptsvm = accuracy_score(y_predsvm,y_test)*100
cxptrd = accuracy_score(y_predrd,y_test)*100
print(f"Độ chính xác: {accuracy_score(y_predsvm,y_test)*100}% ")
print(f"Độ chính xác: {accuracy_score(y_predrd,y_test)*100}% ")



#print(gg)
#print(ff)

l = [[1,0,1,0,4981,3913,131,-83,226]]
gg = model.predict(l)[0]
ff = clf.predict(l)[0]
print('svm')
if gg==100:
    print('doi xanh thang')
else:
    print('doi do thang')

print('random')
if ff==100:
    print('doi xanh thang')
else:
    print('doi do thang')





