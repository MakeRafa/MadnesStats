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

    player_stat_info = requests.get('https://balldontlie.io/api/v1/season_averages?season=2020&player_ids[]='+str(result_json['data'][0]['id'])+'')

    result2_json = player_stat_info.json()


    context = {
    'first_name': result_json['data'][0]['first_name'],
    'last_name': result_json['data'][0]['last_name'],
    'position': result_json['data'][0]['position'],
    'team_name': result_json['data'][0]['team']['full_name'],
    
    'player_id': result_json['data'][0]['id'],

    'pts': result2_json['data'][0]['pts'],
    'ast': result2_json['data'][0]['ast'],
    'reb': result2_json['data'][0]['reb']
    
    }


    return render_template('player.html', **context)

# @app.route('/player_stats', methods=['POST'])
# def player_stats():

#     player_id = request.form['players_id']

#     player_stat_info = requests.get('https://balldontlie.io/api/v1/season_averages?player_ids[]='+player_id+'')

#     json_result = player_stat_info.json()

#     context = {
#         'pts': json_result['data'][0]['pts']
#     }
#     return render_template('stats.html', **context)

if __name__ == '__main__':

    app.run(debug=True)