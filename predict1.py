import operator
import re
import csv
import pandas as pd
import numpy as np
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt




def fun():
    df = pd.read_excel('./dataset/raw_data.xlsx')
    data = df.fillna(method='ffill')
    list(data)
    def process_data(data):
        data_list = []
        data_name = data.replace('^','_').split('_')
        n = 1
        for names in data_name:
            if (n % 2 == 0):
                data_list.append(names)
            n += 1
        return data_list
    disease_list = []
    disease_symptom_dict = defaultdict(list)
    disease_symptom_count = {}
    count = 0
    for idx, row in data.iterrows():
        if (row['Disease'] !="\xc2\xa0") and (row['Disease'] != ""):
            disease = row['Disease']
            disease_list = process_data(data=disease)
        if (row['Symptom'] !="\xc2\xa0") and (row['Symptom'] != ""):
            symptom = row['Symptom']
            symptom_list = process_data(data=symptom)
            for d in disease_list:
                for s in symptom_list:
                    disease_symptom_dict[d].append(s)
                disease_symptom_count[d] = count

    df1 = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease','Symptom'])  





    baddict={}

    for x in disease_symptom_dict.keys():
    
                baddict[x]=0
            

    

    for i in range(100):
        print("*************** enter the symptoms or enter OK for results ******************")
        a=input()
        if(a=='OK'):
            break
        else:
            for x in disease_symptom_dict.keys():
                for y in disease_symptom_dict[x]:
                    if(y==a):
                    
                        baddict[x]=baddict[x]+1

        

        
        
    l=[key for m in [max(baddict.values())] for key,val in baddict.items() if val == m]
    print("expected disease(s) are :\n")
    for i in range(len(l)):
        print(l[i])
    
 



    diff=[]

    if(len(l)>1):
        for i in range(len(l)):
            for x in disease_symptom_dict.keys():
                if(x==l[i]):
                    for y in disease_symptom_dict[x]:
                        if y in diff:
                            diff.remove(y)
                        if y not in diff:
                            diff.append(y)
                
                

    if(len(l)>1):
        print("\n********* for more accurate results give Symptoms from following *******\n")

        for i in range(len(diff)):
            print(diff[i])
    
    
  
        for i in range(100):
            print("*************** Enter the symptoms from ABOVE or Enter 'OK' for results ******************")
            a=input()
            if(a=='OK'):
                break
            else:
                for x in disease_symptom_dict.keys():
                    for y in disease_symptom_dict[x]:
                        if(y==a):
                        
                            baddict[x]=baddict[x]+1
            
            
            
            
            

    if(len(l)>1):
        l=[key for m in [max(baddict.values())] for key,val in baddict.items() if val == m]
        print("Most expected disease are :\n")
        for i in range(len(l)):
            print(l[i])
fun()    
 


