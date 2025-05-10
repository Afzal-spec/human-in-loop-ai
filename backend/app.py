from fastapi import FastAPI, HTTPException
from database.db import load_requests, save_requests, load_kb, save_kb
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Or specify GET, POST, etc.
    allow_headers=["*"],
)


class SupervisorResponse(BaseModel):
    request_id: str
    answer: str

@app.get("/requests")
def get_all_requests():
    return load_requests()

@app.post("/respond")
def respond_to_request(response: SupervisorResponse):
    requests = load_requests()
    updated = False

    for req in requests:
        if req["id"] == response.request_id and req["status"] == "pending":
            req["status"] = "resolved"
            req["response"] = response.answer
            updated = True
            break

    if not updated:
        raise HTTPException(status_code=404, detail="Request not found or already resolved")

    save_requests(requests)

    # Update knowledge base
    kb = load_kb()
    kb[req["question"]] = response.answer
    save_kb(kb)

    # Simulate AI following up
    print(f"🤖 AI (follow-up): {req['response']} (original question: {req['question']})")

    return {"message": "Response recorded and knowledge base updated"}

@app.get("/knowledge-base")
def get_knowledge_base():
    return load_kb()
