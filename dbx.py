#!/usr/bin/python3

import dropbox
import datetime
import os

try:
	accessToken = os.environ['AMAZON_SPIDER_ACCESSTOKEN']
except KeyError:
	print("Environment variable not found: AMAZON_SPIDER_ACCESSTOKEN")
	exit()
	
dbox = dropbox.Dropbox(accessToken)
filename = '/files/' + datetime.datetime.now().strftime("%Y-%b-%d").upper() + '.csv'
with open('output.csv', 'r') as myfile:
    data=myfile.read()
dbox.files_upload(bytes(data,'utf-8'), filename)
