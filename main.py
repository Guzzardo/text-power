
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':


        return render_template('test_results.html', name='name')
    else:
        return render_template('test_home.html', name='name')


