from flask import Flask, render_template
from web_scraping import get_states
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/states')
def states():
    return render_template('states.html', states=get_states())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
