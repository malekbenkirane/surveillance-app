from flask import Flask, jsonify
from monitor import check_server_status
from mailer import send_alert

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
