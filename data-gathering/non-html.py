import json
import re

splitter = "Re: 2019 Applicant Profiles and Admission Results"

def doSearch(search, text):
	matcher = re.compile(search)
	s = matcher.search(text)
	return s


def doFile(year):
	file = open("posts/" + str(year) + ".txt", "r")

	user = {"username": 'N/A', "universities": {}}
	splitter = file.readline()
	outFile = open("json/" + str(year) + ".json", "w")
	outFile.write("[\n")

	count = 0
	usertext = ""
	gpaCount = 0
	greQCount = 0
	majorCount = 0
	information = []
	for line in file:
		if splitter in line: 		#We've come to a new user
			count+=1

			outFile.write(json.dumps(user) + ",\n")
			for key in user:
				user[key] = 'N/A'
			user["universities"] = {}
		matcher = re.compile(r'Postby (\w*) ')
		s = matcher.search(line)
		if (s):
			user['username'] = s.group(1)
			#print(s.group(1))

		s = doSearch(r'Major\(s\): (\w*)', line)
		if (s):
			majorCount += 1
			user['major'] = s.group(1)

		s = doSearch(r'(?i)Undergrad Institution: (.*)\n', line)
		if (s):
			user['undergraduateInstitution'] = s.group(1)

		s = doSearch(r'(?i)Overall GPA: (\d.\d\d?)', line)
		if (s):
			user['overallGpa'] = s.group(1)
			gpaCount += 1

		s = doSearch(r'Q: ?(\d\d\d?)', line)
		if (s):
			greQCount += 1
			user['greQ'] = s.group(1)

		s = doSearch(r'V: ?(\d\d\d?)', line)
		if (s):
			user['greV'] = s.group(1)

		s = doSearch(r'W: ?(\d.\d\d?|\d)', line)
		if (s):
			user['greW'] = s.group(1)

		s = doSearch(r'P: ?(\d\d\d?)', line)
		if (s):
			user['greP'] = s.group(1)

		s = doSearch(r'(?i)^([^-]*).*(Rejected|Rejection)', line)
		if (s):
			user["universities"][s.group(1).strip()] = 'rejected'

		s = doSearch(r'(?i)^([^-]*).*(Accepted|Acceptance)', line)
		if (s):
			user["universities"][s.group(1).strip()] = 'accepted'

		s = doSearch(r'(?i)Type of Student:(.*)', line)
		if(s):
			user["studentType"] = s.group(1).strip().lower().replace(',','').split(' ')

		matcher = re.compile(r'Overall.GPA\s?:\s?(\d\.\d\d?)')

	file.close()
	print("\nData for year: ", year)
	print('overall gpa pct: ', gpaCount / count)
	print('overall major pct: ', majorCount / count)
	print('overall greQ pct: ', greQCount / count)
	outFile.write("]")
	outFile.close()


for i in range(2009, 2018):
	doFile(i)