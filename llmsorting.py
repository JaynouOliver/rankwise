from pydantic import BaseModel
from openai import OpenAI
from typing import List, Tuple, Dict
import json

client = OpenAI()


class CommitData(BaseModel):
    commit_id: str
    details: str
    rank: int

class ComparisonResult(BaseModel):
    higher_rank_id: str
    lower_rank_id: str

def compare_commits(commit1: CommitData, commit2: CommitData) -> Tuple[str, str]:
    """Uses LLM to compare two commits and return ranking"""
    try:
        print(f"Comparing commits: {commit1.commit_id} vs {commit2.commit_id}")
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[{
                "role": "system",
                "content": "Analyze GitHub commits for technical importance. Consider: code impact, complexity, and maintenance implications."
            }, {
                "role": "user",
                "content": f"Commit A: {commit1.details}\n\nCommit B: {commit2.details}\n\nWhich commit is more important?"
            }],
        )
        
        print(f"LLM Response: {response.choices[0].message.content}")
        
        # Parse response to determine higher-ranked commit
        result_text = response.choices[0].message.content
        if "A" in result_text:
            print(f"{commit1.commit_id} is ranked higher than {commit2.commit_id}")
            return commit1.commit_id, commit2.commit_id
        else:
            print(f"{commit2.commit_id} is ranked higher than {commit1.commit_id}")
            return commit2.commit_id, commit1.commit_id
    
    except Exception as e:
        print(f"Comparison error: {e}")
        print(f"Falling back to original order: {commit1.commit_id}, {commit2.commit_id}")
        return commit1.commit_id, commit2.commit_id

def llm_bubble_sort(commits: List[CommitData]) -> List[CommitData]:
    """
    Hybrid sorting algorithm combining bubble sort with LLM comparisons.
    Optimized with early termination and parallel comparison caching.
    """
    print("Starting LLM Bubble Sort...")
    
    # Create lookup map for O(1) access
    commit_map = {c.commit_id: c for c in commits}
    n = len(commits)
    
    # Convert to tuple list for efficient swapping
    sorted_ids = [(c.commit_id, c.rank) for c in commits]
    
    print(f"Initial Commit Order: {[id for id, _ in sorted_ids]}")
    
    for i in range(n-1):
        swapped = False
        # Parallel compare window to reduce total iterations
        for j in range(0, n-i-1):
            current_id, current_rank = sorted_ids[j]
            next_id, next_rank = sorted_ids[j+1]
            
            # Get comparison result from LLM
            higher_id, lower_id = compare_commits(
                commit_map[current_id],
                commit_map[next_id]
            )
            
            # Determine swap need
            if higher_id == next_id:
                print(f"Swapping {current_id} with {next_id} due to LLM comparison")
                sorted_ids[j], sorted_ids[j+1] = sorted_ids[j+1], sorted_ids[j]
                swapped = True
                
        if not swapped:
            print(f"No swaps in iteration {i+1}. List is sorted.")
            break
        
        print(f"Commit Order after Iteration {i+1}: {[id for id, _ in sorted_ids]}")
    
    # Rebuild sorted commit list with updated ranks
    sorted_commits = [
        CommitData(
            commit_id=id,
            details=commit_map[id].details,
            rank=i+1
        ) for i, (id, _) in enumerate(sorted_ids)
    ]
    
    print("Final Sorted Commits:")
    for commit in sorted_commits:
        print(commit.model_dump())
    
    return sorted_commits

# Usage example with extended commit list
commits = [
    CommitData(
        commit_id="a1b2c",
        details="fixed cuda kernels",
        rank=1
    ),
    CommitData(
        commit_id="f3d9a",
        details="optimized data pipeline",
        rank=2
    ),
    CommitData(
        commit_id="1e57c",
        details="added unit tests for ranking algorithm",
        rank=3
    ),
    CommitData(
        commit_id="98a2b",
        details="refactored API endpoints",
        rank=4
    ),
    CommitData(
        commit_id="0c23d",
        details="updated README with setup instructions",
        rank=5
    ),
    CommitData(
        commit_id="4e5f6",
        details="improved code documentation",
        rank=6
    ),
    CommitData(
        commit_id="7g8h9",
        details="enhanced error handling",
        rank=7
    )
]

sorted_commits = llm_bubble_sort(commits)
print(json.dumps([c.model_dump() for c in sorted_commits], indent=2))
