# concepts/ Folder Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `concepts/` sibling folder as a layered DSA learning, practice, and interview-revision system.

**Architecture:** The folder is documentation-first, with top-level navigation files for quick revision and curriculum flow, plus focused deep-note pages grouped by foundations, data structures, algorithms, techniques, and advanced topics. A runnable Python template bank provides executable examples and built-in assertions.

**Tech Stack:** Markdown documentation, Python 3 standard library, existing repository conventions.

---

## File Structure

- Create `concepts/README.md` as the entry point and usage guide.
- Create `concepts/00_quick_revision_cards.md` for compact interview cards.
- Create `concepts/01_learning_path.md` for curriculum-first study order.
- Create `concepts/02_concept_index.md` for lookup across every concept.
- Create `concepts/03_template_bank.py` for runnable Python templates.
- Create `concepts/04_decision_tables.md` for data-structure and algorithm selection.
- Create `concepts/05_practice_map.md` for anchors, extras, and drills.
- Create `concepts/06_interview_revision.md` for last-week and same-day review.
- Create deep-note files under `concepts/foundations/`, `concepts/data-structures/`, `concepts/algorithms/`, `concepts/techniques/`, and `concepts/advanced/`.
- Modify root `README.md` to link to `concepts/` beside `patterns/` and `DSA_Plan.md`.

### Task 1: Create Folder Skeleton And Plan Commit

**Files:**
- Create: `docs/superpowers/plans/2026-07-28-concepts-folder.md`
- Create directories under `concepts/`

- [ ] **Step 1: Save this implementation plan**

Use the exact plan file path above.

- [ ] **Step 2: Create directories**

Run:

```bash
mkdir -p concepts/foundations concepts/data-structures concepts/algorithms concepts/techniques concepts/advanced
```

Expected: command exits with code 0.

### Task 2: Add Top-Level Learning System Files

**Files:**
- Create: `concepts/README.md`
- Create: `concepts/00_quick_revision_cards.md`
- Create: `concepts/01_learning_path.md`
- Create: `concepts/02_concept_index.md`
- Create: `concepts/04_decision_tables.md`
- Create: `concepts/05_practice_map.md`
- Create: `concepts/06_interview_revision.md`

- [ ] **Step 1: Write `README.md`**

Include purpose, read order, daily workflow, and relationship to `patterns/`.

- [ ] **Step 2: Write quick cards**

Cover all approved topics with trigger, core idea, complexity, template, anchor,
and trap.

- [ ] **Step 3: Write learning path, concept index, decision tables, practice map, and interview revision**

Use the approved topic map and keep links relative to `concepts/`.

### Task 3: Add Template Bank With Test-First Verification

**Files:**
- Create: `concepts/03_template_bank.py`

- [ ] **Step 1: Write a failing template-bank test harness**

Create the file with `_run_tests()` calling the intended public template functions
before the functions exist.

- [ ] **Step 2: Run the file and verify RED**

Run:

```bash
python3 concepts/03_template_bank.py
```

Expected: failure because at least one template function is not defined.

- [ ] **Step 3: Implement the template functions and data structures**

Include practical templates for hashing, prefix sums, binary search, linked lists,
tree traversal, heap, union-find, graph traversal, topological sort, backtracking,
dynamic programming, greedy, bit manipulation, trie, segment tree, and Fenwick tree.

- [ ] **Step 4: Run the file and verify GREEN**

Run:

```bash
python3 concepts/03_template_bank.py
```

Expected output:

```text
ALL CONCEPT TEMPLATES PASS
```

### Task 4: Add Deep Concept Notes

**Files:**
- Create every approved deep-note file under `concepts/foundations/`
- Create every approved deep-note file under `concepts/data-structures/`
- Create every approved deep-note file under `concepts/algorithms/`
- Create every approved deep-note file under `concepts/techniques/`
- Create every approved deep-note file under `concepts/advanced/`

- [ ] **Step 1: Add foundations notes**

Create pages for Big-O, recursion, iteration and invariants, math for DSA,
Python DSA toolkit, and testing edge cases.

- [ ] **Step 2: Add data-structure notes**

Create pages for arrays and strings, hash maps and sets, stacks and queues,
linked lists, trees and BSTs, heaps, graphs, tries, union-find, and intervals.

- [ ] **Step 3: Add algorithm notes**

Create pages for sorting, binary search, tree traversals, graph traversals,
topological sort, shortest paths, MST, dynamic programming, greedy, and bit
manipulation.

- [ ] **Step 4: Add technique notes**

Create pages for two pointers, sliding window, prefix sums, monotonic stack and
queue, backtracking, divide and conquer, sweep line, fast/slow pointers, and
search on answer.

- [ ] **Step 5: Add advanced notes**

Create pages for segment tree, Fenwick tree, advanced graphs, advanced DP,
string algorithms, and system-design DSA.

### Task 5: Wire Root README And Verify

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add `concepts/` to the Study system section**

Add `concepts/` as the deep learning and interview-revision system.

- [ ] **Step 2: Run template bank**

Run:

```bash
python3 concepts/03_template_bank.py
```

Expected output:

```text
ALL CONCEPT TEMPLATES PASS
```

- [ ] **Step 3: Check Markdown links and expected files**

Use shell checks to confirm all expected concept files exist and obvious relative
links resolve.

- [ ] **Step 4: Check git status**

Run:

```bash
git status --short
```

Expected: only the new plan, the new `concepts/` files, and root `README.md` are
modified or untracked.

### Task 6: Commit Implementation

**Files:**
- All created `concepts/` files
- `README.md`
- `docs/superpowers/plans/2026-07-28-concepts-folder.md`

- [ ] **Step 1: Stage only relevant files**

Run:

```bash
git add README.md concepts docs/superpowers/plans/2026-07-28-concepts-folder.md
```

- [ ] **Step 2: Commit**

Run:

```bash
git commit -m "Add DSA concepts learning system"
```

Expected: commit succeeds.

## Self-Review

Spec coverage:

- New sibling folder `concepts/`: covered by Tasks 1-4.
- Layered quick, deep, and practice modes: covered by Tasks 2 and 4.
- Curriculum-first path: covered by `01_learning_path.md` in Task 2.
- Runnable template bank: covered by Task 3.
- Root README link: covered by Task 5.
- Verification and commit: covered by Tasks 5-6.

Placeholder scan: no TBD, TODO, FIXME, or unspecified task remains.
