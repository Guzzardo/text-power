from collections import defaultdict
from helpers import *


def contact_ratio(texts):
	"""Returns how many times each party participated in the conversation"""
	participants = defaultdict(int)
	for text in texts:
		participants[text['name']] += 1
	return participants

def contact_ratio_with_emoji(texts):
	"""Returns how many times each party participated in the conversation"""
	participants = defaultdict(int)
	for text in texts:
		if contains_emoji(text['message']):
			participants[text['name']] += 1
	return participants


def contact_ratio_with_corrections(texts):
	"""Returns how many times each party corrected themselved (text contains *)"""
	participants = defaultdict(int)
	for text in texts:
		if '*' in text['message']:
			participants[text['name']] += 1
	return participants


def contact_ratio_with_exclamation(texts):
	"""Returns how many times each party corrected themselved (text contains !)"""
	participants = defaultdict(int)
	for text in texts:
		if '?' in text['message']:
			participants[text['name']] += 1
	return participants

def contact_ratio_with_question_mark(texts):
	"""Returns how many times each party corrected themselved (text contains !)"""
	participants = defaultdict(int)
	for text in texts:
		if '!' in text['message']:
			participants[text['name']] += 1
	return participants

def contact_ratio_message(texts, message):
	"""Returns how many times each party sent a given message"""
	participants = defaultdict(int)
	for text in texts:
		if text['message'].strip().lower() == message.strip().lower():
			participants[text['name']] += 1
	return participants

def contact_ratio_one_letter(texts, message):
	"""Returns how many times each party sent a one-character message"""
	participants = defaultdict(int)
	for text in texts:
		if len(text['message']) == 1:
			participants[text['name']] += 1
	return participants

def contact_ratio_swear_words(texts, message):
	"""Returns how many times each party sent swear words"""
	participants = defaultdict(int)
	for text in texts:
		for swear in [
						'anal',
						'anus',
						'arse',
						'ass',
						'balls',
						'bastard',
						'bitch',
						'biatch',
						'bloody',
						'blowjob',
						'blow job',
						'bollock',
						'bollok',
						'boner',
						'boob',
						'bugger',
						'bum',
						'butt',
						'clitoris',
						'cock',
						'coon',
						'crap',
						'cunt',
						'damn',
						'dick',
						'dildo',
						'dyke',
						'fag',
						'feck',
						'fellate',
						'fellatio',
						'felching',
						'fuck',
						'f u c k',
						'fudgepacker',
						'fudge packer',
						'flange',
						'Goddamn',
						'God damn',
						'hell',
						'homo',
						'jerk',
						'jizz',
						'knob',
						'muff',
						'nigger',
						'nigga',
						'penis',
						'piss',
						'prick',
						'pube',
						'pussy',
						'queer',
						'scrotum',
						'shit',
						's hit',
						'sh1t',
						'slut',
						'smegma',
						'spunk',
						'tit',
						'tosser',
						'turd',
						'twat',
						'vagina',
						'wank',
						'whore',
						'wtf',
					  ]:
			participants[text['name']] += text['message'].lower().count(swear)
	return participants

def contact_ratio_neediness(texts, message):
	"""Returns how many times each party sent needy words"""
	participants = defaultdict(int)
	for text in texts:
		for swear in ['i need',
					  'i want',
					  'my need',
					  'my want',
					  'will you',
					  'can you',
					  'would you',
					]:
			participants[text['name']] += text['message'].lower().count(swear)
	return participants

def contact_ratio_all_caps(texts, message):
	"""Returns how many times each party sent all caps"""
	participants = defaultdict(int)
	for text in texts:
		if text['message'].upper() == text['message']:
			participants[text['name']] += 1
	return participants

