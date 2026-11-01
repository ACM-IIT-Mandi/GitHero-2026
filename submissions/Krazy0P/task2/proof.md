git remote -v
origin  https://github.com/Krazy0P/GitHero-2026.git (fetch)
origin  https://github.com/Krazy0P/GitHero-2026.git (push)
upstream        https://github.com/ACM-IIT-Mandi/GitHero-2026.git (fetch)
upstream        https://github.com/ACM-IIT-Mandi/GitHero-2026.git (push)


git log --oneline -3
59b379e (HEAD -> task-2/Krazy0P, origin/task-2/Krazy0P) chore: ignore rocket junk
9d1e163 (upstream/main, upstream/HEAD, origin/main, origin/HEAD, main) add hall of fame
1013d0c add hall of fame archive


git status --ignored
On branch task-2/Krazy0P
Your branch is up to date with 'origin/task-2/Krazy0P'.

Ignored files:
  (use "git add -f <file>..." to include in what will be committed)
        submissions/Krazy0P/task2/.env
        submissions/Krazy0P/task2/battle.log

nothing to commit, working tree clean


git reflog -5
59b379e (HEAD -> task-2/Krazy0P, origin/task-2/Krazy0P) HEAD@{0}: commit (amend): chore: ignore rocket junk
301a474 HEAD@{1}: commit: chore: ignore rockt junk
9d1e163 (upstream/main, upstream/HEAD, origin/main, origin/HEAD, main) HEAD@{2}: checkout: moving from main to task-2/Krazy0P
9d1e163 (upstream/main, upstream/HEAD, origin/main, origin/HEAD, main) HEAD@{3}: checkout: moving from task-1/Krazy0P to main
e50acba (origin/task-1/Krazy0P, task-1/Krazy0P) HEAD@{4}: commit: proof added


https://github.com/ACM-IIT-Mandi/GitHero-2026/pull/12


b8dc5890