import pyping, socket, ipaddress, struct

myip = socket.gethostbyname(socket.gethostname())

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

i = findnth(myip, ".", 2)

subnetMask = myip[:i-1] + "0.0/16"
uMySubnet = unicode(subnetMask, "utf-8")

network = ipaddress.IPv4Network(uMySubnet , strict=False)

for x in network.hosts():
	response = pyping.ping(str(x))
	ip = socket.inet_ntoa(struct.pack('!L', x))
	if response.ret_code == 0:
		print "%s is up" % (ip)
	else:
		print "%s is down" % (ip)