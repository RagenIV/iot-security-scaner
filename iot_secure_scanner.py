# -*- coding: utf_8 -*-

import requests
from subprocess import Popen, PIPE
import random
import string

import my_modules

import port_scaner
import requests_finder
import brute_post
import crawler


# import crawler

# Popen("ls -1", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split('\n')


def gen_pass(length):
	ans = ''
	for i in range(length):
		ans += random.choice('!@#$%&*?^' + string.digits + string.ascii_letters)
	return ans
	
def send_mail(adr, rep):
	ans = ''
	for i in rep:
		ans += i.replace('\n','\r\n') + '\r\n___________\r\n'
	r = requests.get('http://scanner.juwilie.pw/sendMail.php?email=' + adr + '&text=' + ans')
	print(ans)

def gogogo(dic):
	r = requests.get('http://scanner.juwilie.pw/sendMail.php?email=19nick98@gmail.com&text='+dic['email']+'\r\n'+dic['host']+'\r\n'+str(dic['adv']))
	report = []
	
	report.append('Scanned device is ' + dic['host'])

	if dic['adv'] == '0':
		'''
		print('first_start')
		report.append('Scan was intensive')
		print('f1')
		print(dic['host'])
		webs = crawler.crawl(dic['host'], 13)
		print('f2')
		for lin in webs:
			rrr = requests_finder.findit(lin)
			for r in rrr:
				if ans[1] == 'post':
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
		'''
		pass
	else:
		report.append('Scan was wide')
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
		print('second_finish')
	print('4321')
	send_mail(dic['email'], report)
	
