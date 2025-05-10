import json
import os
from datetime import datetime

# Load the knowledge base
def load_knowledge_base():
    with open('data/knowledge_base.json', 'r') as f:
        return json.load(f)

# Log a help request if the AI doesn't know the answer
def trigger_help_request(question):
    help_request = {
        "id": f"req_{int(datetime.utcnow().timestamp())}",
        "question": question,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat(),
        "response": None
    }

    # Load existing requests
    if os.path.exists('data/pending_requests.json'):
        with open('data/pending_requests.json', 'r') as f:
            requests = json.load(f)
    else:
        requests = []

    requests.append(help_request)

    # Save back to file
    with open('data/pending_requests.json', 'w') as f:
        json.dump(requests, f, indent=4)

    print(f"📨 Help request created for supervisor: {question}")


# Simulate a phone call
def handle_call():
    print("📞 Incoming call received...")
    question = input("👤 Caller asks: ")

    kb = load_knowledge_base()

    answer = kb.get(question)

    if answer:
        print(f"🤖 AI Agent: {answer}")
    else:
        print("🤖 AI Agent: Let me check with my supervisor and get back to you.")
        trigger_help_request(question)


if __name__ == "__main__":
    handle_call()
