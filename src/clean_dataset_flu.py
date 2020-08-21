# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:21:10 2019

@author: Li Xiang

clean dataset of PHM2017 and FLU 2013, for better doing machine learning task afterwards

uncomment the last lines if want to generate new flu dataset

"""

import pandas as pd 
import numpy as np
import os 

flu_old_fpath='../data/flu_annotations/'
flu_tweet_fpath='../data/tweets_flu/'


#-------------------------deal with flu dataset-------------------------------
flu_aware2009_df=pd.read_csv(flu_old_fpath+'AwarenessVsInfection2009TweetIDs.txt',header=None,sep='\t')
flu_aware2012_df=pd.read_csv(flu_old_fpath+'AwarenessVsInfection2012TweetIDs.txt',header=None,sep='\t')
flu_relate2009_df=pd.read_csv(flu_old_fpath+'RelatedVsNotRelated2009TweetIDs.txt',header=None,sep='\t')
flu_relate2012_df=pd.read_csv(flu_old_fpath+'RelatedVsNotRelated2012TweetIDs.txt',header=None,sep='\t')
flu_self2009_df=pd.read_csv(flu_old_fpath+'SelfVsOthers2009TweetIDs.txt',header=None,sep='\t')
flu_self2012_df=pd.read_csv(flu_old_fpath+'SelfVsOthers2012TweetIDs.txt',header=None,sep='\t')

flu_aware2009_ids=flu_aware2009_df[0].tolist()
flu_aware2012_ids=flu_aware2012_df[0].tolist()
flu_relate2009_ids=flu_relate2009_df[0].tolist()
flu_relate2012_ids=flu_relate2012_df[0].tolist()
flu_self2009_ids=flu_self2009_df[0].tolist()
flu_self2012_ids=flu_self2012_df[0].tolist()


flu_aware2009_lst=[]
flu_aware2012_lst=[]
flu_relate2009_lst=[]
flu_relate2012_lst=[]
flu_self2009_lst=[]
flu_self2012_lst=[]


l=len(os.listdir(flu_tweet_fpath))
file_lst=os.listdir(flu_tweet_fpath)

for t_id in flu_aware2009_ids:
    if(str(t_id)+'.csv' in file_lst):
        df=pd.read_csv(flu_tweet_fpath+str(t_id)+'.csv')
        twt=df.tweet.tolist()[0]
        flu_aware2009_lst.append([str(t_id),twt,flu_aware2009_df.loc[flu_aware2009_df[0]==t_id,1].values[0]])
 
for t_id in flu_aware2012_ids:
    if(str(t_id)+'.csv' in file_lst):
        df=pd.read_csv(flu_tweet_fpath+str(t_id)+'.csv')
        twt=df.tweet.tolist()[0]
        flu_aware2012_lst.append([str(t_id),twt,flu_aware2012_df.loc[flu_aware2012_df[0]==t_id,1].values[0]])
 
for t_id in flu_relate2009_ids:
    if(str(t_id)+'.csv' in file_lst):
        df=pd.read_csv(flu_tweet_fpath+str(t_id)+'.csv')
        twt=df.tweet.tolist()[0]
        flu_relate2009_lst.append([str(t_id),twt,flu_relate2009_df.loc[flu_relate2009_df[0]==t_id,1].values[0]])
 
for t_id in flu_relate2012_ids:
    if(str(t_id)+'.csv' in file_lst):
        df=pd.read_csv(flu_tweet_fpath+str(t_id)+'.csv')
        twt=df.tweet.tolist()[0]
        flu_relate2012_lst.append([str(t_id),twt,flu_relate2012_df.loc[flu_relate2012_df[0]==t_id,1].values[0]])
 
for t_id in flu_self2009_ids:
    if(str(t_id)+'.csv' in file_lst):
        df=pd.read_csv(flu_tweet_fpath+str(t_id)+'.csv')
        twt=df.tweet.tolist()[0]
        flu_self2009_lst.append([str(t_id),twt,flu_self2009_df.loc[flu_self2009_df[0]==t_id,1].values[0]])
 
for t_id in flu_self2012_ids:
    if(str(t_id)+'.csv' in file_lst):
        df=pd.read_csv(flu_tweet_fpath+str(t_id)+'.csv')
        twt=df.tweet.tolist()[0]
        flu_self2012_lst.append([str(t_id),twt,flu_self2012_df.loc[flu_self2012_df[0]==t_id,1].values[0]])
        

#--------------uncomment the below lines if want to generate files-------


#flu_aware2009_new_df=pd.DataFrame(flu_aware2009_lst,columns=['id','tweet','label'])
#flu_aware2009_new_df.to_csv('../clean_data/flu/AwarenessVsInfection2009.csv',index=False)
#
#flu_aware2012_new_df=pd.DataFrame(flu_aware2012_lst,columns=['id','tweet','label'])
#flu_aware2012_new_df.to_csv('../clean_data/flu/AwarenessVsInfection2012.csv',index=False)
#
#flu_relate2009_new_df=pd.DataFrame(flu_relate2009_lst,columns=['id','tweet','label'])
#flu_relate2009_new_df.to_csv('../clean_data/flu/RelatedVsNotRelated2009.csv',index=False)
#
#flu_relate2012_new_df=pd.DataFrame(flu_relate2012_lst,columns=['id','tweet','label'])
#flu_relate2012_new_df.to_csv('../clean_data/flu/RelatedVsNotRelated2012.csv',index=False)
#
#flu_self2009_new_df=pd.DataFrame(flu_self2009_lst,columns=['id','tweet','label'])
#flu_self2009_new_df.to_csv('../clean_data/flu/SelfVsOthers2009.csv',index=False)
#
#flu_self2012_new_df=pd.DataFrame(flu_self2012_lst,columns=['id','tweet','label'])
#flu_self2012_new_df.to_csv('../clean_data/flu/SelfVsOthers2012.csv',index=False)












