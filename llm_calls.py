from pydantic import BaseModel
from openai import OpenAI
from typing import List
import json

client = OpenAI()

# Fixed schema definition
class CommitRank(BaseModel):
    commit_id: str
    commit_rank: int

class ResponseFormat(BaseModel): 
    ranked_commits: List[CommitRank]  

class TwoStrings(BaseModel):
    string_id: int
    string_id: int

context_prompt = "Analyze GitHub commit details, including content, to rank commits by contribution importance (e.g., typo fixes vs. kernel fixes). Return commit IDs and assigned ranks according to given Pydantic-compatible structure. I need all the commits ranked"


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

def compare_two_string(data1, data2):
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "Compared the two information and rank them according to the context".join(context_prompt)},
                {"role": "user", "content": "\n".join(data1, data2)},
            ],
            response_format=TwoStrings,
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


#step 2 
#we're gonna put a sorting algorithm here mixed with LLM sorting

def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
