# Binary Tree
### Types
#### 1. Full Binary Tree
Every node has either zero or two children.</br>
Nodes with a degree of 0(has zero child) are on the same level(last level).</br>
#### 2. Complete Binary Tree
All levels are fully filled except possibly for the last level</br>
Last level is filled from left to right!</br>
#### 3. Binary Search Tree (BST)
For every node:<br/>
Left subtree contains values smaller than the node's value</br>
Right subtree contains values greater than the node's value</br>
#### 4. Balanced Binary Search Tree
#####   i. AVL Tree
Self-balancing binary search tree---height difference between the left and right subtrees of any node is no more than 1.</br>
搜索、插入、删除的时间复杂度为 O(log n)
#####   ii. Red-Black Tree
### Storage methods
1. **Linked Representation (or Pointer-based Representation)**: Each node in the tree has pointers to its left and right children, along with the node's value.
2. **Array Representation**: The binary tree is stored in a single array where:
   - The root is at index 0.
   - The left child of a node at index `i` is stored at index `2i + 1`.
   - The right child of a node at index `2i + 2`.
### Traversal methods
#### Depth-First Search (DFS): -- use of stack
1. **Pre-order traversal**: ROOT --> LEFT --> RIGHT
2. **In-order traversal**: LEFT --> ROOT --> RIGHT
3. **Post-order traversal**: LEFT --> RIGHT --> ROOT

#### Breadth-First Search (BFS): -- use of queue
1. **Level-order traversal**: LEVEL by LEVEL from TOP to BOTTOM, visiting all nodes at each level from LEFT to RIGHT.
