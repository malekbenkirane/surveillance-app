import subprocess
import json
import os

# Charger la liste des serveurs depuis le fichier JSON
file_path = os.path.join(os.path.dirname(__file__), 'server_list.json')
with open(file_path, 'r') as f:
    servers = json.load(f)

def ping(host):
    # Exécute la commande ping de Windows et retourne le code de sortie
    command = ['ping', '-n', '1', host]
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if response.returncode == 0:
        return True
    else:
        return False

def check_server_status():
    server_status = {}
    for server_name, ip in servers.items():
        status = ping(ip)
        server_status[server_name] = "Up" if status else "Down"
    return server_status
