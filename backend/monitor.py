import ping3
import json
import os

# Charger la liste des serveurs depuis le fichier JSON
file_path = os.path.join(os.path.dirname(__file__), 'server_list.json')

try:
    with open(file_path, 'r') as f:
        servers = json.load(f)
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} est introuvable.")
    servers = {}  # Si le fichier n'est pas trouvé, initialiser un dictionnaire vide.
except json.JSONDecodeError:
    print(f"Erreur : Impossible de décoder le fichier {file_path}. Assurez-vous qu'il est bien formaté en JSON.")
    servers = {}

def check_server_status():
    server_status = {}
    for server_name, ip in servers.items():
        try:
            status = ping3.ping(ip)
            if status is None:
                server_status[server_name] = "Down (timed out)"
            else:
                server_status[server_name] = "Up"
        except Exception as e:
            server_status[server_name] = f"Down (Erreur : {str(e)})"
    return server_status
