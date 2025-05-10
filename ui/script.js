async function loadRequests() {
    const res = await fetch('http://localhost:8000/requests');
    const data = await res.json();
  
    const container = document.getElementById('requests');
    container.innerHTML = '';
  
    data.reverse().forEach(req => {
      const div = document.createElement('div');
      div.className = `request ${req.status}`;
  
      div.innerHTML = `
        <p><strong>Question:</strong> ${req.question}</p>
        <p><strong>Status:</strong> ${req.status}</p>
        ${req.status === 'pending' ? `
          <input type="text" placeholder="Supervisor answer" id="answer-${req.id}" />
          <button onclick="submitAnswer('${req.id}')">Submit</button>
        ` : `
          <p><strong>Answer:</strong> ${req.response}</p>
        `}
      `;
  
      container.appendChild(div);
    });
  }
  
  async function submitAnswer(id) {
    const answerInput = document.getElementById(`answer-${id}`);
    const answer = answerInput.value;
  
    const res = await fetch('http://localhost:8000/respond', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ request_id: id, answer: answer })
    });
  
    if (res.ok) {
      alert('Response submitted!');
      loadRequests(); // refresh
    } else {
      alert('Failed to submit response.');
    }
  }
  async function loadKnowledgeBase() {
    const res = await fetch('http://localhost:8000/knowledge-base');
    const data = await res.json();
  
    const ul = document.getElementById('knowledge-base');
    ul.innerHTML = '';
  
    Object.entries(data).forEach(([question, answer]) => {
      const li = document.createElement('li');
      li.innerHTML = `<strong>${question}</strong>: ${answer}`;
      ul.appendChild(li);
    });
  }
  

  loadRequests();
  loadKnowledgeBase();
