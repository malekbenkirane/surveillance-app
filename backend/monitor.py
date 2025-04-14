import ping3
import json

# Charger la liste des serveurs depuis le fichier JSON
with open('server_list.json', 'r') as f:
    servers = json.load(f)

def check_server_status():
    server_status = {}
    for server_name, ip in servers.items():
        status = ping3.ping(ip)
        server_status[server_name] = "Up" if status else "Down"
    return server_status
