# -*- coding: utf_8 -*-

import re
import requests

def findit(url):
	try:
		r = requests.get(url)
		ans = [] # ans[i][0] == <URL>; ans[i][1] == 'get' or 'post'; дальше параметры  
		if r.status_code == 200:
			con = r.text
			for form in re.findall('\<form.*\<\/form\>', con, re.DOTALL):
				loc_action = re.findall('action="(.*?)"', form)
				if len(loc_action) == 0:
					continue # если ссылки не найдены
				else:
					ans.append([url + loc_action[0]])
					if len(re.findall('method="post"', form)) > 0:
						# если post-запрос
						ans[len(ans) - 1].append('post')
						fields = re.findall('name="(.*?)"', form)
						ans[len(ans) - 1].append(fields[1:])
					else:
						ans[len(ans) - 1].append('get')
	except:
		ans = [[url, 'noget']]
	return ans

# test: print(findit('http://172.0.6.238/login.rsp'))
# print(findit('https://94.237.35.76:8443/spb/setup.do'))
