import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def get_path(filename):
    return os.path.join(DATA_DIR, filename)

def load_requests():
    path = get_path('pending_requests.json')
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)

def save_requests(data):
    with open(get_path('pending_requests.json'), 'w') as f:
        json.dump(data, f, indent=4)

def load_kb():
    path = get_path('knowledge_base.json')
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def save_kb(kb):
    with open(get_path('knowledge_base.json'), 'w') as f:
        json.dump(kb, f, indent=4)
