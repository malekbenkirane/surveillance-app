import logging
from flask import Flask, jsonify

# Importation relative de monitor
from monitor import check_server_status

# Configurer les logs
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    logging.debug("Home route accessed")
    return "Surveillance App is running!"

@app.route('/check_status')
def check_status():
    logging.debug("Check status route accessed")
    try:
        servers = check_server_status()
        logging.debug(f"Server status: {servers}")
        return jsonify(servers)
    except Exception as e:
        logging.error(f"Error in check_status route: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    logging.debug("Starting the Flask app")
    app.run(debug=True)
