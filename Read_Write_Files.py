#txt====================================

##開啟 or 創建 & 寫入字串============================
string='Happy Birthday'
txt_w=open("test.txt",'w')    #開啟text.txt文字檔為寫入模式，並記錄在txt_w中，若沒有此檔案，則會新增一個
txt_w.write(string)   #將string寫入文字檔中
txt_w.close() #關閉文字檔

"""另有一種寫法
with open("test.txt",'w') as txt_W:
    txt_w.write(string)

此寫法在跳出with後即會關閉檔案，故無需 txt_w.close() 
"""
##讀取文字檔內容===============================
txt_r=open("test.txt",'r') #打開text.txt檔案為讀取模式，並記錄於txt_r
string_r=txt_r.read() #讀取file的內容進string_r
txt_r.close()    #讀取完後關閉檔案


#npy====================================
import numpy as np
##創建 & 寫入============================
prime=[2,3,5,7,9,11,13]
np.save("PrimeSequence",prime)  #將prime list 存入新建的 PrimeSequence.npy檔中

##讀取===================================
npy_r=np.load("PrimeSequence.npy")  #讀取PrimeSequence.npy內容進npy_r

"""npy檔內資料為numpy 內ndarray型別，
基本上npy檔用來存一筆資料，即一個list or np.array的資料
"""


#pickle=========================================
import pickle
#pickle=================================
li=[[i**2 for i in range(3)] for j in range(5)]

p_w=open("pick.pickle",'wb')    #新建或開啟 pickle檔案為寫入模式，紀錄於p_w
pickle.dump(li,p_w) #將li 寫入p_w
p_w.close() #關閉

p_r=open("pick.pickle",'rb')    #開啟 pickle檔案為讀取模式，紀錄於p_r
lis=pickle.load(p_r)    #讀取p_r之內容
p_r.close() #關閉

"""pickle檔內可將資料以原始型別儲存
"""

"""另有with寫法，與txt類似
with open("newList.pickle",'wb') as file:
    pickle.dump(lis,file)
"""