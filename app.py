from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Charger les données depuis le CSV
data = pd.read_csv('atp_ranking.csv', sep = ';')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    player_name = request.form.get('player_name')
    if not player_name:
        return render_template('index.html', error="Veuillez entrer un nom de joueur.")
    
    # Filtrer les données pour trouver le joueur
    player_data = data[data['player'].str.contains(player_name, case=False, na=False)]
    if player_data.empty:
        return render_template('index.html', error="Joueur non trouvé.")
    
    # Extraire les informations pertinentes
    stats = player_data.iloc[0].to_dict()
    return render_template('index.html', player=stats)

if __name__ == '__main__':
    app.run(debug=True)
