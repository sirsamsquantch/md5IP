from netaddr import IPNetwork
import hashlib

for ip in IPNetwork('10.2.6.1/23'):
	
	ip = str(ip).encode('utf-8')
	m = hashlib.md5()
	m.update(ip)
	md5 = m.hexdigest()


	if md5 == '7e4280601947cdb745d21f8582292598':
		print(str(ip)+' : '+str(md5))