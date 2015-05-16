import csv

from rules import *


def main():
	input_file = open('Adam_s_iPhone and Joe_Guzzardo__UCB___5868500690_.txt')
	file_contents = input_file.read().decode("utf-16")
	username, texts = parse_message_file(file_contents)

	print "USERNAME : {}".format(username)
	
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

	print "\"Sentiment Count"
	print sentiment_count(texts)

	print "\nPositivity Average"
	print positivity_average(texts)

	print "\nNegativity average"
	print negativity_average(texts)

	print "\ncontact_ratio_one_letter"
	print contact_ratio_one_letter(texts)

	print "\ncontact_ratio_swear_words"
	print contact_ratio_swear_words(texts)

	print "\ncontact_ratio_neediness"
	print contact_ratio_neediness(texts)

	print "\ncontact_ratio_word_count -- sorry"
	print contact_ratio_word_count(texts, 'sorry')

	print "\n Poop"
	print contact_ratio_poop(texts)

	print "\n I want"
	print contact_ratio_neediness_i_want(texts)

	print "\n I need"
	print contact_ratio_neediness_i_need(texts)

	print "\n Could You"
	print contact_ratio_neediness_could_you(texts)

	print "\n Would You"
	print contact_ratio_neediness_would_you(texts)

	print "\n Sorry"
	print contact_ratio_sorry(texts)

	print "\n All Caps"
	print contact_ratio_all_caps(texts)

	print "\n avg length"
	print contact_ratio_average_length(texts)

	print "\n big words"
	print contact_ratio_big_words(texts)


if __name__ == '__main__':
	main()
	
