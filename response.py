from flask import abort

# calculating statistics for API endpoint
def generate_response(data, player_name):
    #all variables is set to zero
    games_played = ftm = fta = pm2 = pa2 = pm3 = pa3 = reb = blk = ast = stl = tov = 0

    #going through csv data, calcuating simple stats
    for player_stats in data:
        #checking for name from path
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

    #name doesn't exist
    if(games_played == 0):
        abort(404, description=f"Player not found!")

    #format response
    response = {
        'playerName': player_name,
        'gamesPlayed': games_played,
        'traditional': {
            'freeThrows': {
                'attempts' : fta,
                'made' : ftm,
                'shootingPercentage' : round(ftm/fta*100,1),
            },
            'twoPoints' : {
                'attempts' : pa2,
                'made' : pm2,
                'shootingPercentage' : round(pm2/pa2*100,1),
            },
            'threePoints' : {
                'attempts' : pa3,
                'made' : pm3,
                'shootingPercentage' : round(pm3/pa3*100,1),
            },
            'points' : round(ftm+2*pm2+3*pm3,1),
            'rebounds' : reb,
            'blocks' : blk,
            'assists' : ast,
            'steals' : stl,
            'turnovers' : tov,
        },
        'advanced' : {
            'valorization' : round((ftm+2*pm2+3*pm3+reb+blk+ast+stl)-(fta-ftm+pa2-pm2+pa3-pm3+tov),1),
            'effectiveFieldGoalPercentage' : round((pm2+pm3+0.5*pm3)/(pa2+pa3)*100,1),
            'trueShootingPercentage' : round((ftm+2*pm2+3*pm3)/(2*(pa2+pa3+0.475*fta))*100,1),
            'hollingerAssistRatio' : round(ast/(pa2+pa3+0.475*fta+ast+tov)*100,1)
        }
    }
    
    return response