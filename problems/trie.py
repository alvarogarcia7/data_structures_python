"""Trie (Prefix Tree) starter code.

Stores a collection of lowercase words (assume a–z only; tests include empty string). Shared prefixes stored once.

Methods to implement:
- insert(word: str) -> None
- contains(word: str) -> bool                 Exact word match
- starts_with(prefix: str) -> list[str]       All words beginning with prefix (sorted)
- find_by_keyword(keyword: str) -> list[str]  Alias for starts_with (ASSUMPTION: keyword means prefix)
- list_regex(pattern: str) -> list[str]       All words matching regex pattern (sorted)
- delete(word: str) -> bool                   Remove word if present

Helper ideas:
- _collect(node, prefix, out)
- delete uses post-order recursion returning prune signal.

Edge cases:
- Empty string insertion & lookup.
- "app" vs "apple" (word that is prefix of another).
- Deleting leaf vs branching word.
- Regex patterns examples:
  '^a.*' starts with a
  '.*tion$' ends with 'tion'
  '^[aeiou]{2}.*' two vowels start
  '^$' matches empty string exactly

Replace all pass statements with working code when implementing.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class _TrieNode:
    children: Dict[str, '_TrieNode'] = field(default_factory=dict)
    is_word: bool = False


class Trie:
    def __init__(self) -> None:
        self._root = _TrieNode()
        self._size = 0

    def insert(self, word: str) -> None:
        pass  # TODO: implement

    def contains(self, word: str) -> bool:  # type: ignore
        pass  # TODO: implement

    def starts_with(self, prefix: str) -> List[str]:  # type: ignore
        pass  # TODO: implement

    def find_by_keyword(self, keyword: str) -> List[str]:  # type: ignore
        pass  # TODO: implement

    def list_regex(self, pattern: str) -> List[str]:  # type: ignore
        pass  # TODO: implement

    def delete(self, word: str) -> bool:  # type: ignore
        pass  # TODO: implement

    def __len__(self) -> int:  # pragma: no cover - trivial
        return self._size
