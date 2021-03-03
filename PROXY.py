#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 02 13:26:46 2021

@author: acer
"""

class Data:
    def __init__(self,list):
        self.list = list
        
class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        obj_inst = self.instance
        new_inst_list = []
        print('Proxy..')
        for element in obj_inst.list:
            if type(element) == float:
                new_inst_list.append(element)
            else:
                new_inst_list.append(float(element))
        self.instance.list = new_inst_list
        print('Here you have it. :)')	
        

list_data = [0, 1, 2.5, 3, 4, 5]
obj_data = Data(list_data)
obj_proxy = Proxy(object_data)
obj_proxy.proxy()
print(obj_data.list)
print(obj_data.list)
