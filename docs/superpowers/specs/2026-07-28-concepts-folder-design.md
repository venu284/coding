# concepts/ Folder Design

## Goal

Create a new sibling folder named `concepts/` for broad DSA learning and interview
revision. It should complement `patterns/`, not replace it:

- `patterns/` remains the fast pattern-first speedrun.
- `concepts/` becomes the deeper concept-first system for techniques, data
  structures, algorithms, explanations, templates, practice mapping, and revision.

The folder must support three modes:

1. Deep learning from fundamentals through advanced topics.
2. Quick interview revision from compact cards and decision tables.
3. Practice through anchor problems, extra problems, edge cases, and interview prompts.

## Top-Level Structure

```text
concepts/
├── README.md
├── 00_quick_revision_cards.md
├── 01_learning_path.md
├── 02_concept_index.md
├── 03_template_bank.py
├── 04_decision_tables.md
├── 05_practice_map.md
├── 06_interview_revision.md
├── foundations/
├── data-structures/
├── algorithms/
├── techniques/
└── advanced/
```

## File Responsibilities

`README.md` explains the purpose of `concepts/`, how it relates to `patterns/`,
and which file to use depending on whether the learner is studying, revising, or
practicing.

`00_quick_revision_cards.md` provides compact cards for every major concept:
trigger, use case, template shape, complexity, anchor problem, and common trap.

`01_learning_path.md` defines the curriculum order. It starts with foundations,
then core data structures, core algorithms, common techniques, and advanced topics.

`02_concept_index.md` is the complete lookup table. It maps every concept to its
category, deep-note file, template name, related patterns, and practice problems.

`03_template_bank.py` contains runnable Python skeletons and small correctness
checks for core data structures, algorithms, and techniques.

`04_decision_tables.md` helps choose the right data structure, algorithm, or
technique based on input type, constraints, target complexity, and trigger words.

`05_practice_map.md` maps each concept to anchor problems, extra problems,
drills, and suggested solve order.

`06_interview_revision.md` is the condensed final-review guide for last-week,
day-before, and same-day interview prep.

## Topic Map

```text
foundations/
├── 01_big_o.md
├── 02_recursion.md
├── 03_iteration_and_invariants.md
├── 04_math_for_dsa.md
├── 05_python_dsa_toolkit.md
└── 06_testing_edge_cases.md

data-structures/
├── 01_arrays_and_strings.md
├── 02_hash_maps_and_sets.md
├── 03_stacks_and_queues.md
├── 04_linked_lists.md
├── 05_trees_and_bsts.md
├── 06_heaps_priority_queues.md
├── 07_graphs.md
├── 08_tries.md
├── 09_union_find.md
└── 10_intervals.md

algorithms/
├── 01_sorting.md
├── 02_binary_search.md
├── 03_tree_traversals.md
├── 04_graph_traversals.md
├── 05_topological_sort.md
├── 06_shortest_paths.md
├── 07_minimum_spanning_tree.md
├── 08_dynamic_programming.md
├── 09_greedy.md
└── 10_bit_manipulation.md

techniques/
├── 01_two_pointers.md
├── 02_sliding_window.md
├── 03_prefix_sums.md
├── 04_monotonic_stack_queue.md
├── 05_backtracking.md
├── 06_divide_and_conquer.md
├── 07_sweep_line.md
├── 08_fast_slow_pointers.md
└── 09_search_on_answer.md

advanced/
├── 01_segment_tree.md
├── 02_fenwick_tree.md
├── 03_advanced_graphs.md
├── 04_advanced_dynamic_programming.md
├── 05_string_algorithms.md
└── 06_system_design_dsa.md
```

## Standard Page Format

Every deep-note page should use the same format so the folder is easy to scan:

1. `# Concept Name`
2. `## Quick Revision`
   - When to use it
   - Core idea
   - Complexity
   - Template name in `../03_template_bank.py`
   - Common trap
3. `## Mental Model`
4. `## How It Works`
5. `## Python Template`
6. `## Walkthrough`
7. `## Edge Cases`
8. `## Common Mistakes`
9. `## Practice`
   - Anchor problems
   - Extra problems
   - Interview prompts
10. `## Related Concepts`

## Content Style

The writing should be practical and interview-focused:

- Explain why the concept works, not only how to code it.
- Use compact examples that can be followed without external diagrams.
- Keep quick revision short enough to review under pressure.
- Include complexity in every concept page.
- Include traps and hidden-test edge cases.
- Prefer Python examples consistent with the rest of the repository.

## Relationship To Existing Files

`patterns/` remains unchanged and continues to be the primary fast-track pattern
system. `concepts/` can reference `patterns/` when useful, especially where a
concept overlaps with a pattern, such as sliding window, binary search, heap,
union-find, dynamic programming, and graph traversal.

`DSA_Plan.md` remains the long-track reference. The new `concepts/01_learning_path.md`
should be usable independently but can align with the existing long-track order.

## Implementation Notes

The first implementation pass should create the complete folder structure and the
core overview files. Deep-note pages can be filled with useful initial content,
but the priority is a coherent learning system rather than exhaustive textbook
coverage in one pass.

`03_template_bank.py` should be runnable with:

```bash
python3 concepts/03_template_bank.py
```

The expected success output should be:

```text
ALL CONCEPT TEMPLATES PASS
```

## Verification

After implementation:

1. Run `python3 concepts/03_template_bank.py`.
2. Check all Markdown links that point within `concepts/`.
3. Confirm the top-level `README.md` links to `concepts/`.
4. Confirm no existing user changes, especially `DSA_Plan.md`, were overwritten.
