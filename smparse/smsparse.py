import csv

from rules import *


def main():
	input_file = open('Adam_s_iPhone and Joe_Guzzardo__UCB___5868500690_.txt')
	file_contents = input_file.read().decode("utf-16")
	texts = parse_message_file(file_contents)
	
	# rows = csv.DictReader(open('Adam_s_iPhone and Joe_Guzzardo__UCB___5868500690_.csv', 'rb'))
	# csv_texts = [row for row in rows]
	# texts = parse_csv_texts(csv_texts)
	# return texts

	print "Text to Text Ratio"
	print contact_ratio(texts)

	print "\nText to Text Ratio with emoji"
	print contact_ratio_with_emoji(texts)

	print "\nText to Text Ratio with corrections"
	print contact_ratio_with_corrections(texts)

	print "\nText to Text Ratio with exclamations"
	print contact_ratio_with_exclamation(texts)

	print "\nText to Text Ratio with question marks	"
	print contact_ratio_with_question_mark(texts)

	print "\nText to Text Ratio with just K"
	print contact_ratio_message(texts, 'k')

	print "\nText to Text Ratio with just Ok"
	print contact_ratio_message(texts, 'ok')

	
	print sentiment_count(texts)

	print positivity_average(texts)

	print negativity_average(texts)

if __name__ == '__main__':
	main()
	
