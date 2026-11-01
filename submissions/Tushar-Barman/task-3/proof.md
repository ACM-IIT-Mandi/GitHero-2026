1.)A file called hideout_notes.txt was deleted at some point. Which commit deleted it?
Command:- git log
output:- commit 9d1e1639ea27f619a1a8d58a0c4601143fabd7b7 (HEAD -> main, upstream/main, upstream/HEAD, origin/main, origin/HEAD, task-3/Tushar-Barman)
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter

commit cc96f2e60e94174f3c7cf94bad03b15a4986cd63
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Thu Oct 1 13:37:00 2026 +0530

    add submissions folder

commit 5318fd84fa38ac0df014682e4fe578d5d4bffb0d
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 30 12:30:00 2026 +0530

    readme: note that answers are case-sensitive

commit 973c23b52e6469f6188f4ae0d08be8bc5e9dafe1
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Tue Sep 29 11:23:00 2026 +0530

    add route 4 map

commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

commit a41db4d0316b501d7ddae294db91a426f6806f4e
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Sun Sep 27 16:09:00 2026 +0530

    add celadon gym

:
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter

commit cc96f2e60e94174f3c7cf94bad03b15a4986cd63
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Thu Oct 1 13:37:00 2026 +0530

    add submissions folder

commit 5318fd84fa38ac0df014682e4fe578d5d4bffb0d
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 30 12:30:00 2026 +0530

    readme: note that answers are case-sensitive

commit 973c23b52e6469f6188f4ae0d08be8bc5e9dafe1
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Tue Sep 29 11:23:00 2026 +0530

    add route 4 map

commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

commit a41db4d0316b501d7ddae294db91a426f6806f4e
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Sun Sep 27 16:09:00 2026 +0530

    add celadon gym

:
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter
Answer:- commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad deleted it . Was done by aryan raj

2.) That file, before deletion, contained a line PASSCODE: <something>. What is the passcode?
Command :- git show 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Output:- commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
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

answer:- The Passcode is:- SilphScope

3.) Exactly one commit message contains the tag [ROCKET-INTEL]. Which commit is it, and who is its author?

Command:- git log
Output:- commit 9d1e1639ea27f619a1a8d58a0c4601143fabd7b7 (HEAD -> main, upstream/main, upstream/HEAD, origin/main, origin/HEAD, task-3/Tushar-Barman)
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter

commit cc96f2e60e94174f3c7cf94bad03b15a4986cd63
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Thu Oct 1 13:37:00 2026 +0530

    add submissions folder

commit 5318fd84fa38ac0df014682e4fe578d5d4bffb0d
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 30 12:30:00 2026 +0530

    readme: note that answers are case-sensitive

commit 973c23b52e6469f6188f4ae0d08be8bc5e9dafe1
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Tue Sep 29 11:23:00 2026 +0530

    add route 4 map

commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

commit a41db4d0316b501d7ddae294db91a426f6806f4e
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Sun Sep 27 16:09:00 2026 +0530

    add celadon gym

:
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter

commit cc96f2e60e94174f3c7cf94bad03b15a4986cd63
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Thu Oct 1 13:37:00 2026 +0530

    add submissions folder

commit 5318fd84fa38ac0df014682e4fe578d5d4bffb0d
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 30 12:30:00 2026 +0530

    readme: note that answers are case-sensitive

commit 973c23b52e6469f6188f4ae0d08be8bc5e9dafe1
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Tue Sep 29 11:23:00 2026 +0530

    add route 4 map

commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

commit a41db4d0316b501d7ddae294db91a426f6806f4e
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Sun Sep 27 16:09:00 2026 +0530

    add celadon gym

:
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter

commit cc96f2e60e94174f3c7cf94bad03b15a4986cd63
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Thu Oct 1 13:37:00 2026 +0530

    add submissions folder

commit 5318fd84fa38ac0df014682e4fe578d5d4bffb0d
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 30 12:30:00 2026 +0530

    readme: note that answers are case-sensitive

commit 973c23b52e6469f6188f4ae0d08be8bc5e9dafe1
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Tue Sep 29 11:23:00 2026 +0530

    add route 4 map

commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

commit a41db4d0316b501d7ddae294db91a426f6806f4e
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Sun Sep 27 16:09:00 2026 +0530

    add celadon gym

:
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter

commit cc96f2e60e94174f3c7cf94bad03b15a4986cd63
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Thu Oct 1 13:37:00 2026 +0530

    add submissions folder

:
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame

commit 1013d0c1100263b525272c39d60451c38cffc7cd
Author: Frozen-afk <0947farhanalam@gmail.com>
Date:   Wed Oct 7 09:33:04 2026 +0530

    add hall of fame archive

commit b012c9c841c84649543abc2e136365ef52802bae
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Oct 7 01:33:33 2026 +0530

    add wild encounter

commit cc96f2e60e94174f3c7cf94bad03b15a4986cd63
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Thu Oct 1 13:37:00 2026 +0530

    add submissions folder

commit 5318fd84fa38ac0df014682e4fe578d5d4bffb0d
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 30 12:30:00 2026 +0530

    readme: note that answers are case-sensitive

commit 973c23b52e6469f6188f4ae0d08be8bc5e9dafe1
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Tue Sep 29 11:23:00 2026 +0530

    add route 4 map

commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

commit a41db4d0316b501d7ddae294db91a426f6806f4e
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Sun Sep 27 16:09:00 2026 +0530

    add celadon gym

commit 604ed8abff6bf1c1aec7cf7c6deb3920c4e5d19f
Author: Archer <archer@rocket.example>
Date:   Sat Sep 26 15:02:00 2026 +0530

    fix typo in mewtwo notes

commit bfb060084a5f570563fba92b5fa78a2e0a00895d
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Fri Sep 25 14:55:00 2026 +0530

    update item list

commit 65e0f66a16c7e6a241edd4fab9b0d784a4ddd6ab
Author: Giovanni <giovanni@rocket.example>
Date:   Thu Sep 24 13:48:00 2026 +0530

    [ROCKET-INTEL] shipment schedule for Silph Co.

commit d9641b0d1f2c45e874024688f02d7e176c9cc26c
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 23 12:41:00 2026 +0530

    add hideout notes

commit a25ce9a81e7437b7ea195d5c34785f3e59a7eb3c
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Tue Sep 22 11:34:00 2026 +0530

    add gym leader list

commit 640ca58917c71b1608a832e37e6c1cb9a9bf89d2
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 21 10:27:00 2026 +0530

    add mewtwo lab notes

commit 88d9c7b54aea66348307beb608c89aa7df174fab
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Sun Sep 20 16:20:00 2026 +0530

    initial commit
Answer:- The commit is commit 65e0f66a16c7e6a241edd4fab9b0d784a4ddd6a and the author is Giovanni <giovanni@rocket.example>

4.) In lab/mewtwo_notes.txt, who last modified line 7, and in which commit?
command :- git blame lab/mewtwo_notes.txt
output:- 640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 1) Mewtwo notes - Cerulean Cave lab
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 2) Subject created from a fossil sample.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 3) Genetic splicing started at 02:00.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 4) Power readings are unstable.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 5) Containment field set to level 3.
604ed8ab (Archer    2026-09-26 15:02:00 +0530 6) Psychic output higher than any known subject, retested.
604ed8ab (Archer    2026-09-26 15:02:00 +0530 7) Subject escaped the containment tank.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 8) Tank rebuilt with reinforced glass.
640ca589 (Aryan Raj 2026-09-21 10:27:00 +0530 9) Observation continues.
answer:- commit :- 604ed8ab author :- archer

https://github.com/ACM-IIT-Mandi/GitHero-2026/pull/40

python badge.py Tushar-Barman "ilphScope"

