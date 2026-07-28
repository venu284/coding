# Tries

## Quick Revision

- **When to use it:** prefix lookup, dictionary words, autocomplete, wildcard search.
- **Core idea:** shared prefixes are stored once.
- **Complexity:** O(L) insert/search for word length L.
- **Template:** `Trie`.
- **Common trap:** forgetting explicit word-end marker.

## Mental Model

A trie is a tree of characters. Reaching a node means the prefix exists; seeing an
end marker means a full word exists.

## How It Works

Each node maps character -> next node. Insert walks or creates nodes. Search walks
existing nodes and checks the end marker.

## Python Template

```python
node = root
for ch in word:
    node = node.setdefault(ch, {})
node["$"] = True
```

See `Trie` in `../03_template_bank.py`.

## Walkthrough

After inserting `apple`, `starts_with("app")` is true because the prefix path
exists. `search("app")` is false until `app` itself is inserted.

## Edge Cases

- Empty string if allowed.
- Word that is prefix of another word.
- Duplicate insert.
- Wildcard search requires DFS.

## Common Mistakes

- Confusing prefix existence with word existence.
- Using a set of words when prefix queries need trie performance.
- Not pruning board-search DFS.

## Practice

- **Anchor problems:** Implement Trie, Design Add and Search Words.
- **Extra problems:** Word Search II, Replace Words.
- **Interview prompt:** "Do shared prefixes matter?"

## Related Concepts

- `../advanced/05_string_algorithms.md`
- `../techniques/05_backtracking.md`
