from flask import jsonify, abort

# calculating statistics for API endpoint
def statistics(data, player_name):
    games_played = ftm = fta = pm2 = pa2 = pm3 = pa3 = reb = blk = ast = stl = tov = 0

    for player_stats in data:
        if player_stats[0] == player_name:
            games_played += 1
            ftm += int(player_stats[2])
            fta += int(player_stats[3])
            pm2 += int(player_stats[4])
            pa2 += int(player_stats[5])
            pm3 += int(player_stats[6])
            pa3 += int(player_stats[7])
            reb += int(player_stats[8])
            blk += int(player_stats[9])
            ast += int(player_stats[10])
            stl += int(player_stats[11])
            tov += int(player_stats[12])


    if(games_played == 0):
        abort(404, description=f"Player not found!")

    response = {
        'playerName': player_name,
        'gamesPlayed': games_played,
        'traditional': {
            'freeThrows': {
                'attempts' : fta,
                'made' : ftm,
                'shootingPercentage' : None,
            },
            'twoPoints' : {
                'attempts' : pa2,
                'made' : pm2,
                'shootingPercentage' : None,
            },
            'threePoints' : {
                'attempts' : pa3,
                'made' : pm3,
                'shootingPercentage' : None,
            },
            'points' : None,
            'rebounds' : reb,
            'blocks' : blk,
            'assists' : ast,
            'steals' : stl,
            'turnovers' : tov,
        },
        'advanced' : {
            'valorization' : None,
            'effectiveFieldGoalPercentage' : None,
            'trueShootingPercentage' : None,
            'hollingerAssistRatio' : None
        }
    }
    
    return response