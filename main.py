import csv
import json
from flask import Flask 
from statistics import statistics

app = Flask(__name__)
player_data = None

# loading data from csv
def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        next(csv_reader)#skipping header

        for row in csv_reader:
            data.append(row)
    return data

# API endpoint
@app.route('/stats/player/<string:player_name>', methods=['GET'])
def get_stats(player_name):
    global player_data
    if player_data is None:
        player_data = load_data('L9HomeworkChallengePlayersInput.csv')

    response = statistics(player_data, player_name)
    return app.response_class(
        response=json.dumps(response, ensure_ascii=False, indent=4),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)