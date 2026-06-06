# Stock Picker AI Agent

AI powered multi agent stock research and recommendation system built with CrewAI.

## Features

- Trending sector discovery
- Trending company analysis
- Financial research automation
- AI based stock recommendation
- Push notifications
- Persistent memory
- Web search integration

---

## Tech Stack

- Python
- CrewAI
- Pydantic
- SerpAPI
- Ollama
- SQLite
- Pushover

---

## Installation

```bash
git clone <repo-url>

cd stock-picker

pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```env
SERPAPI_API_KEY=your_key
PUSHOVER_USER=your_user
PUSHOVER_TOKEN=your_token
```

---

## Run Project

```bash
python main.py
```

---

## Workflow

1. Find trending sectors
2. Find trending companies
3. Research companies
4. Pick best stock
5. Send push notification

---

## Memory Support

- Long term memory using SQLite
- Short term RAG memory
- Entity based memory tracking

---

## Example Output

```text
=== FINAL DECISION ===

NVIDIA selected as strongest investment candidate due to AI market leadership and strong growth outlook.
```

---

## Future Enhancements

- Portfolio optimization
- Real time stock APIs
- Risk analysis engine
- Autonomous scheduled execution
- Advanced financial scoring
