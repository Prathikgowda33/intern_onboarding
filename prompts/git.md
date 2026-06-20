# Prompts — Git

For the [Git topic](../topics/git/). Common situations: confusing history, merge conflicts,
undoing mistakes, branch recovery. **Git mistakes feel scary** — these prompts emphasize
"don't make it worse."

---

## My git log / history is confusing

**When:** you can't tell what happened from `git log --graph`.

```
[CONTEXT] I'm working on the Git <level> assignment. I expected my history to show
<e.g., "a branch with 2 commits, then a merge back to main">.
[ACTUAL] Here's my `git log --oneline --graph --all`:
```<paste full output>```

[WHAT'S HAPPENING — my understanding]
Reading the graph, I think:
- <line/branch 1> represents <main / my feature branch>
- The divergence at <hash> is where <I created the branch>
- The merge at <hash> is where <I merged back>
Correct me where I'm wrong.

[WHAT'S WRONG — my hypothesis]
The graph <doesn't show a branch / shows a straight line / has commits in the wrong
place>, which I think means <e.g., "I did a fast-forward merge instead of --no-ff, so no
merge commit was created">.

[ASK] Walk me through reading this graph: what each line means, where the branch points
are, what's missing vs. what the assignment expects. Then tell me if my history is
actually fine or if I need to redo something — and if so, the exact safe commands.
```

---

## Stuck in a merge conflict

**When:** `git merge` reports conflicts and you don't know how to resolve them.

```
[CONTEXT] I was merging <branch> into <main>. Git reported conflicts.
[ACTUAL] `git status` shows these conflicted files:
```<paste git status output>```
One conflicted file looks like this:
```<paste the file with <<<<<<< ======= >>>>>>> markers, or the relevant section>```

[WHAT'S HAPPENING — my understanding]
My understanding of what the markers mean:
- `<<<<<<< HEAD` = <your interpretation — the version on current branch>
- `=======` = <separator>
- `>>>>>>> branch-name` = <the version coming in from the other branch>
I need to <your understanding of what "resolving" means — e.g., "pick one side or combine
both, then remove the markers">.

[WHAT'S WRONG — my hypothesis]
I want to keep <e.g., "my change to line X from main, but take their change to line Y
from the branch">. I'm <confident/unsure> how to combine them without breaking syntax.

[WHAT I TRIED]
- I <read the conflict / tried editing / ran `git merge --abort`> and <result>.

[ASK] First, confirm my understanding of the conflict markers. Then walk me through
resolving THIS specific conflict: what the final file should look like, and the exact git
commands to stage + commit the resolution. Don't rush — I don't want to lose work.
```

---

## I made a mistake and need to undo it (scary moment)

**When:** you ran a git command and now something is wrong, and you're afraid to make it worse.

```
[CONTEXT] I ran `<the exact git command>` and now <what happened — e.g., "my last commit
is gone" / "I'm on a detached HEAD" / "I reset and lost my work">.

[WHAT'S HAPPENING — my understanding]
I think what `<command>` did was <your understanding — e.g., "it moved my branch pointer
back one commit, but the commit still exists, just unreachable">.

[WHAT'S WRONG — my hypothesis]
I think I can recover with <e.g., "git reflog to find the lost commit hash, then git reset
--hard to it">, but I'm scared of running another destructive command.

[INFO I GATHERED]
- `git status` shows: <paste>
- `git reflog` (last 10 lines) shows: <paste>
- `git log --oneline -5` shows: <paste>

[ASK] DON'T give me a command to run yet. First, reassure me whether my work is actually
recoverable (is it in reflog? dangling? gone?). Then explain, step by step, the safest
recovery path — and what each command does to my history. Warn me before any command that
could make things worse. I want to understand before I act.
```

---

## Accidentally committed something I shouldn't have (secret, big file)

**When:** you pushed/committed a secret, huge file, or wrong content and want to remove it from history.

```
[CONTEXT] I committed <what — e.g., "a .env file with API keys" / "a 500MB video"> on
branch <branch>. <It's been pushed / it's only local>.
[ACTUAL] The commit <hash> contains the bad file.

[WHAT'S HAPPENING — my understanding]
I understand that:
- If it's only local, I can amend or reset to remove it.
- If it's pushed, others may have pulled it, and rewriting history is more dangerous.
<Confirm or correct this.>

[WHAT'S WRONG — my hypothesis]
I think I need <e.g., "git rebase -i to drop the commit, or git filter-branch /
git-filter-repo to strip just the file from history">. I'm unsure which is right and
whether it's safe given <pushed/not pushed>.

[ASK] Given my situation (<pushed/not pushed>, <solo/team repo>), what's the safest way to
remove this? Walk me through it step by step. CRITICAL: if it's a secret, also tell me
what else I must do (rotate the key? force-push? notify collaborators?). Don't minimize
the remediation — I'd rather over-react.
```

---

## Branch / commit seems lost

**When:** you switched branches and your work "disappeared."

```
[CONTEXT] I was working on <branch>. I <did something — switched branches / ran a
command> and now my changes <are gone / aren't showing up>.
[ACTUAL] `<git status / git branch / git log>` shows:
```<paste>```

[WHAT'S HAPPENING — my understanding]
My understanding of Git: commits exist as objects, branches are just pointers. So "lost"
work is usually still in the repo, just not referenced by my current branch. I think my
work is <e.g., "on the other branch I switched away from" / "in reflog as a dangling
commit">.

[WHAT'S WRONG — my hypothesis]
I think I need to <e.g., "git checkout <other-branch> to get back" / "find the commit in
reflog and cherry-pick or reset to it">.

[INFO I GATHERED]
- `git branch -a` shows: <paste>
- `git reflog | head -20` shows: <paste>
- `git stash list` shows: <paste>

[ASK] Help me find where my work actually is (walk through reflog with me). Then tell me
the exact command to get back to it. Reassure me it's not gone — Git rarely truly loses
committed work.
```

---

## Don't understand branching / merging conceptually

**When:** you're fuzzy on what branches/merges actually do.

```
[CONTEXT] I'm learning Git. I can run the commands but I don't really understand what's
happening "under the hood."
[GOAL] I want a clear mental model of <branches / merging / rebasing / remote tracking>.

[WHAT'S HAPPENING — my current (possibly wrong) mental model]
Here's what I currently think:
- A branch is <your understanding — e.g., "a separate copy of all my files">.
- A merge is <your understanding — e.g., "combining two folders">.
- <Confusion> — <e.g., "I don't get how the same commit can be on two branches">.

[ASK] Correct my mental model where it's wrong. Use the "commits are snapshots, branches
are sticky notes (pointers)" analogy. Give me a tiny concrete example with 3-4 commits and
show what happens to the pointers when I branch and merge. Don't use jargon without
defining it. I want intuition, not a command reference.
```

---

## Should I rebase or merge?

**When:** you've heard of both but don't know which to use.

```
[CONTEXT] I have a feature branch with <N> commits. Main has moved ahead with <M> commits.
I want to integrate.
[GOAL] Decide between `git merge main` and `git rebase main`.

[WHAT'S HAPPENING — my understanding]
My current understanding:
- merge: <your interpretation — e.g., "creates a merge commit, preserves branch history">
- rebase: <your interpretation — e.g., "replays my commits on top of main, rewrites
  history, linear log">
I'm confused about <e.g., "when rebase is dangerous" / "the golden rule of rebase">.

[ASK] Compare merge vs rebase for my situation. Explain: (1) what each does to history
(show me a before/after sketch), (2) the golden rule (never rebase shared/public
branches — why?), (3) which you'd recommend for a solo learner like me and why. Don't
just say "rebase is cleaner" — explain the tradeoff.
```

---

## Pre-commit / hook / config confusion

**When:** something about `.gitconfig`, hooks, or `.gitignore` isn't behaving.

```
[CONTEXT] I'm trying to <configure something — e.g., "make git ignore node_modules" /
"set my default branch name" / "run a hook before commit">.
[ACTUAL] <It's not working / I get an error / unexpected behavior>.

[WHAT'S HAPPENING — my understanding]
I think <`.gitignore` / `.gitconfig` / hooks> works by <your mental model>. I edited
<file> to <change>. I expect <result>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., ".gitignore only affects untracked files — if node_modules is already
tracked, adding it to .gitignore won't untrack it" / "my hook isn't executable">.

[INFO I GATHERED]
- `cat <config file>`: <paste>
- `git config --list` (relevant lines): <paste>
- `ls -l .git/hooks/`: <paste if hooks>

[ASK] Confirm my understanding of how <gitignore/config/hooks> works. Then diagnose why my
setup isn't behaving and give me the fix. Explain the gotcha so I don't hit it again.
```
