from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]



def structured_outputs():
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "Extract the event information."},
                {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
            ],
            response_format=CalendarEvent,
        )

        event = completion.choices[0].message.parsed
        
        return event
    except Exception as e:
        print(f"Error: {e}")
        return None

a = structured_outputs()
print(a)


commits = [
    {
        "commits_details": "fixed cuda kernels",
        "commits_author": "suvrakamal",
        "commits_date": "2025-03-25",
        "commits_id": "1234567890",
        "commits_branch": "main",
        "commits_rank": 1
    },
    {
        "commits_details": "optimized data pipeline",
        "commits_author": "alexdoe",
        "commits_date": "2025-03-24",
        "commits_id": "0987654321",
        "commits_branch": "main",
        "commits_rank": 2
    },
    {
        "commits_details": "added unit tests for ranking algorithm",
        "commits_author": "janedoe",
        "commits_date": "2025-03-23",
        "commits_id": "1122334455",
        "commits_branch": "feature/ranking",
        "commits_rank": 3
    },
    {
        "commits_details": "refactored API endpoints",
        "commits_author": "suvrakamal",
        "commits_date": "2025-03-22",
        "commits_id": "6677889900",
        "commits_branch": "main",
        "commits_rank": 4
    },
    {
        "commits_details": "updated README with setup instructions",
        "commits_author": "alexdoe",
        "commits_date": "2025-03-21",
        "commits_id": "5544332211",
        "commits_branch": "docs",
        "commits_rank": 5
    }
]