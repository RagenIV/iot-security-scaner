# -*- coding: utf_8 -*-

import socket

# host - строка
# ports - список
def scanit(host='127.0.0.1', ports=[80]):
	host = str(host)
	open_port = []
	
	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.01)
		try:
			sock.connect((host, port))
			open_port.append(port)
		except:
			pass
		sock.close()
	
	return open_port
