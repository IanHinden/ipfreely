import pyping, socket, ipaddress

myip = socket.gethostbyname(socket.gethostname())

network = ipaddress.IPv4Network(myip , strict=False)

for x in network:
	response = typing.ping(myip)
	if response.ret_code == 0:
		print "%d is up" % (x)
	else:
		print "%d is down" % (x)