# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cxH8n9RaLeSOVwWsGU9dwzzHWFi4TpbP
"""

path = 'hw2_data.txt'
my_dict = {}
with open(path) as data:
  for voc in data.readlines():
    if voc not in my_dict:
      my_dict[voc] = 1
    else:
      my_dict[voc] += 1
print("Different english words:", len(my_dict))
print(my_dict)