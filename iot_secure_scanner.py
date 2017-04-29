# -*- coding: utf_8 -*-

import requests
from subprocess import Popen, PIPE
import random
import string
from urllib.parse import urlparse

import my_modules

import port_scaner
import requests_finder
import brute_post
import crawler


# import crawler

# Popen("ls -1", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split('\n')

def get_root(url):
	toor = urlparse(url)
	if toor.netloc.find(':') == -1:
		root = toor.netloc
	else:
		root = toor.netloc[:toor.netloc.find(':')]
	return root

def gen_pass(length):
	ans = ''
	for i in range(length):
		ans += random.choice('!@#$%&*?^' + string.digits + string.ascii_letters)
	return ans
	
def send_mail(adr, rep):
	ans = ''
	for i in rep:
		ans += i + '\r\n___________\r\n'
	r = requests.get('http://scanner.juwilie.pw/sendMail.php?email=' + adr + '&text=' + ans)


def gogogo(dic):
	# r = requests.get('http://scanner.juwilie.pw/sendMail.php?email=19nick98@gmail.com&text='+dic['email']+'\r\n'+dic['host']+'\r\n'+str(dic['adv']))
	report = []
	
	report.append('Scanned device is ' + dic['host'])
	root = get_root(dic['host'])
	if dic['adv'] == '0':
		po = port_scaner.scanit(root,[22,23,25,80,443,1111,1234,3389,8000,8080,8888,9001])
		if len(po) > 0:
			report.append('Take care about these ports (they are open):\r\n'+'\r\n'.join(map(str, po)))
		webs = crawler.crawl(str(dic['host']), 5)
		for lin in webs:
			rrr = requests_finder.findit(lin)
			for r in rrr:
				if r[1] == 'post':
					print('epta')
					logfi = 'etoneLoGin444'
					pwdfi = 'eT0HEpassword'
					for i in ans[2:]:
						if (i.lower().find('login') != -1):
							logfi = i
							break
					for i in ans[2:]:
						if (i.lower().find('pass') != -1)or(i.loser().find('pwd') != -1):
							pwdfi = i
							break
					if (logfi != 'etoneLoGin444')and(pwdfi != 'eT0HEpassword'):
						pwd = brute_post.brute(lin, logfi, pwdfi)
						if len(pwd) == 2:
							report.append("DANGER: your password isn't strong at all!!!\r\nSolution: change %s's password to more secure\r\nYou can use this: %s (generated automaticaly by random)" % (pwd[1], gen_pass(21)))
	else:
		report.append('Scan was wide')
		po = port_scaner.scanit(root,[i for i in range(1235)] + [3389,7777,8000,8080,8888,9001])
		if len(po) > 0:
			report.append('Take care about these ports (they are open):\r\n'+'\r\n'.join(map(str, po)))
		webs = crawler.crawl(str(dic['host']), 13)
		
		for lin in webs:
			rrr = requests_finder.findit(lin)
			for r in rrr:
				if r[1] == 'post':
					print('epta')
					logfi = 'etoneLoGin444'
					pwdfi = 'eT0HEpassword'
					for i in ans[2:]:
						if (i.lower().find('login') != -1):
							logfi = i
							break
					for i in ans[2:]:
						if (i.lower().find('pass') != -1)or(i.loser().find('pwd') != -1):
							pwdfi = i
							break
					if (logfi != 'etoneLoGin444')and(pwdfi != 'eT0HEpassword'):
						pwd = brute_post.brute(lin, logfi, pwdfi)
						if len(pwd) == 2:
							report.append("DANGER: your password isn't strong at all!!!\r\nSolution: change %s's password to more secure\r\nYou can use this: %s (generated automaticaly by random)" % (pwd[1], gen_pass(21)))
				elif r[1] == 'noget':
					pass
				else:
					pass
					# scan for get
			
			
	try:
		send_mail(dic['email'], report)
		print('success')
	except:
		print('fiasco')

