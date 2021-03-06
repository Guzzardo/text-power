from collections import defaultdict
from helpers import *
import numpy
from textblob import TextBlob

"""
poop emoji count
sentiment analysis
neediness
	I want
	I need
	could you
	will you
sorry count
big words count
all caps (passion)
texts least
average text length
k count
"""


def sentiment_struc():
	return {
		'pos': 0,
		'neg': 0,
		'neutral': 0,
	}
# {:adam => {:pos => 42, :neg => 53, :neutral => 54}}
def sentiment_count(texts):
	participants = defaultdict(sentiment_struc)
	for text in texts:
		if text['message'].lower().strip() == 'ok':
			continue
		text_blob = TextBlob(text['message'])
		sentiment_score = text_blob.sentiment.polarity
		if sentiment_score > 0:
			participants[text['name']]['pos'] += 1
		elif sentiment_score < 0:
			participants[text['name']]['neg'] += 1
		else:
			participants[text['name']]['neutral'] += 1
	return participants

def positivity_average(texts):
	"""Returns the positivity score for each party"""
	participants = defaultdict(list)
	for text in texts:
		text_blob = TextBlob(text['message'])
		pos_score = text_blob.sentiment.polarity
		if pos_score > .1:
			participants[text['name']].append(pos_score)
	ret = {}
	for key,value in participants.items():
		average = sum(value) / len(value)
		ret[key] = average
	return ret

def negativity_average(texts):
	"""Returns the negativity score for each party"""
	participants = defaultdict(list)
	for text in texts:
		text_blob = TextBlob(text['message'])
		neg_score = text_blob.sentiment.polarity
		if neg_score < -.1:
			participants[text['name']].append(neg_score)
	ret = {}
	for key,value in participants.items():
		average = sum(value) / len(value)
		ret[key] = average
	return ret

def sentiment_average(text):
	"""Returns the average sentiment for each party"""
	participants = defaultdict(list)
	for text in texts:
		text_blob = TextBlob(text['message'])
		sentiment_score = text_blob.sentiment.polarity
		if sentiment_score > .1 or sentiment_score < -1:
			participants[text['name']].append(sentiment_score)
	ret = {}
	for key,value in participants.items():
		average = sum(value) / len(value)
		ret[key] = average
	return ret

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

def contact_ratio_one_letter(texts):
	"""Returns how many times each party sent a one-character message"""
	participants = defaultdict(int)
	for text in texts:
		if len(text['message']) == 1:
			participants[text['name']] += 1
	return participants

def contact_ratio_swear_words(texts):
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

def contact_ratio_neediness(texts):
	"""Returns how many times each party sent needy words"""
	participants = defaultdict(int)
	for text in texts:
		for word in ['i need',
					  'i want',
					  'my need',
					  'my want',
					  'will you',
					  'can you',
					  'would you',
					]:
			participants[text['name']] += text['message'].lower().count(word)
	return participants

def contact_ratio_word_count(texts, keyword):
	participants = defaultdict(int)
	for text in texts:
		if keyword.lower() in text['message'].lower():
			participants[text['name']] += text['message'].lower().count(keyword)
	return participants

def contact_ratio_neediness_i_want(texts):
	return contact_ratio_word_count(texts, 'i want')

def contact_ratio_neediness_i_need(texts):
	return contact_ratio_word_count(texts, 'i need')

def contact_ratio_neediness_could_you(texts):
	return contact_ratio_word_count(texts, 'could you')

def contact_ratio_neediness_would_you(texts):
	return contact_ratio_word_count(texts, 'would_you')

def contact_ratio_sorry(texts):
	return contact_ratio_word_count(texts, 'sorry')

def contact_ratio_problem(texts):
	participants = defaultdict(int)
	for text in texts:
		for word in ['np',
					  'no problem',
					]:
			participants[text['name']] += text['message'].lower().count(word)
	return participants

def contact_ratio_my_bad(texts):
	return contact_ratio_word_count(texts, 'my bad')

def contact_ratio_poop(texts):
	return contact_ratio_word_count(texts, u'\udca9')

def contact_ratio_all_caps(texts):
	"""Returns how many times each party sent all caps"""
	participants = defaultdict(int)
	for text in texts:
		if text['message'].upper() == text['message']:
			participants[text['name']] += 1
	return participants

def contact_ratio_k(texts):
	participants = defaultdict(int)
	for text in texts:
		if text['message'].lower() == 'k':
			participants[text['name']] += 1
	return participants

def contact_ratio_average_length(texts):
	"""Returns how many times each party sent all caps"""
	participants = defaultdict(list)
	for text in texts:
		participants[text['name']].append(len(text['message']))
	return dict((name, "%.2f" % numpy.mean(sizes)) for name, sizes in participants.items())

def contact_ratio_big_words(texts):
	participants = defaultdict(int)
	for text in texts:
		for word in text['message'].split(' '):
			if len(word) >= 10:
				participants[text['name']] += 1
	return participants
