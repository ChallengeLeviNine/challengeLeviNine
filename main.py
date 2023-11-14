import csv
import json
from flask import Flask
from response import generate_response
from prints import terminal_print

app = Flask(__name__)
player_data = None

# loading data from csv
def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        #skipping header
        next(csv_reader)

        for row in csv_reader:
            data.append(row)
    return data

# API endpoint
@app.route('/stats/player/<string:player_name>', methods=['GET'])
def get_stats(player_name):
    global player_data
    if player_data is None:
        player_data = load_data('L9HomeworkChallengePlayersInput.csv')

    response = json.dumps(generate_response(player_data, player_name), ensure_ascii=False, indent=4)

    terminal_print(response)
    
    return app.response_class(
        response=response,
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)