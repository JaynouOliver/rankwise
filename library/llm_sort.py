from .compare import compare_commits

def llm_bubble_sort(commits):
    """
    Sorts a list of commits using LLM-based comparisons.
    """
    commit_map = {c['commit_id']: c for c in commits}
    sorted_ids = [(c['commit_id'], c['rank']) for c in commits]

    for i in range(len(sorted_ids) - 1):
        swapped = False
        for j in range(len(sorted_ids) - i - 1):
            current_id, _ = sorted_ids[j]
            next_id, _ = sorted_ids[j + 1]

            higher_id, lower_id = compare_commits(commit_map[current_id], commit_map[next_id])

            if higher_id == next_id:
                sorted_ids[j], sorted_ids[j + 1] = sorted_ids[j + 1], sorted_ids[j]
                swapped = True

        if not swapped:
            break

    return [commit_map[id] for id, _ in sorted_ids]
