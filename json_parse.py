#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import requests
import json
import time

import my_modules

import port_scaner
import requests_finder
import brute_post
import crawler


import iot_secure_scanner

def get_json():
	flag = 0 == 0
	r = requests.get('http://scanner.juwilie.pw/getRequest.php')
	if r.status_code == 200:
		try:
			dic = json.loads(r.text)
			print(dic)
			for i in dic:
				if dic[i] == None:
					flag = 0 != 0
			if flag:
				print('gogogo')
				iot_secure_scanner.gogogo(dic)
		except:
			pass
	else:
		print("Server not reposining: ", r.status_code)

while 0 == 0:
	time.sleep(10)
	get_json()
