#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Instagram username availablity checker.
# Coded by @4201337
# https://github.com/4201337
# ---------------------

from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock as LockPool
import requests
import time
import sys

myList = open('app.txt').readlines()
myThreads = 50
myLock = LockPool()
myPool = ThreadPool(myThreads)

def myRun(username):
	username = username.strip()
	url = 'https://www.instagram.com/'
	req = requests.get(url + username)
	if req.status_code == 200:
		with myLock:
			print("Unavailable") , username
		with open('Unavailable.txt', 'a') as Unavailable:
			Unavailable.write(username + '\n')
	elif req.status_code == 404:
		with myLock:
			print("Available") , username
		with open('Available.txt', 'a') as Available:
			Available.write(username + '\n')
	else:
		with myLock:
			print("Error") , username
		with open('Error.txt', 'a') as Error:
			Error.write(username + '|' + req.status_code + '\n')

startTime = time.time()

if __name__ == '__main__':
    myPool.map(myRun, myList)
    myPool.close()
    myPool.join()

endTime = time.time()

print("=============================")
print 'Done!'
print("=============================")
print("Total Time    :") , round(endTime - startTime, 2) , 'Seconds'
print("Total Threads :")  , myThreads
print("Total Tries   :")  , len(myList)
print("=============================")
print("Thank you for using Kitsune!")
print("=============================")
