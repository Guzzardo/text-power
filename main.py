
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request

from smparse.helpers import *
from smparse.rules import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        file_contents = request.files['messages'].read().decode('utf-16')

        username, texts = parse_message_file(file_contents)

        # ratio
        ratio_values = contact_ratio(texts)
        # Get the other persons name
        partner_name = [i for i in ratio_values.keys() if i != username][0]
        partner_first_name = 'Stephanie' #partner_name.split(' ')[0]
        ratio = "{}:{}".format(ratio_values[username], ratio_values[partner_name])

        if ratio_values[username] < ratio_values[partner_name]:
        	ratio_message = "{} sent you {} more texts!!".format(partner_first_name, ratio_values[partner_name]-ratio_values[username])
        elif ratio_values[username] > ratio_values[partner_name]:
        	ratio_message = "You text more :("
        else:
        	ration_message = "You both text the same amount!"


        ### GET THE POOP COUNT
        ratio_values = contact_ratio_poop(texts)

        if ratio_values[username] < ratio_values[partner_name]:
        	poop_ratio_message = "{} sends more poop.".format(partner_first_name)
        elif ratio_values[username] > ratio_values[partner_name]:
        	poop_ratio_message = "You send more poop."
        else:
        	poop_ratio_message = "You both send the same amount of poop!"

        poop_count_message = "You sent {}, {} sent {}".format(ratio_values[username], partner_first_name, ratio_values[partner_name])



        return render_template('new_results.html', 
        	partner_first_name=partner_first_name,
        	ratio=ratio,
        	ratio_message=ratio_message,
        	poop_ratio_message=poop_ratio_message,
        	poop_count_message=poop_count_message,
        )
    else:
        return render_template('landing.html')


@app.route('/send_sms', methods=['GET'])
def send_message():
	send_text()
	return ''


if __name__ == '__main__':
    app.run(debug=True)