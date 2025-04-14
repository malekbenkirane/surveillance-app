import ping3
import json

# Charger la liste des serveurs depuis le fichier JSON
import os

file_path = os.path.join(os.path.dirname(__file__), 'server_list.json')
with open(file_path, 'r') as f:

    servers = json.load(f)

def check_server_status():
    server_status = {}
    for server_name, ip in servers.items():
        status = ping3.ping(ip)
        server_status[server_name] = "Up" if status else "Down"
    return server_status
