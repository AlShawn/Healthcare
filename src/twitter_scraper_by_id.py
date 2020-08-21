# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:32:25 2019

@author: Li Xiang

scrape the twitter info by twitter id

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import os  
import time 
import pandas as pd
import sys
import random

def TwitterScraper(twitter_id):
    

    path2=os.path.abspath('..')
    ex_path=path2+'/driver/geckodriver.exe'
    options = Options()
    options.headless = True
#    options.binary_location = "/usr/bin/firefox"
    driver = webdriver.Firefox(firefox_options=options, executable_path=ex_path)
#    driver = webdriver.Firefox(executable_path=ex_path)
    user_id=random.randint(0,sys.maxsize)
    url='https://twitter.com/'+str(user_id)+'/status/'+str(twitter_id)
    
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'js-tweet-text-container')))
#    if the twitter don't exist
    except TimeoutException:
        with open('../data/tweets_flu/suspended_id.txt','a') as f:
            f.write('{}\n'.format(twitter_id))
        print(twitter_id, ' suspended!')
        driver.quit()
        return 

    twitter_class_name='js-tweet-text-container'
    try:
        tweet_text=driver.find_elements_by_class_name(twitter_class_name)
        tweet_text_1=driver.find_elements_by_class_name(twitter_class_name)[0]
    except IndexError:
        print("index error")
    else:
        tweets=[]
#        print('tweet number:{}'.format(len(tweet_text)))
        for t in tweet_text:
#            print('tweet text:{}'.format(t.text))
            tweets.append(t.text)
        df = pd.DataFrame(tweets, columns = ['tweet'])
        df.to_csv('../data/tweets_flu/'+str(twitter_id)+'.csv',index=False)
        
    time.sleep(5)
    driver.quit()
    return

if(__name__=='__main__'):
    
#    for the PHM2017 dataset
#    fpath='../data/PHM2017.txt'
#    df = pd.read_csv(fpath, delimiter = "\t",names=['twitter_id','symptom','label'])

#    for the flu dataset
#---------------write the useful ids in the txt file
#    fdir='../data/flu_annotations/'
#    unique_twitter_ids=[]
#    for file in os.listdir(fdir):
#        if(file.endswith('.txt')):
#            df = pd.read_csv(fdir+file, delimiter = "\t",names=['twitter_id','label'])
#            unique_twitter_ids.extend(df['twitter_id'].tolist())
#    unique_twitter_ids_1=list(set(unique_twitter_ids))
#    
#    with open(fdir+'all_tweet_id.txt','w') as f:
#        for id_ in unique_twitter_ids:
#            f.write('{}\n'.format(id_))
# ---------read the useful ids from the txt file
    fdir='../data/flu_annotations/'
    fpath=fdir+'all_tweet_id.txt'
#    unique_twitter_ids
    with open(fpath,'r') as f:
        unique_twitter_ids=f.readlines()
    unique_twitter_ids=[int(id_.rstrip('\n')) for id_ in unique_twitter_ids]   
        
#--------for scraping 
    flag=0
    for i,t_id in enumerate(unique_twitter_ids[flag:]):
        i+=flag
        TwitterScraper(t_id)
        print('{}/{}'.format(i,len(unique_twitter_ids)))
        










