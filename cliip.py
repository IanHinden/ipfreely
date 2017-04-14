from flask import Flask
import pyping, socket, ipaddress, struct
from flask_sqlalchemy import SQLAlchemy
from IP_Status import db, IpStatus

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
	ip_record = IpStatus.query.filter(IpStatus.ip_address.endswith(ip)) #see if there is an equals method instead of endswith
	status = IpStatus(ip, True)
	if response.ret_code == 0:
		print "%s is free" % (ip)
		status.free = True
	else:
		print "%s is claimed" % (ip)
		status.free = False
	if not ip_record:
		db.session.add(status)
	else:
		ip_record.free = status.free
	db.create_all() #necessary?
	db.session.commit()