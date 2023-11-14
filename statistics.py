from flask import jsonify, abort

# calculating statistics for API endpoint
def statistics(data, player_name):
    games_played = 0
    for player_stats in data:
        if player_stats[0] == player_name:
            games_played += 1
    if(games_played == 0):
        abort(404, description=f"Player not found!")

    response = {
        'playerName': player_name,
        'gamesPlayed': games_played,
        'traditional': {
            'freeThrows': {
                'attempts' : None,
                'made' : None,
                'shootingPercentage' : None,
            },
            'twoPoints' : {
                'attempts' : None,
                'made' : None,
                'shootingPercentage' : None,
            },
            'threePoints' : {
                'attempts' : None,
                'made' : None,
                'shootingPercentage' : None,
            },
            'points' : None,
            'rebounds' : None,
            'blocks' : None,
            'assists' : None,
            'steals' : None,
            'turnovers' : None,
        },
        'advanced' : {
            'valorization' : None,
            'effectiveFieldGoalPercentage' : None,
            'trueShootingPercentage' : None,
            'hollingerAssistRatio' : None
        }
    }
    
    return response