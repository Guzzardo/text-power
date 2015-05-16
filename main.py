
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        messages_content = request.files['messages'].read().decode('utf-8')

        return render_template('test_results.html', messages_content=messages_content)
    else:
        return render_template('test_home.html', name='name')


if __name__ == '__main__':
    app.run(debug=True)