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
