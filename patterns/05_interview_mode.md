# Interview Mode — the protocol you run live

Knowing the pattern isn't the score. Running a clean, spoken protocol is. Practice
this on EVERY timed solve so it's automatic under pressure. Same protocol works for
a live interview and (silently) for an OA.

## The 5 phases (say the first four OUT LOUD)

### 1. CLARIFY (1–2 min) — before touching code
- Restate the problem in your own words; confirm with the interviewer.
- Ask about: input size / ranges, empty or single-element input, duplicates,
  negatives, sorted?, return value (index vs value vs count), ties.
- State assumptions explicitly: "I'll assume the input fits in memory and values are 32-bit."

### 2. PLAN + COMPLEXITY (3–5 min) — earn buy-in before coding
- Walk the **decision tree** (`03_decision_tree.md`) out loud: "It's a contiguous-
  substring-with-a-constraint problem, so I'm reaching for sliding window."
- State brute force + its complexity first, then your improved approach + target complexity.
- Get a nod ("does that approach sound reasonable?") BEFORE you code. This is where
  points are won — interviewers score approach and communication, not just a green submit.

### 3. CODE (15–20 min) — from your memorized template
- Start from the pattern's template (`01_template_bank.py`). Type the skeleton first.
- Narrate as you go: "dummy head to avoid the empty-list edge case…".
- Clean names, type hints, no premature optimization. If you get stuck, say what
  you're thinking — silence reads worse than a wrong turn you're reasoning through.

### 4. TEST (3–5 min) — walk your own code
- Dry-run the happy path aloud, tracing variables on a small input.
- Then hit the **4 categories** (this is the from-scratch discipline that impresses):
  1. Happy path (the example)
  2. Edge: empty / single element / all same
  3. Boundary: min/max constraint
  4. Tricky: negatives, duplicates, already/reverse sorted
- Fix bugs you find before the interviewer points them out.

### 5. OPTIMIZE / REFLECT (2 min)
- State final time/space. Name one improvement if asked ("could roll the DP to O(1) space").
- Mention a follow-up variation you'd handle.

---

## Timed-solve self-scorecard (fill after each practice solve)
```
Problem: ____________________   Pattern: ____________   Date: ______
[ ] Identified pattern in < 2 min
[ ] Stated brute force + target complexity before coding
[ ] Coded from template without looking it up
[ ] Tested all 4 categories, caught my own bugs
[ ] Finished medium in < 25 min (hard < 40 min)
Slowest phase: ______________   → drill that next.
```

## Common failure modes (and the fix)
| Failure | Fix |
|---|---|
| Jump straight to code | Force the CLARIFY + PLAN phases; they're scored. |
| Freeze on pattern ID | Fall back to brute force + the 3 questions (hash? sort? overlapping subproblems?). |
| Silent coding | Narrate every non-obvious line; interviewers can't score what they can't hear. |
| Skip tests | The 4-category walk is half your "senior" signal — never skip it. |
| Off-by-one / boundary bug | Pick ONE invariant per pattern and keep it (see each card's Trap). |

## Behavioral (don't neglect — 1 evening total)
Have 3 STAR stories ready (Situation, Task, Action, Result): a hard bug you fixed,
a conflict/teamwork moment, a project you're proud of. One evening to write, reuse everywhere.

## Mock cadence
Once Phase A (install) is done: 1 full mock per week (2 problems, 45 min, spoken
protocol, ideally with a peer or out loud to yourself + recording). The gap between
"can solve" and "can solve while talking" only closes by doing it live.
