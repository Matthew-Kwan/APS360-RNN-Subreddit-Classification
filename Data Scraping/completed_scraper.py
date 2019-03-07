# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:47:54 2019

@author: linda
"""

import csv
import praw 
#initialize csv
f = open('redditdata1.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['id','subreddit','titles','post','score','url'])
data = {}

#create request
reddit = praw.Reddit(client_id='4-rymST_4DmH0Q',
                     client_secret="NOvMOy9faobYCfP2r6LQbUcn_wM", password='12345ABCabc!',
                     user_agent='a', username='aps360')

#change this to desired subreddit
subreddit = reddit.subreddit('history')
count = 0 

for submission in subreddit.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])

subreddit2 = reddit.subreddit('Showerthoughts')

for submission in subreddit2.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit2
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])
    
subreddit3 = reddit.subreddit('AskEurope')

for submission in subreddit3.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit3
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])

subreddit4 = reddit.subreddit('Jokes')

for submission in subreddit4.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit4
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])
    
subreddit5 = reddit.subreddit('AskMen')

for submission in subreddit5.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit5
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])

subreddit6 = reddit.subreddit('books')

for submission in subreddit6.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit6
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])
    
subreddit7 = reddit.subreddit('legaladvice')

for submission in subreddit7.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit7
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])

subreddit8 = reddit.subreddit('personalfinance')

for submission in subreddit8.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit8
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)

    
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])

subreddit9 = reddit.subreddit('personalfinancecanada')

for submission in subreddit9.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit9
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])

subreddit10 = reddit.subreddit('LifeProTips')

for submission in subreddit10.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit10
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])
    
subreddit11 = reddit.subreddit('TwoXChromosomes')

for submission in subreddit11.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit11
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])

subreddit12 = reddit.subreddit('Relationships')

for submission in subreddit12.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit12
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])
subreddit13 = reddit.subreddit('TalesFromRetail')

for submission in subreddit13.top(time_filter='all',limit=1000):
    count = count + 1
    data['id'] = count
    data['subreddit'] = subreddit13
    data['titles'] = (submission.title).encode('utf-8')  # Output: the submission's title
    data['post'] = (submission.selftext).encode('utf-8')
    data['score'] = submission.score
    data['url'] = submission.url
    
    #for debugging purposes 
    print(count)
    #write out the rest of the rows
    writer.writerow([data['id'],data['subreddit'], data['titles'],data['post'],data['score'],data['url']])


