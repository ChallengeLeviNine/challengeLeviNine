# Challenge LeviNine - Basketball Stats API

__Overview__  
This is a simple python script that iimplements a Basketball Stats API using Flask. The API reads player statistics from a CSV file, exposes an endpoint to retrieve player stats, and allows filtering by player name.

__Prerequisites__  
Make sure you have Python installed on your system. You can download Python from the official Python website.

__Usage__  
1. Run the Flask app from terminal : python main.py

2. Open your web browser and navigate to: http://127.0.0.1:5000/stats/player/playerName
   
Replace playerName with desired player's name. This will return a JSON response containing the player's statistics.

Here are a few examples:

http://127.0.0.1:5000/stats/player/Luyanda%20Yohance  
http://127.0.0.1:5000/stats/player/Haji%20Nabulung  
http://127.0.0.1:5000/stats/player/Sifiso%20Abdalla  
http://127.0.0.1:5000/stats/player/Try%20This *(this will open error page, player with name Try This doesn't exist!)* 

__Customization__  
You can modifiy the CSV file ('L9HomeworkChallengePlayersInput.csv') with your own data.

__Dependencies__  
Flask: Web framework for Python
