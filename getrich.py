#!/usr/bin/python3

import json
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='Get Rich Headers from LaikaBOSS JSON and return a list of PE compilation tools')
parser.add_argument('-c', '--comp_ids',
                    help='path to comp_ids.txt from https://github.com/dishather/richprint')
parser.add_argument('-i', '--infile',
                    help='path to LaikaBOSS JSON file')

try:
	with open(args.infile, 'r') as f:
		result = json.load(f)
except:
	print("Bad JSON file")

try:
	comp_ids = list()
	with open(args.compd_ids, 'r') as f:
		for line in f:
			line = line.strip()
			if line and not line.startswith("#"):
				comp_ids.append(line)
	comp_dict = dict()
	for comp_id in comp_ids:
		comp_dict[comp_id[0:8]] = comp_id[9:]
except:
	print("Bad comp_ids.txt")
	print("https://github.com/dishather/richprint")

try:
	for scan_result in result['scan_result']:
		rich_list = list()
		if 'META_PE' in scan_result['moduleMetadata'].keys():
			rich_values = dict()
			try:
				rich_values = scan_result['moduleMetadata']['META_PE']['Rich Header']['Rich Header Values']
			except:
				pass
			if rich_values:
				rich_list.append(rich_values)
	if rich_list:
		for rich_values in rich_list:
			pprint(rich_values)
			for rich_value in rich_values:
				rich = '{:04X}'.format(rich_value['Id']) + '{:04X}'.format(rich_value['Version'])
				try:
					print("%s: %s" % (rich, comp_dict[rich.lower()]))
				except KeyError:
					print("%s: No matching ID and Version" % rich)
except:
	print("I don't know what you did, but you broke it.")
