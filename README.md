# Data Structures Mini-Project, in Python

You will implement classic data structures from scratch. For each one, read the description, study the required API, then complete the starter code by replacing the `pass` stubs. Use the tests to guide your progress: they are initially marked with `xfail` (expected failure). As you finish each part, remove the related `xfail` markers so the tests must pass.

## How to Work
1. Pick one problem under `problems/`.
2. Open the file, implement one method at a time.
3. Run `pytest -k <structure>` to focus only that structure.
4. When a method works, remove the related `xfail` for its test.
5. After finishing, compare with the cheatsheet in `cheatsheets/` and the full solution in `solutions/`.

## Problems Overview
### 1. Binary Search Tree (`problems/binary_search_tree.py`)
Insert, search, traversals, height, balance, min/max. Focus: recursion & invariants.

### 2. Min Heap (`problems/min_heap.py`)
Array-backed heap: push, pop, peek, build, replace root. Focus: index math & percolation.

### 3. Trie / Prefix Tree (`problems/trie.py`)
Store a set of lowercase words. Operations:
- insert(word)
- contains(word) exact match
- starts_with(prefix) -> list of words starting with prefix (sorted)
- find_by_keyword(keyword) -> same as prefix search (ASSUMPTION: keyword means prefix)
- list_regex(pattern) -> words matching regex (sorted)
- delete(word) -> remove if present
Focus: recursive/iterative traversal, path sharing, search pruning.

Edge cases: empty string insertion, overlapping prefixes ("app" vs "apple"), deleting leaf vs branching word, regex matching anchors.

## Time Budget Suggestion
- Binary Search Tree: ~1.5–2h
- Min Heap: ~1–1.5h
- Trie: ~1–1.5h

## Stretch Ideas (Optional)
- BST: add level-order traversal and a method to rebalance.
- MinHeap: add decrease_key / merge.
- Trie: add wildcard search with `?` and `*`, implement substring search optimization.

## Running Tests
```bash
pytest -q
pytest -k binary_search_tree -q
pytest -k min_heap -q
pytest -k trie -q
```

Remove `@pytest.mark.xfail` decorators gradually to enforce correctness.

Good luck and have fun learning!
