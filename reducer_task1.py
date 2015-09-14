#!/usr/bin/python

import sys

hitCount = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	thisKey, count = data_mapped
	
	# Unless it is the first key and a different key is recieved from previous save the count
	if oldKey and oldKey != thisKey:
	        print oldKey, "\t", hitCount
	        oldKey = thisKey;
	        hitCount = 0

	oldKey = thisKey
	hitCount += 1

# Save the last key value
if oldKey != None:
    print oldKey, "\t", hitCount	
