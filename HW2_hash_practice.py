# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cxH8n9RaLeSOVwWsGU9dwzzHWFi4TpbP
"""

path = 'hw2_data.txt'
my_dict = {}                                                                    #創建dictionary
with open(path) as data:                                                        #讀寫檔案
  for voc in data.readlines():
    voc = voc.replace("\n", "")                                                 #把預設換行字元去除                   
    if voc not in my_dict:                                                      #當字彙不在dictionary裡，把字彙放入dictionary，並預設值1
      my_dict[voc] = 1
    else:                                                                       #反之把dictonary 中的值(次數)+1
      my_dict[voc] += 1

print("Different english words:", len(my_dict))                                 #印出有幾個不同單字
print(my_dict)                                                                  #印出dictionary，值=次數