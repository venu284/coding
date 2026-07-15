# Drill Schedule — front-load the grip, then repetition makes it obvious

Your model: *familiarize the patterns fast, then repetition makes them obvious.*
This schedule does exactly that — a heavy front-load to install all 19 patterns,
then a light spaced-repetition loop you can run indefinitely while you apply for
jobs, so you're always interview/OA-ready.

Pace is flexible (you have ~6 months, but want to be ready for any surprise OA).
Two tracks — pick by how much time you have per day.

---

## Phase A — INSTALL (front-load, ~2–3 weeks)
Goal: every one of the 38 anchors is blind-codeable and every pattern is recognizable.

**Aggressive (3–4 hrs/day → ~12 days) or Steady (1.5–2 hrs/day → ~3 weeks).**

Each day = **2 patterns**. Per pattern:
1. Read its card (`00_pattern_cards.md`) — Trigger, Why, Trap. (5 min)
2. Type its template from `01_template_bank.py` into a blank file, from memory. (10 min)
3. Solve both anchors from scratch, log each in a problem folder. (60–90 min)
4. Add the pattern to your recall deck (see Phase B). (2 min)

| Day | Patterns (2/day) |
|---|---|
| 1 | Hashing · Two Pointers |
| 2 | Sliding Window · Binary Search |
| 3 | Stack/Monotonic · Linked List |
| 4 | Tree DFS · Tree BFS |
| 5 | Trie · Heap |
| 6 | Backtracking · Graph BFS/DFS |
| 7 | Topological Sort · Union-Find |
| 8 | DP 1D · DP 2D |
| 9 | Intervals · Greedy |
| 10 | Bit Manipulation · **catch-up / weakest pattern** |

Steady track: same table, ~1.5 patterns/day, finishes in ~3 weeks. Don't skip the
"type template from memory" step — that's where the grip forms.

---

## Phase B — REPETITION (indefinite, ~30–45 min/day)
This is the "repetition makes it obvious" engine. Run it every day after Phase A,
right up to and between interviews.

**Active recall deck (the core habit).** For each of the 19 patterns, a card with:
- Front: the **Trigger** line only.
- Back: pattern name + template shape + complexity.
Review with spaced repetition (paper/Anki/notes — any tool). Rule: if you can't
say the template shape in 15 sec, re-drill that pattern's anchor tomorrow.

**Daily 30–45 min loop:**
1. **Recall pass (10 min):** flip through today's due cards; for any you blank on,
   re-type the template from memory.
2. **One timed solve (20–30 min):** a NEW problem (an "extra" from
   `02_anchor_problems.md`, or a random LeetCode medium). Use the interview
   protocol (`05_interview_mode.md`): pattern-ID out loud → complexity → code → test.
3. **Log the trigger (2 min):** one line — "Problem X → Pattern Y because Z".

**Spaced-repetition interval per anchor** (re-solve from scratch on these days after first solving):
Day 1 → Day 3 → Day 7 → Day 21. If you nail Day 21 blind, it's installed; retire it
to occasional review. If you fumble any checkpoint, reset that anchor to Day 1.

---

## Phase C — PRESSURE (rolling, whenever an OA/interview is near)
When a real OA or interview appears, switch the daily solve to this for ~1 week:
- 2 problems back-to-back, 25 min each, NO topic label — you identify the pattern.
- Alternate: 1 medium you've never seen + 1 re-solve of a weak anchor.
- After each: did you ID the pattern in <2 min? If no, that pattern goes back to Phase B Day 1.
- Add 2–3 "design-y" reps (LRU Cache, Min Stack) — they show up in OAs and phone screens.

---

## The one-page weekly rhythm (steady state)
- **Mon–Fri:** Phase B daily loop (recall + 1 timed solve + log). 30–45 min.
- **Sat:** 3 timed solves, mixed patterns, no labels. Review the week's trigger log.
- **Sun:** re-solve the 2–3 anchors you were slowest on. Rest is allowed.

## Progress tracker (fill as you go)
```
Pattern              Anchor1  Anchor2  Recall<15s  Timed<25m
Hashing              [ ]      [ ]      [ ]         [ ]
Two Pointers         [ ]      [ ]      [ ]         [ ]
Sliding Window       [ ]      [ ]      [ ]         [ ]
Binary Search        [ ]      [ ]      [ ]         [ ]
Stack/Monotonic      [ ]      [ ]      [ ]         [ ]
Linked List          [ ]      [ ]      [ ]         [ ]
Tree DFS             [ ]      [ ]      [ ]         [ ]
Tree BFS             [ ]      [ ]      [ ]         [ ]
Trie                 [ ]      [ ]      [ ]         [ ]
Heap                 [ ]      [ ]      [ ]         [ ]
Backtracking         [ ]      [ ]      [ ]         [ ]
Graph BFS/DFS        [ ]      [ ]      [ ]         [ ]
Topological Sort     [ ]      [ ]      [ ]         [ ]
Union-Find           [ ]      [ ]      [ ]         [ ]
DP 1D                [ ]      [ ]      [ ]         [ ]
DP 2D                [ ]      [ ]      [ ]         [ ]
Intervals            [ ]      [ ]      [ ]         [ ]
Greedy               [ ]      [ ]      [ ]         [ ]
Bit Manipulation     [ ]      [ ]      [ ]         [ ]
```
All four columns checked across all rows = interview-ready. Keep Phase B running after that.
