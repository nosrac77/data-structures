# Data-Structures

[![Build Status](https://travis-ci.org/nosrac77/data-structures.svg?branch=trie-traveral)](https://travis-ci.org/nosrac77/data-structures)

**Authors**: Chelsea Dole and Carson Newton


**Resources**: Pytest, pytest-cov, tox, and timeit were all used to make/test the following data structures.

## Data Structures:

* **Singly Linked List** — a data structure comprised of nodes with pointers. The pointer of each node directs towards the next node down the list. Each node has only a single link to another node.

* **Doubly Linked List** - a data structure, like a Singly Linked List, comprised of nodes with pointers. Like the SLL, each node has pointers, however they have two pointers: one pointing to the next node (towards the tail) and one pointing towards the previous node (towards the head). Each node has two links to other nodes.

* **Stack** - a "stacked" data structure which uses the "last in, first out" method to store nodes. It inherits from the Singly Linked List.

* **Queue** - a list/"queue" of nodes. All nodes enter from one side, and exit from the other. Nodes point in only one direction.

* **Deque** - a list/"queue" of nodes. Similar to a queue, except not all nodes enter from one side and exit from the other. Nodes can be entered and/or removed from either side of the deque.

* **Binary Heap** - a binary tree where values are sorted. How the heap is sorted is dependent upon the type of heap. A max heap sorts values from highest to lowest, and min heap does the opposite. Values are added to the bottom, or next open space, and removed from the top.

* **Graph** - an unordered graph of nodes, connected to each other with pointers (or "edges") that aim in one direction. Non-traversible.

* **Weighted Graph** - A graph (as described above) with weighted edges assigned at edge creation. Traversible using depth-first or breadth-first methods.

* **Binary Search Tree** - A binary search tree containing nodes. Each node has a value, which is currently set up to hold integers, and also left and right attributes. Nodes are sorted upon insertion. Each node is inserted according to it's value compared to the other nodes in the tree.

## Time Complexities:


* .push() *The time complexity for this method is O(1), because because push always pushes in from the front, and therefore will always take the same amount of time to complete.*

* .pop() *The time complexity for this method is O(1), because pop exclusively removes from the front of the data structure — meaning that it always takes the same amount of time to complete.*

* .append() *The time complexity for this method is O(1), because you're always adding to the end of the data structure, so the time of operation will not change regardless of data structure size.*

* .size()/.len() *The time complexity for this method is O(1), because it is calculated by initializing a counter at 0, and adding/subtracting with various functions. Therefore, all .size does is return the current counter value, not iterate over the data structure.*

* .search(val) *The time complexity for this method is O(n), because the larger the data structure, the longer it takes to search through it for your value. Worst case scenario, it's the last element. Best case, it's the 1st. Therefore, it's O(n).*

* .remove(val) *The time complexity for the remove method is O(n), because the larger the data structure, the longer it takes to search through it. The length is not static, and depends on if you're removing the first item, or the last item. Therefore, it's O(n).*

* .display() *The time complexity for the display method is O(n), because the number of iterations display will do over the while loop depends on the size of the data structure. Therefore, because the time depends on size of structure, and is O(n).*

* .enqueue(val) *The time complexity for the enqueue method is O(1), because it always adds a single value to the end of the queue data structure, and doesn't loop through anything. (Essentially the same as .append.)*

* .dequeue() *The time complexity for dequeue is O(1), because it always removes one value off the front of the queue, and nowhere else. Therefore, no matter the queue size, it will take a static amount of time. (Essentially the same as .pop.)*

* .peek() *The time complexity for peek is O(1) because it always prints only the value of the first item in the queue. No matter how large the queue, it will always print only that. Due to this, it takes a static amount of time and is O(1).*

* .append_left() *The time complexity for append_left() is O(1) because you're always adding to the front of the data structure, so the time of operation will not change regardless of data structure size.*

* .peek_left() *The time complexity for peek_left is O(1) because it always prints only the value of the first item in the deque. No matter how large the deque, it will always print only that. Due to this, it takes a static amount of time and is O(1).*

* .append_left() *The time complexity for this method is O(1), because you're always adding to the front of the data structure, so the time of operation will not change regardless of data structure size.*

* .nodes() *The time complexity of this method is O(n), because the runtime will depend on the size of n.*

* .edges() *The time complexity of this method is O(n), because the time that the .edges() method takes up will depend on the size of n.*

* .add_node() *The time complexity of this is O(1), because every time the method is just appending to a list, so it'll take the same amount of time every time.*

* .add_edge() *The time complexity of this is O(n), because the for loop's length will depend on the size of n — so its time scales.*

* .del_node() *The time complexity of this is O(n), because how many nodes you have to serach through depends on the size of n. Though there are nested for loops, you're only running the second loop once, so it's not O(n^2).*

* .del_edge() *The time complexity is O(n), because the 'in' operator iterates through all nodes, so it depends on the size of n.*

* .has_node() *The time complexity is O(n), because the function runs through and compares every node in self.all_nodes to val — so runtime depends on the size of n.*

* .neighbors() *The time complexity is O(n), because the function iteratrates through all nodes on the graph.*

* .adjacent() *The time complexity is O(n), because the function runs through all edges in self.all_edges, and the number of edges depends on n size.*

* .breadth_first_traversal() *The time complexity is O(n^2), because is has a nested for loop, so the runtime will grow exponentially based on the size of n.*

* .depth_first_traversal() *The time complexity is O(n), because the runtime gets longer as n gets bigger.*

**Binary Search Tree Methods:**

* .insert() *The time complexity of this method is, at it's best, O(log n), and at it's worst, 0(n). These differences depend entirely on the tree structure.*

* .search() *The time complexity of this method is 0(n) because it checks the value given against every node in the tree using a for loop.*

* .size() *The time complexity of this method is 0(1) because it just returns the length of a list.*

* .contains() *The time complexity of this method is 0(k) at best and O(n) at worst because it checks the value given against an entire list of values.*

* .depth() *The time complexity of this method is, at it's worst, 0(n), and at it's best, 0(1), depending on the size of the tree.*

* .balance() *The time complexity of this method is, at it's worst, 0(n), and at it's best, 0(1), depending on the size of the tree.*

* .pre_order() *The time complexity of this method is O(n), because it requires every node in the binary search tree to get recursively called before the generator can yield the correct pre-order values. As a side note, this method calls upon a helper function, _pre_order_traversal, in order to accomplish it's task. The aforementioned time complexity takes into account the time complexity of both functions.*

* .post_order() *The time complexity of this method is O(n), because it requires every node in the binary search tree to get recursively called before the generator can yield the correct post-order values. As a side note, this method calls upon a helper function, _post_order_traversal, in order to accomplish it's task. The aforementioned time complexity takes into account the time complexity of both functions.*

* .in_order() *The time complexity of this method is O(n), because it requires every node in the binary search tree to get recursively called before the generator can yield the correct in-order values. As a side note, this method calls upon a helper function, _in_order_traversal, in order to accomplish it's task. The aforementioned time complexity takes into account the time complexity of both functions.*

* .breadth_first() *The time complexity of this method is O(n^2), because it requires every node in the binary search tree to get iterated over while also iterating over that node's children before the generator can yield the correct breadth-first values. As a side note, this method calls upon two helper functions, _breadth_first_traversal and _get_children, in order to accomplish it's task. The aforementioned time complexity takes into account the time complexity of all three functions.*

**Trie Table Methods:**

* .insert() *The time complexity of this method is at it's worst, 0(n). In the case that the same word is being inserted twice in a row, this method will call the contains method, which would at that point iterate over the entire tree before telling the insert method to do an empty return. Also, if the insert is being performed for the first time, it must technically iterate over the entire tree to add all letters of the given word.*

* .contains() *The time complexity of this method is, at it's worst, 0(n). In the case that the tree only has one word, and contains is called using that word, the method must technically iterate over every node in the tree before returning True.*

* .size() *The time complexity of this method is, at it's worst, 0(1). This is because the method only returns the integer contained in the trees _size attribute.*

* .remove() *The time complexity of this method is, at it's worst, 0(n). In the case that the tree only has one word, and the method is called on that word, the method must technically iterate over every node in the tree before accomplishing it's task.*

* .traversal() *The time complexity of this method is, at worst, O(n). This is because, if start value given is an empty string, the method will traverse over the entire table to build the initial list from which to yield from.*
