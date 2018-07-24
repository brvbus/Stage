# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:09:30 2018

@author: L030909
"""
#import csv
#import os

import os, os.path
import win32com.client

import csv
import os

def RemplissageAuto():
    
    Data = open('test.txt','r')
    
    lines=Data.readlines()
    NameTxt=lines[1].replace('\n','')
    StrKey=lines[3]
    ListKey=StrKey.split(';')
    del ListKey[-1]
    
    #with File:  
    #   writer = csv.writer(File)
    #   writer.writerow(ListKey)
    
    DicoKey={}
    DicoKey['exact location']=''
    DicoKey['name']=NameTxt
    DicoKey['key1']=ListKey[0]
    DicoKey['key2']=ListKey[1]
    DicoKey['key3']=ListKey[2]
    print(DicoKey)
    
    ListKey.append(NameTxt)
    
    with open("testcsv1.csv","a", newline="") as File:
        CSVWriter = csv.writer(File)
        CSVWriter.writerow(ListKey)

RemplissageAuto()