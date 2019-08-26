#!/usr/bin/python
import requests
import os
import random
import string
import json
import sys
import geocoder

from torrequest import TorRequest

ip_check_url = 'http://ipecho.net/plain'

original_ip = requests.get(ip_check_url).text
print("My original Ip: %s" % original_ip)

tr = TorRequest(password=os.environ.get('TOR_PASS'))

target_url = 'http://newtaxicsv.taxiromaniaonline.ro/aplicatie/make_request'

addresses = json.load(open('addresses1.json'))
userAgents = json.load(open('userAgents.json'))

while True:
	try:
		tr.reset_identity()
		tor_ip = tr.get(ip_check_url).text
		print("Using ip: %s" % tor_ip)

		if tor_ip == original_ip:
			raise ValueError("%s == %s" % (tor_ip, original_ip))

		headers = {
			'User-agent': random.choice(userAgents)
		}
		print("Headers: %s" % headers)


		address = str(random.choice(addresses))
		nr = random.choice(range(1,6))

		randomPrefix = random.choice(["str", "strada", "str.", "Str.", "St"])
		address = address.replace("Strada", randomPrefix)

		full_addr = '%s, nr. %d, %s' % (address, nr, 'Suceava')
		g = geocoder.arcgis(full_addr)
		device_id = ''.join(str(random.randint(0,8)) for e in range(15))

		data = {
			'version': 5,
			'device_id': device_id,
			'app_id': 'androidapp',
			'action': 'import_reservation',
			'street': '%s, nr. %d' % (address, nr),
			'street_no': nr,
			'building': '',
			'scara': '',
			'details': '',
			'latitude': g.latlng[0],
			'longitude': g.latlng[1],
			'eta': random.choice([5, 10, 15])
		}

		print("Sending request payload:")
		print(json.dumps(data, indent=2))

		# response = tr.post(target_url, data=data, headers=headers)
		# print("Response status_code %d " % response.status_code)

	except Exception as e:
		print("Error occured %s" % e)
		sys.exit()
	