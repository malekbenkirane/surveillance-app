import socket
import json
import os

file_path = os.path.join(os.path.dirname(__file__), 'server_list.json')
try:
    with open(file_path, 'r') as f:
        servers = json.load(f)
except FileNotFoundError:
    print(f"Fichier {file_path} introuvable.")
    servers = {}

def check_server_status(port=80, timeout=2):
    server_status = {}
    for server_name, ip in servers.items():
        try:
            with socket.create_connection((ip, port), timeout=timeout):
                server_status[server_name] = "Up"
        except Exception as e:
            server_status[server_name] = f"Down ({e})"
    return server_status
