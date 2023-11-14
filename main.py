import csv
from flask import Flask 
from statistics import statistics

app = Flask(__name__)
player_data = None

# loading data from csv
def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

# API endpoint
@app.route('/stats', methods=['GET'])
def get_stats():
    global player_data
    if player_data is None:
        player_data = load_data('L9HomeworkChallengePlayersInput.csv')

    response = statistics(player_data)
    return response

if __name__ == '__main__':
    app.run(debug=True)