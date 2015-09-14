#!/usr/bin/python

import sys
import csv
import re


reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
	# If the node_id is not valid then ignore that line
	# This check should suffice for some other scenarios too where it should be ignored
	try:
		body = line[4]
		node_id = int(line[0])
	except:
		continue
	# Parse the sentences into words
	# A word is strictly an array of alphabets (no digits and etc)
	bodyWords = re.findall(r"['\w]+",body)
	for word in bodyWords:
		if len(re.findall(r"[a-z]",word.lower())) == len(word):
			print "{0}\t{1}".format(word.lower(),node_id)
	
