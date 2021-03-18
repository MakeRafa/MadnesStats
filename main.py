import requests

from flask import Flask, render_template, request, send_file


app = Flask(__name__)

API_URL ='https://balldontlie.io/api/v1/players'

@app.route('/')
def home():
    """Display the logo and search bars"""

    return render_template('home.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)