# Human-in-the-Loop AI Supervisor (Frontdesk Assignment)

## 🚀 Project Overview

A simulated AI receptionist that:

- Handles customer questions
- Escalates unknown queries to a human supervisor
- Follows up with users
- Learns and updates its knowledge base over time

## 📁 Folder Structure

- `agent/`: Simulated AI logic
- `backend/`: FastAPI backend API
- `database/`: JSON-based DB for help requests and KB
- `ui/`: Supervisor admin panel (HTML/JS)
- `data/`: Persistent storage files

## 🛠 Tech Stack

- Python, FastAPI
- HTML + JS for UI
- JSON files as DB (can be swapped with Firebase/SQLite)

## 📦 Features

- Simulated AI answering from a salon knowledge base
- Auto-escalation when unknown
- Supervisor responds via UI
- AI auto-replies and learns
- Timeout for unanswered queries
- Knowledge base viewer

## 🖥 How to Run

### 1. Backend API

```bash
uvicorn backend.app:app --reload
```

### 2. Opening the UI

```cd ui
python -m http.server 5500
```

### 3. Running the AI Agent

```
python agent/simulated_agent.py
```

### 4. (Optional) Starting timeout handler

```
python -m backend.timeout_checker
```
