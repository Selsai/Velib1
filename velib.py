from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# 1. Chargement
def load_velib_data():
    data = pd.read_csv("C:/Users/selsa/OneDrive/Documents/Velib/velib-pos.csv", delimiter=';')
    velib_data = []
    for index, row in data.iterrows():
        velib_data.append({'name': row['Nom de la station'], 'latitude': float(row['geo'].split(',')[0]), 'longitude': float(row['geo'].split(',')[1])})
    return velib_data

# 2. Route
@app.route('/')
def index():
    return render_template('map.html')

# 3. 2eme Route
@app.route('/get_velib_data')
def get_velib_data():
    velib_data = load_velib_data()
    return jsonify(velib_data)

if __name__ == '__main__':
    app.run(debug=True)
