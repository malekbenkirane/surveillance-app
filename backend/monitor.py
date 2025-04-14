import ping3
import json
import os
import logging

# Configurer les logs
logging.basicConfig(level=logging.DEBUG)

# Charger la liste des serveurs depuis le fichier JSON
file_path = os.path.join(os.path.dirname(__file__), 'server_list.json')

logging.debug(f"Reading server list from {file_path}")

try:
    with open(file_path, 'r') as f:
        servers = json.load(f)
    logging.debug("Server list loaded successfully")
except Exception as e:
    logging.error(f"Failed to load server list: {e}")

def ping(host):
    logging.debug(f"Pinging {host}...")
    try:
        # Utiliser ping3 pour vérifier si le serveur est accessible
        response = ping3.ping(host)
        if response is None:
            logging.debug(f"Ping to {host} timed out")
            return False
        else:
            logging.debug(f"Ping to {host} successful")
            return True
    except Exception as e:
        logging.error(f"Error during ping to {host}: {e}")
        return False

def check_server_status():
    logging.debug("Starting server status check")
    server_status = {}
    for server_name, ip in servers.items():
        logging.debug(f"Checking status of server: {server_name} with IP {ip}")
        status = ping(ip)
        server_status[server_name] = "Up" if status else "Down"
    logging.debug(f"Server status check complete: {server_status}")
    return server_status
