import openai

def compare_commits(commit1, commit2):
    """
    Compare two commits using OpenAI API and return their ranks.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Rank these commits based on technical importance."},
                {"role": "user", "content": f"Commit A: {commit1['details']}\nCommit B: {commit2['details']}"}
            ]
        )
        result_text = response.choices[0].message.content.strip()
        return (commit1['commit_id'], commit2['commit_id']) if "A" in result_text else (commit2['commit_id'], commit1['commit_id'])
    except Exception as e:
        print(f"Error comparing commits: {e}")
        return (commit1['commit_id'], commit2['commit_id'])
