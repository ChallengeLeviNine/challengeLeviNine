from flask import abort

# calculating statistics for API endpoint
def generate_response(data, player_name):
    #all variables is set to zero
    games_played = ftm = fta = pm2 = pa2 = pm3 = pa3 = reb = blk = ast = stl = tov = 0
    val = []
    efg = []
    shp = []
    har = []

    #going through csv data, calcuating simple stats
    for player_stats in data:
        #checking for name from path
        if player_stats[0] == player_name:
            games_played += 1
            #sum simple stats
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
            #calculating advanced stats
            val.append(round((int(player_stats[2])+2*int(player_stats[4])+3*int(player_stats[6])+int(player_stats[8])+int(player_stats[9])+int(player_stats[10])+int(player_stats[11]))-(int(player_stats[3])-int(player_stats[2])+int(player_stats[5])-int(player_stats[4])+int(player_stats[7])-int(player_stats[6])+int(player_stats[12])),2))
            efg.append(round((int(player_stats[4])+int(player_stats[6])+0.5*int(player_stats[6]))/(int(player_stats[5])+int(player_stats[7]))*100,2))
            shp.append(round((int(player_stats[2])+2*int(player_stats[4])+3*int(player_stats[6]))/(2*(int(player_stats[5])+int(player_stats[7])+0.475*int(player_stats[3])))*100,2))
            har.append(round(int(player_stats[10])/(int(player_stats[5])+int(player_stats[7])+0.475*int(player_stats[3])+int(player_stats[10])+int(player_stats[12]))*100,2))

    #name doesn't exist
    if(games_played == 0):
        abort(404, description=f"Player not found!")

    #format response
    response = {
        'playerName': player_name,
        'gamesPlayed': games_played,
        'traditional': {
            'freeThrows': {
                'attempts' : round(fta/games_played,1),
                'made' : round(ftm/games_played,1),
                'shootingPercentage' : round(ftm/fta*100,1),
            },
            'twoPoints' : {
                'attempts' : round(pa2/games_played,1),
                'made' : round(pm2/games_played,1),
                'shootingPercentage' : round(pm2/pa2*100,1),
            },
            'threePoints' : {
                'attempts' : round(pa3/games_played,1),
                'made' : round(pm3/games_played,1),
                'shootingPercentage' : round(pm3/pa3*100,1),
            },
            'points' : round((ftm+2*pm2+3*pm3)/games_played,1),
            'rebounds' : round(reb/games_played,1),
            'blocks' : round(blk/games_played,1),
            'assists' : round(ast/games_played,1),
            'steals' : round(stl/games_played,1),
            'turnovers' : round(tov/games_played,1),
        },
        'advanced' : {
            'valorization' : round(sum(val)/games_played,1),
            'effectiveFieldGoalPercentage' : round(sum(efg)/games_played,1),
            'trueShootingPercentage' : round(sum(shp)/games_played,1),
            'hollingerAssistRatio' : round(sum(har)/games_played,1)
        }
    }
    
    return response