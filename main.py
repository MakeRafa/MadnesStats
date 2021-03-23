import requests

from flask import Flask, render_template, request, send_file

from pprint import PrettyPrinter

app = Flask(__name__)

pp = PrettyPrinter(indent=4)

# API_URL ='https://balldontlie.io/api/v1/players/237'

@app.route('/')
def home():
    """Display the logo and search bars"""

    return render_template('home.html')

@app.route('/player_result', methods=['POST'])
def player_result():
    # player_id = request.args.get('id')

    name = request.form['player_name']

    player_info = requests.get('https://balldontlie.io/api/v1/players?search='+name+'')

    result_json = player_info.json()

    context = {
    'first_name': result_json['data'][0]['first_name'],
    'last_name': result_json['data'][0]['last_name'],
    'position': result_json['data'][0]['position'],
    'team_name': result_json['data'][0]['team']['full_name']

    }
    return render_template('player.html', **context)

    # params = {
    #     'id': player_id
    # }
    # result_json = requests.get(API_URL, params=params).json()
    # pp.pprint(result_json)

    # context = {
    #     'id': player_id,
    #     # 'first_name': result_json[first_name],
    #     # 'last_name': result_json[last_name],
    #     # 'position': result_json[position]
    # }

    # return render_template('player.html', **context)

if __name__ == '__main__':

    app.run(debug=True)