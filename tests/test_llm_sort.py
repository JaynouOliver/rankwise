import pytest
from rankwise.llm_sort import llm_bubble_sort

def test_llm_bubble_sort():
    commits = [
        {"commit_id": "a1b2c", "details": "Fixed CUDA kernels", "rank": 1},
        {"commit_id": "f3d9a", "details": "Optimized data pipeline", "rank": 2},
    ]
    
    sorted_commits = llm_bubble_sort(commits)
    
    assert sorted_commits[0]['commit_id'] == 'a1b2c'
