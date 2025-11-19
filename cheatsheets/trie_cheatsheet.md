# Trie Cheatsheet

Operations & Complexity (n = word length, k = number of words under prefix)
- insert: O(n)
- contains: O(n)
- starts_with: O(p + k * avg_word_len_under_prefix)
- find_by_keyword: same as starts_with
- list_regex: O(T + R) where T = total chars across stored words, R = regex matching cost
- delete: O(n)

Patterns
- Node structure: dict children + is_word flag.
- Insert: create nodes via `setdefault`.
- Collect words: DFS accumulating prefix when `is_word` True.
- Delete: recursive post-order; prune child dict entries when they become leaf & not a word.

Edge Cases
- Empty string as word: root `is_word` True.
- Word is prefix of another: never prune if `is_word` True.
- Deleting non-existent word: return False, no structural change.

Regex Matching
- Compile pattern: `regex = re.compile(pattern)`
- Filter collected words with `regex.fullmatch(word)`.

