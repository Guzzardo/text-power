
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

        return render_template('test_results.html', messages_content=texts)
    else:
        return render_template('landing.html', name='name')


@app.route('/send_sms', methods=['GET'])
def send_message():
	send_text()
	return ''


if __name__ == '__main__':
    app.run(debug=True)