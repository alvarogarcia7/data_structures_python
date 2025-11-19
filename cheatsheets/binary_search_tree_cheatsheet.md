# Binary Search Tree Cheatsheet

Operations & Complexity (average / worst)
- insert: O(log n) / O(n)
- search: O(log n) / O(n)
- delete: O(log n) / O(n)
- inorder: O(n)
- height: O(n)
- is_balanced: O(n)
- find_min/find_max: O(log n) / O(n)

Delete Cases
1. Leaf: remove directly.
2. One child: replace node by child.
3. Two children: copy inorder successor's value, delete successor.

Balance Check Pattern: post-order recursion returning (balanced, height).


