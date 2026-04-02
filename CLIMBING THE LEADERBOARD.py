Problem Explanation (Climbing the Leaderboard)
This problem from HackerRank is about ranking scores.
🎮 How the leaderboard works (Dense Ranking)
Highest score → Rank 1
Same scores → Same rank
Next different score → Next rank (no gaps)
Example:

Scores:

100 100 50 40 40 20 10

Ranks:

1   1   2   3   3   4   5
👤 What you need to do

A player (Alice) plays multiple games and gets scores like:

5 25 50 120

👉 After each score, you must tell her rank on the leaderboard

📌 Example Understanding
Player Score	Rank Reason
5	Lower than all → Rank 6
25	Between 20 & 40 → Rank 4
50	Same as 50 → Rank 2
120	Higher than all → Rank 1

✅ Output:

6 4 2 1
💡 Key Idea to Solve Efficiently

Instead of checking from the top every time (slow ❌):

Do this:

Remove duplicate scores:

[100, 50, 40, 20, 10]
Start from the end (lowest score)
For each player score:
Move backward until you find where it fits
Assign rank

👉 This is fast because you only move in one direction

🚀 Python Code
def climbingLeaderboard(ranked, player):
    # Remove duplicates and keep descending order
    unique_scores = sorted(set(ranked), reverse=True)
    
    result = []
    i = len(unique_scores) - 1  # start from lowest rank
    
    for score in player:
        # Move left while player score is higher
        while i >= 0 and score >= unique_scores[i]:
            i -= 1
        
        # Rank is position + 2
        result.append(i + 2)
    
    return result
⚡ Time Complexity
Removing duplicates: O(n)
Traversing both lists: O(n + m)

✅ Very efficient for large inputs
