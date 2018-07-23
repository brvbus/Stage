# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:07:15 2018

@author: faris
"""
from tkinter import *
import os
from  tkinter.tix import *
import fnmatch
import functools
import csv

class Application():
    
    def __init__(self):
        
### AFFICHAGE ###

        self.root = Tk()
        Label(self.root,text ="Capitalisation des outils SES").grid(sticky=N)
                            

        l=Label(self.root,width=80).grid(row=3)
        self.saisir=StringVar()
        self.entryBox=Entry(self.root,width=40)
        self.entryBox.grid(row=3,sticky=W)
        self.entryBox.insert(0,"Tapez votre recherche ici")
        self.entryBox1=Entry(self.root,width=40)
        self.entryBox1.grid(row=5,sticky=W)
        self.entryBox1.insert(0,"Tapez les mots-clés ici")
        self.grabBtn=Button(self.root, text="Recherche",command=self.grabText)
        self.grabBtn.grid(row=3,column=0,sticky=E)
        self.grabBtn1=Button(self.root, text="Recherche par mot-clé",command=self.RechercheMotCle)
        self.grabBtn1.grid(row=5,column=0,sticky=E)

#        self.entryBox.bind('<Return>', self.grabText)
# utiliser bind pour touche entrée!!!!!!             
      
### LISTE DEROULANTE###
      
         
        self.varcombo = StringVar()  
        self.combo = ComboBox(self.root, editable=0, dropdown=1, variable=self.varcombo)
        self.combo.grid(row=3,columnspan=1) 
        self.combo.entry.config(state='normal')  
        self.combo.insert(0, '.exe') 
        self.combo.insert(1, '.xlsx') 
        self.combo.insert(2, '.XLSM')
        self.combo.insert(3, '.txt') 
        self.combo.insert(4, '.json') 
        self.combo.insert(5, '.don')
        self.combo.insert(6, '.run')
        self.combo.insert(7, '.pt')
        self.combo.insert(8, '.bat')
        self.combo.insert(9, '.lnk')
        
        self.root.mainloop() 
        
### PROGRAMME CORRESPONDANCE ###
        
    def grabText(self):
            
        results=[]
        results1=[]
        
        self.retour=self.entryBox.get()
        self.extention=self.combo.entry.get()
        self.research=self.retour+self.extention
#        print(self.research)
        matches = []
        names=[]
        for root, dirnames, filenames in os.walk('X:/01_OUTILS/'):
            for filename in fnmatch.filter(filenames, ('*'+str(self.extention))):
                R=os.path.join(root, filename)
                matches.append(R)
                u=os.path.basename(R)
                names.append(u)
        
        self.root1 = Tk()
        self.root1.columnconfigure(0, weight=2)
              
        
        for i in range (len(names)):
            ligne=-1
            Ligne=[]
#            if self.research==names[i]:
#                os.startfile(str(matches[i]))
            if self.retour in names[i]:
                results.append(names[i])
                                
                for i in range(len(results)):
                    a=Label(self.root1,text=results[i])
                    a.grid(row=i+1,sticky=W)
    
        for i in range (len(matches)):
            
            
            if self.retour in matches[i]:
                results1.append(matches[i])
                ligne+=1
                Ligne.append(ligne)               
       
        def OpenFile(n):
                os.startfile(str(results1[n]))
        
        for n in range(len(Ligne)):

            Button(self.root1, text="Ouvrir",command=lambda n=n:(OpenFile(n))).grid(row=n+1,column=1,sticky=E)
        
#        print(len(Ligne))
        
        
### SCROLLBAR A CODER ###        
        
#        canv = Canvas(self.root1, width=600, height=400, scrollregion=(0, 0, 600, 600))
#        canv.grid(row=0, column=0)
#        
#        defilY = Scrollbar(self.root1, orient='vertical',command=canv.yview)
#        defilY.grid(row=0, column=10, sticky=NS)
#        
#        defilX = Scrollbar(self.root1, orient='horizontal', command=canv.xview)
#        defilX.grid(row=(len(Ligne)-1), column=0, sticky=EW)
#        
#        canv['xscrollcommand'] = defilX.set
#        canv['yscrollcommand'] = defilY.set
        
        self.root1.mainloop() 
        
### RECHERCHE PAR MOT-CLE ###
        
    def RechercheMotCle(self):

        self.root2 = Tk()
        self.root2.columnconfigure(0, weight=2)
        
        
        self.dico=[]
        self.f=open('X:/StageFSE/testcsv1.csv', 'r')
            
        lecteur= csv.DictReader(self.f,delimiter=";")
        for ligne in lecteur:
            global totalLines
            totalLines=lecteur.line_num
            for l in range (totalLines-1):
                self.dico.append(ligne)
            
        self.f.close()
        
        self.keyword_search=''
        
        global keyword_search
        self.keyword_search=self.entryBox1.get()
        self.Lkeyword_search=self.keyword_search.split()       
                
        keyresults=[]
        affresults=[]

        
        for y in range(len(self.Lkeyword_search)):
        
            for z in range (len(self.dico)):
                    
                if self.Lkeyword_search[y]==(self.dico[z]['key 1']):
                    keyresults.append(self.dico[z]['exact location'])
                    affresults.append(self.dico[z]['name'])
                    
                elif self.Lkeyword_search[y]==(self.dico[z]['key 2']):
                    affresults.append(self.dico[z]['name'])
                    keyresults.append(self.dico[z]['exact location'])

                    
                elif self.Lkeyword_search[y]==(self.dico[z]['key 3']):
                    affresults.append(self.dico[z]['name'])
                    keyresults.append(self.dico[z]['exact location'])
                    
                    
                elif self.Lkeyword_search[y]==(self.dico[z]['name']):
                    affresults.append(self.dico[z]['name'])
                    keyresults.append(self.dico[z]['exact location'])
                    
                    
#                else:
#                    print('non')
        
        def OpenFile(m):
            os.startfile(keyresults[m])

        list(set(affresults))

        for m in range(len(keyresults)-1):
            
            Button(self.root2, text="Ouvrir",command=lambda m=m:(OpenFile(m))).grid(row=m+1,column=1,sticky=E)
            a=Label(self.root2,text=affresults[m])
            a.grid(row=m+1,sticky=W)
            
        print(affresults)
    
#        print(results)
#        print(results1)

#        print(names)          
#        print(matches)
        
        self.root2.mainloop() 
        
    

Application()




        
 