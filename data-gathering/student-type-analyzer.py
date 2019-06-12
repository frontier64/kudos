import json
from collections import OrderedDict
from operator import itemgetter

read_json = open('./json/all.json', 'r')
data = json.load(read_json)

student_types = {}
count = 0
for user in data:
	count += 1
	if "studentType" not in user:
		continue
	for type in user["studentType"]:
		if type not in student_types:
			student_types[type] = 1
		else:
			student_types[type] += 1
print(OrderedDict(sorted(student_types.items(), key = itemgetter(1), reverse = True)))
