1. 
git log --follow -p -- hideout_notes.txt

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


38b0356


2.

git log -S PASSCODE:
commit 38b0356f3bde68e1dbd5db797f45c9630b4b72ad
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Mon Sep 28 10:16:00 2026 +0530

    remove hideout notes

commit d9641b0d1f2c45e874024688f02d7e176c9cc26c
Author: Aryan Raj <aryanraj1092@gmail.com>
Date:   Wed Sep 23 12:41:00 2026 +0530

    add hideout notes

git checkout 38b0356f3bde68e1dbd5db797f45c9630b4b72ad^ hideout_notes.txt
Updated 1 path from 387fec1

cat hideout_notes.txt 
Rocket hideout, basement level
Guard rotation: every 4 hours
PASSCODE: SilphScope
Do not share outside the team.


PASSCODE is SilphScope

3.

git log --graph --oneline
* 9d1e163 (HEAD -> main, upstream/main, upstream/HEAD, origin/main, origin/HEAD) add hall of fame
* 1013d0c add hall of fame archive
* b012c9c add wild encounter
* cc96f2e add submissions folder
* 5318fd8 readme: note that answers are case-sensitive
* 973c23b add route 4 map
* 38b0356 remove hideout notes
* a41db4d add celadon gym
* 604ed8a fix typo in mewtwo notes
* bfb0600 update item list
* 65e0f66 [ROCKET-INTEL] shipment schedule for Silph Co.
* d9641b0 add hideout notes
* a25ce9a add gym leader list
* 640ca58 add mewtwo lab notes
* 88d9c7b initial commit

git log 65e0f66
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


commit: 65e0f66
author: Giovanni <giovanni@rocket.example>

4.

git blame -L 7,7 ./lab/mewtwo_notes.txt
604ed8a (Archer 2026-09-26 15:02:00 +0530 7) Subject escaped the containment tank.

author: Archer
commit: 604ed8a

https://github.com/ACM-IIT-Mandi/GitHero-2026/pull/22

badge: b8dc5890