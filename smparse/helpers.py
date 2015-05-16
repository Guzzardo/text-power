import time
import re
import calendar
from time import mktime
from datetime import datetime
import emoji
import csv

def parse_time(date_time_string):
	"""Accepts a time string in '' format, and returns it in epoch format"""
	parsed_time_struct = time.strptime(date_time_string, "%m/%d/%y %I:%M %p")
	converted_date_time = datetime.fromtimestamp(mktime(parsed_time_struct))
	epoch_time = calendar.timegm(converted_date_time.timetuple())

	return epoch_time

def parse_message_file(raw_input):
	"""Accepts file content and returns list of message dicts"""
	lines = raw_input.split('\n[')
	lines.pop(0)

	company_regex = re.compile('(\[(.)*\])')
	phone_regex = re.compile('(\(\d+\))')

	texts = []
	for line in lines:
		time_string, entry = line.split(']', 1)
		name, message = entry.split(':', 1)
		name = company_regex.sub('', name).strip()
		name = phone_regex.sub('', name).strip()

		texts.append({
			'timestamp': parse_time(time_string),
			'name': name.strip(),
			'message': message,
		})

	return texts

def parse_csv_texts(csv_texts):
	"""Accepts CSV parsed content, and makes it into the content as above"""
	company_regex = re.compile('(\[(.)*\])')
	phone_regex = re.compile('(\(\d+\))')
	texts = []
	for csv_text in csv_texts:
		timestamp = parse_time('{} {}'.format(csv_text['Date'], csv_text['Time']))
		name = company_regex.sub('', csv_text['Name']).strip()
		name = phone_regex.sub('', name).strip()
		texts.append({
			'timestamp': timestamp,
			'name': name,
			'message': csv_text['Text'],
			'attachment': (csv_text['Attachment'] == 'none')
		})
	return texts

def is_emoji(char):
	"""returns True if char is emoji"""
	try:
		emoji.decode(char)
	except ValueError:
		return False
	return True

def contains_emoji(string):
	"""returns True if string contains emoji"""
	return u'\ud83d' in string
