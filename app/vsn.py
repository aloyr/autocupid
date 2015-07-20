import csv, os, re, Levenshtein

class VSN:
	"""data abstraction logic goes here
	   for this exercise, no ORM like sqlalchemy is needed
	"""

	vsn = list()
	vsn_pattern = re.compile('[a-z]{6}[0-9]{6}', re.IGNORECASE)

	def __init__(self):
		"""initialize class
		"""
		if len(self.vsn) == 0:
			data = csv.reader(open(os.path.dirname(os.path.realpath(__file__)) + '/data/vsn_data.csv', 'r'))
			for row in data:
				self.vsn.append([re.compile(row[0].replace('*','.'), re.IGNORECASE)] + row)

	def getTable(self):
		output = ''
		for row in self.vsn:
			output += str(row[1:]) + ' <br />\n'
		return output

	def search(self, vsnid):
		"""return list of matching VSNs
		   uses levenshtein comparison similarly to php
		   could also have used difflib here
		"""
		matches = list()
		current_ratio = 0
		for item in self.vsn:
			if (item[0].match(vsnid)):
				new_ratio = Levenshtein.ratio(vsnid, item[1])
				if (new_ratio >= current_ratio):
					if (new_ratio > current_ratio):
						matches = list()
						current_ratio = new_ratio
					matches.append(item[1:])
		return (matches if len(matches) > 0 else None)

	def sanitize(self, vsnid):
		"""crude prevention of bobby tables attack
		   https://xkcd.com/327/
		"""
		if ((len(vsnid) == 0) or ((len(vsnid) == 12) and (self.vsn_pattern.match(vsnid)))):
			result = True
		else:
			result = False
		return result