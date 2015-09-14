#!/usr/bin/python

# Format of each line is:
# IP/Identity/Username/Time/Request/Status/Size
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

import sys
import re

regex = '([0-9\.]+) ([w.-]+) ([w.-]+) \[(.*?)\] "(.*?)" (\d*) (\d*)'
website = 'http://www.the-associates.co.uk'

for line in sys.stdin:
	data = re.match(regex, line)

	if data is None:
		continue
	# Note: All the following are not required always
	ip_addres, identity, username, time, request, status, filesize = data.groups()
	
        # At this stage a request should look like this:
        # GET /assets/js/lowpro.js HTTP/1.1
	request = request.split(" ")[1]

        # Some path names might come along with the website
	if re.match(website,request):
		request = request.split(website)[1]

	if len(request)>1:
		print "{0}\t{1}".format(request,1)
	
