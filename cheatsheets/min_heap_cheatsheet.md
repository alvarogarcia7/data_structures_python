# Min Heap Cheatsheet

Representation: Array where children indices = 2*i+1, 2*i+2; parent = (i-1)//2.

Operations & Complexity
- push: O(log n)
- peek: O(1)
- pop: O(log n)
- build_heap: O(n)
- replace_root: O(log n)

Pop Steps:
1. Save root.
2. Move last element to index 0.
3. Heapify down.
4. Return saved root.

Replace Root:
1. Save old root.
2. Put new value at index 0.
3. Heapify down.
4. Return old root.

