#!/usr/bin/env python

'''
This is script pings any number of remote IP Addresses from a source router.
This currently uses Cisco onePK via the CPAL package to connect to the source router.
'''

import sys
from cpal.core.main import device


def cping(src,dest):

	ping_device = device('ping_device','cisco',src)

	for address in dest:
		
		ping_results = ping_device.cli('ping '+ address).split('\n')[-1].split(',')[0]

		print '-----------------------------------------------------'
		print 'SOURCE: ' + src + ' DESTINATION: ' + address
		print ping_results
		print '-----------------------------------------------------'

if __name__ == "__main__":
	source = '10.1.1.110'
	dests = ['10.1.1.110','10.1.1.120','10.1.1.130']
	cping(source,dests)


'''
SAMPLE OUTPUT WHEN RUNNING THE PROGRAM

cisco@onepk:~/apps/pinger$ python pinger.py

-----------------------------------------------------
SOURCE: 10.1.1.110 DESTINATION: 10.1.1.110
Success rate is 100 percent (5/5)
-----------------------------------------------------
-----------------------------------------------------
SOURCE: 10.1.1.110 DESTINATION: 10.1.1.120
Success rate is 100 percent (5/5)
-----------------------------------------------------
-----------------------------------------------------
SOURCE: 10.1.1.110 DESTINATION: 10.1.1.130
Success rate is 100 percent (5/5)
-----------------------------------------------------
'''