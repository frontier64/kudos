from difflib import SequenceMatcher as sm
import json
from collections import OrderedDict
from operator import itemgetter
"""
s1 ='Columbia'
s2 = 'Yale \u2013 CMT (Feb. 13:'
if s1 in s2:
	print("In")
print(sm(None, s1, s2).ratio())
"""

read_json = open('./posts/good-batch-2019.json', 'r')
data = json.load(read_json)
uni_list_f = open('uni-list.txt', 'r')
uni_list = uni_list_f.read().split(';\n')
for i in range(0, len(uni_list)):
	uni_list[i] = uni_list[i].lower()
	uni_list[i] = uni_list[i].split(', ')

uni_counts = {}
for uni in uni_list:
	uni_counts[uni[0]] = 0
junk_unis = {}
for user in data:
	for university in user["universities"]:
		found = False
		university = university.lower()
		university = university.replace("university","").replace("of","").replace("school","").replace("the").trim()
		for potentialUni in uni_list:
			for nickname in potentialUni:
				if university in nickname or sm(None, university, nickname).ratio() > .95:
					uni_counts[potentialUni[0]] += 1
					found = True
					break
			if found:
				break
		if not found:
			if university in junk_unis:
				junk_unis[university] += 1
			else:
				junk_unis[university] = 1

print(OrderedDict(sorted(junk_unis.items(), key = itemgetter(1), reverse = True)))
uni_list_f.close()
uni_list_f = open('uni-list.txt', 'a')
for key in junk_unis:
	if junk_unis[key] > 5:
		uni_list_f.write(key + ";\n")

uni_list_f.close()