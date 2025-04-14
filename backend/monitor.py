import ping3
import json
import os

# Obtenir le chemin absolu du fichier JSON
file_path = os.path.join(os.path.dirname(__file__), 'server_list.json')

# Charger la liste des serveurs avec gestion d'erreur
try:
    with open(file_path, 'r') as f:
        servers = json.load(f)
except FileNotFoundError:
    print(f"Fichier {file_path} introuvable.")
    servers = {}

def check_server_status():
    server_status = {}
    for server_name, ip in servers.items():
        try:
            status = ping3.ping(ip, timeout=1)
            server_status[server_name] = "Up" if status else "Down"
        except Exception as e:
            server_status[server_name] = f"Error: {e}"
    return server_status