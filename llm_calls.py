from pydantic import BaseModel
from openai import OpenAI
from typing import List
import json

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

# Fixed schema definition
class CommitRank(BaseModel):
    commit_id: str
    commit_rank: int

class ResponseFormat(BaseModel): 
    ranked_commits: List[CommitRank]  


prompt = "Analyze GitHub commit details, including content, to rank commits by contribution importance (e.g., typo fixes vs. kernel fixes). Return commit IDs and assigned ranks according to given Pydantic-compatible structure. I need all the commits ranked"


def structured_outputs(prompt, commits):
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": (prompt)},
                {"role": "user", "content": "\n".join(commits)},
            ],
            response_format=ResponseFormat,
        )

        event = completion.choices[0].message.parsed
        event_json = json.dumps(event.model_dump(), indent=4)
        print(event_json) #shows you the output, good for debugging
        
        return event
    except Exception as e:
        print(f"Error: {e}")
        return None


commits = [
    {
        "commits_details": "fixed cuda kernels",
        "commits_rank": 1,
        "commit_id": "a1b2c"
    },
    {
        "commits_details": "optimized data pipeline",
        "commits_rank": 2,
        "commit_id": "f3d9a"
    },
    {
        "commits_details": "added unit tests for ranking algorithm",
        "commits_rank": 3,
        "commit_id": "1e57c"
    },
    {
        "commits_details": "refactored API endpoints",
        "commits_rank": 4,
        "commit_id": "98a2b"
    },
    {
        "commits_details": "updated README with setup instructions",
        "commits_rank": 5,
        "commit_id": "0c23d"
    }
]
commit_json = json.dumps(commits, indent=2)

# print(json.dumps(commits, indent=4))
structured_outputs(prompt, commit_json)
