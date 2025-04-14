from flask import Flask, jsonify
from backend.monitor import check_server_status
from backend.mailer import send_alert

import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Surveillance App is running!"

@app.route('/check_status')
def check_status():
    servers = check_server_status()  # Fonction de vérification des serveurs
    return jsonify(servers)

if __name__ == "__main__":
    app.run(debug=True)

