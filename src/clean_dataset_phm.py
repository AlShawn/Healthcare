# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:22:08 2019

@author: Li Xiang

uncomment last line to_csv
"""


import pandas as pd 
import numpy as np
import os 

#    for the PHM2017 dataset
fpath='../data/PHM2017/PHM2017.txt'
PHM2017_df = pd.read_csv(fpath, delimiter = "\t",names=['twitter_id','symptom','label'])

tid_map_symptom=pd.Series(PHM2017_df.symptom.values,index=PHM2017_df.twitter_id).to_dict()
tid_map_label=pd.Series(PHM2017_df.label.values,index=PHM2017_df.twitter_id).to_dict()

#-----------------write tweets into new dataframe------------------------------
new_tweet_symptom_label_dataset=[]
fpath='../data/tweets_PHM2017/'
l=len(os.listdir(fpath))
for i,file in enumerate(os.listdir(fpath)):
    if(file[-4:]!='.csv'):
        continue
    tid=int(file[:-4])
    dataset=pd.read_csv(fpath+file)
    for t in dataset['tweet'][dataset.tweet.notnull()].tolist():
        if(tid_map_symptom[tid].lower() in t.lower()):
            sample=[tid,t,tid_map_symptom[tid],tid_map_label[tid]]
            new_tweet_symptom_label_dataset.append(sample)
            break
    if(i%100==0):
        print(i,'/',l)        
        
#new_df=pd.DataFrame(new_tweet_symptom_label_dataset,columns=['id','tweet','symptom','label'])
#new_df.to_csv('../clean_data/PHM2017/PHM2017.csv',index=False)

read_df=pd.read_csv('../clean_data/PHM2017/PHM2017.csv')