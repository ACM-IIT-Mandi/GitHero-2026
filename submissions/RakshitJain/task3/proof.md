Que1:A file called hideout_notes.txt was deleted at some point. Which commit deleted it?
Command: git log --oneline
Output: 
9ff052f (HEAD -> task-3/rakshitjain026-cyber, origin/main, origin/HEAD, main) Added proof
6c23378 feat: rakshitjain026-cyber chooses Charmender
9d1e163 (upstream/main, upstream/HEAD) add hall of fame
1013d0c add hall of fame archive
b012c9c add wild encounter
cc96f2e add submissions folder
5318fd8 readme: note that answers are case-sensitive
973c23b add route 4 map
38b0356 remove hideout notes
a41db4d add celadon gym
604ed8a fix typo in mewtwo notes
bfb0600 update item list
65e0f66 [ROCKET-INTEL] shipment schedule for Silph Co.
d9641b0 add hideout notes
a25ce9a add gym leader list
640ca58 add mewtwo lab notes
88d9c7b initial commit

Answer(Que1): 38b0356

Que2: That file, before deletion, contained a line PASSCODE: <something>. What is the passcode?
Command:  git show 38b0356
Output:
commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

diff --git a/hideout_notes.txt b/hideout_notes.txt
deleted file mode 100644
index de0834a..0000000
--- a/hideout_notes.txt
+++ /dev/null
@@ -1,4 +0,0 @@
-Rocket hideout, basement level
-Guard rotation: every 4 hours
-PASSCODE: SilphScope
-Do not share outside the team.

Answer(Que2): SilphScope

Que3: Exactly one commit message contains the tag [ROCKET-INTEL]. Which commit is it, and who is its author?
Command: 1.git log --oneline 
         2.git show 65e0f66
Output: 1.9ff052f (HEAD -> task-3/rakshitjain026-cyber, origin/main, origin/HEAD, main) Added proof
6c23378 feat: rakshitjain026-cyber chooses Charmender
9d1e163 (upstream/main, upstream/HEAD) add hall of fame
1013d0c add hall of fame archive
b012c9c add wild encounter
cc96f2e add submissions folder
5318fd8 readme: note that answers are case-sensitive
973c23b add route 4 map
38b0356 remove hideout notes
a41db4d add celadon gym
604ed8a fix typo in mewtwo notes
bfb0600 update item list
65e0f66 [ROCKET-INTEL] shipment schedule for Silph Co.
d9641b0 add hideout notes
a25ce9a add gym leader list
640ca58 add mewtwo lab notes
88d9c7b initial commit

2. commit 65e0f66a16c7e6a241edd4fab9b0d784a4ddd6ab
Author: Giovanni <giovanni@rocket.example>
Date:   Thu Sep 24 13:48:00 2026 +0530

    [ROCKET-INTEL] shipment schedule for Silph Co.

diff --git a/lab/intel.txt b/lab/intel.txt
new file mode 100644
index 0000000..060b02c
--- /dev/null
+++ b/lab/intel.txt
@@ -0,0 +1,2 @@
+Silph Co. shipment arrives Friday.
+Two guards on the loading dock.

Answer(Que3): Commit: 65e0f66 & Author: Giovanni <giovanni@rocket.example>

Que4: In lab/mewtwo_notes.txt, who last modified line 7, and in which commit?
First we need to go to lab directory from current directory , i did cd .. for three times to come out of pwd
Command: cd lab , git blame mewtwo_notes.txt , 
Output:
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 1) Mewtwo notes - Cerulean Cave lab
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 2) Subject created from a fossil sample.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 3) Genetic splicing started at 02:00.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 4) Power readings are unstable.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 5) Containment field set to level 3.
604ed8ab (Archer    2026-09-26 15:02:00 +0530 6) Psychic output higher than any known subject, retested.
604ed8ab (Archer    2026-09-26 15:02:00 +0530 7) Subject escaped the containment tank.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 8) Tank rebuilt with reinforced glass.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 9) Observation continues.

Answer(Que4): 604ed8ab (Archer    2026-09-26 15:02:00 +0530 7) Subject escaped the containment tank.
So Archer changed the 7 line in commit 604ed8ab

https://github.com/ACM-IIT-Mandi/GitHero-2026/pull/30

python badge.py rakshitjain026-cyber "SilphScope"


