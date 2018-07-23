# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:09:30 2018

@author: L030909
"""
#import csv
#import os
#
#f=open('test.txt','r')
#g=(open('testcsv1.csv','a'))
#
#def remplissageAuto():
#    L=[]
#        
#    for ligne in f:
#        w=f.readline()
#        print(w)
#        L.append(w)
#    
#    print(L)
#    
#remplissageAuto()
#
#    
#f.close()
#
#c=csv.writer(g)
#c.writerow(L)
#
#os.startfile('testcsv1.csv')

import os, os.path
import win32com.client

import csv
import os

tableau = [[1, 2, 3]]

with open("fichier.csv", "w") as f_write:
    writer = csv.writer(f_write)
    for row in tableau:
        writer.writerow(row)

if os.path.exists("delimiteur1.xlsm"):
    xl=win32com.client.Dispatch("Excel.Application")
    xl.Workbooks.Open(os.path.abspath("delimiteur1.xlsm"), ReadOnly=1)
    xl.Application.Run("delimiteur1.xlsm!delimiteur1")
##    xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
    xl.Application.Quit() # Comment this out if your excel script closes
    del xl

