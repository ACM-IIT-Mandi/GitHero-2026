# GitHero 2K26: Gotta Commit 'Em All

Team Rocket has raided the Pokémon League. The Champion's Trophy and the Gym Badges are gone, scattered across Kanto with traps left behind. You are the last trainer with a working terminal. Every task you finish wins back one badge.

**Points:** 5 / 5 / 10 / 25 / 25 / 30 = 100

## How this works

- Go to the **Issues** tab. Do Tasks 1, 2 and 3 in order: they are guided. Tasks 4, 5 and 6 do not depend on each other. Pick any order. (Task 6 only needs the starter you chose in Task 1.)
- Every task = one Pull Request, titled `Task <N>: <your-github-username>`.
- Tasks 4 to 6 read like a real bug report: a situation and the result that is wanted. They do not tell you what went wrong in the repository, or which commands fix it.
- Any use of AI help is strictly prohibited.
- You may push again as often as you like. Ties are broken by the time of your last accepted Pull Request.

## PR rules, Tasks 1 to 3

- Start each task from your up-to-date `main`, not from the branch of the previous task.
- Branch name: `task-<N>/<your-github-username>`
- Only add files under `submissions/<your-github-username>/task<N>/`
- Put a `proof.md` there with: the pasted command output (as text), the link to your Pull Request, and your line `BADGE: xxxxxxxx`
- You only get the link once the Pull Request is open: open it, add the link to `proof.md`, then commit and push again. The Pull Request updates by itself.
- Get a badge with: `python badge.py <your-github-username> "<answer>"`

## PR rules, Tasks 4 to 6

- The issue names the branches. Each issue ends with a "Done when" list. The organizers check your fork against it: there is no badge to compute.

## Before you start

- git 2.38 or newer, Python 3, and git-filter-repo (`pip install git-filter-repo`).
- **When you fork, untick "Copy the main branch only"**

## Tips

`git status`, `git log --oneline --graph --all` and `git reflog` are your Town Map.

Practice: https://learngitbranching.js.org, https://ohmygit.org
