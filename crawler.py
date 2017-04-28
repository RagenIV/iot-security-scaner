# -*- coding: utf_8 -*-

import re
import requests

def microcrawl(url, links, deep2):
	r = requests.get(url)
	if r.status_code == 200:
		con = r.text
		f = re.findall('"(http\:\/\/.*?)"',con)
		for lin in f:
			if not(lin in links):
				links.append(lin)
		f = re.findall('"(https\:\/\/.*?)"',con)
		for lin in f:
			if not(lin in links):
				links.append(lin)
		f = re.findall('"(\/.*?)"',con)
		for lin in f:
			if not((url + lin) in links):
				links.append(url + lin)
	return deep2 - 1

def crawl(url, deep):
	deep2 = deep
	comeover = 0 != 0
	f = re.findall('\/(.+?)\/',url)
	if len(f) > 0:
		root = f[0]
	else:
		if url.find('/') > -1:
			root = url[:url.find('/')]
		else:
			root = urt[:url.find('.')]
	links = []
	new = [url]
	newnew = []
	while 0 == 0:
		newnew = []
		for i in new:
			if root in i:
				if not(i in links):
					links.append(i)
					deep2 = microcrawl(i,newnew, deep2)
					if deep2 < 0:
						comeover = 0 == 0
						break
		if (len(newnew) == 0)or(comeover):
			break
		else:
			new = newnew
	return links
