import requests

from flask import Flask, render_template, request, send_file

from pprint import PrettyPrinter

app = Flask(__name__)

pp = PrettyPrinter(indent=4)

API_URL ='https://balldontlie.io/api/v1/players/237'

@app.route('/')
def home():
    """Display the logo and search bars"""

    return render_template('home.html')

@app.route('/player_result')
def player_result():
    player_id = request.args.get('id')

    params = {
        'id': player_id
    }
    result_json = requests.get(API_URL, params=params).json()
    pp.pprint(result_json)

    context = {
        'first_name': result_json[first_name],
        'last_name': result_json[last_name],
        'position': result_json[position]
    }

    return render_template('player.html')

if __name__ == '__main__':

    app.run(debug=True)