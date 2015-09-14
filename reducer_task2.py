#!/usr/bin/python

import sys

wordCount = 0
node_id_array = set()	#Use 'set' to avoid duplicates
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	thisKey, node_id = data_mapped
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
	        continue

	if oldKey and oldKey != thisKey:
		print oldKey,"\t",wordCount,"\t",list(sorted(node_id_array))
		oldKey = thisKey
		wordCount = 0
		node_id_array = set()

	oldKey = thisKey
	wordCount += 1
	node_id_array.add(int(node_id))

if oldKey != None:
	print oldKey,"\t", wordCount,"\t",list(sorted(node_id_array))
	

