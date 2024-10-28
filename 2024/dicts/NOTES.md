
## Dictionaries

- The dictionary data structure type permits access to data items by
  content. You stick an item into a dictionary so you can find it when
  you need it.
- The primary operations of dictionary support are:
  - *Search(D, k)* - given a search key, _k_, return a pointer to the
    element in dictionary, _D_ whose key values is _k_, if one exists.
  - *Insert(D, x)* - given a data item _x_, add it to the set in the
    dictionary _D_.
  - *Delete(D, x)* - given a pointer to a given data item _x_ in the
    dictionary _D_, remove it from _D_.
  - *Max(D)* or *Min(D)* - retrieve the item with the largest (or
    smallest) key from _D_. This enables the dictionary to serve as
    a priority queue.
  - *Predecessor(D, k)* or *Successor(D, k)* - retrieve the item from
    _D_ whose key is immediately before (or after) _k_ in sorted order.
    These enables us to iterate through the elements of the data structure.
 
### Dictionary Implementations

1. Simple - arrays and linked lists
1. Binary search trees (BST)
1. Hash tables

**Problem:** whare ar ethe asymptotic worst-case running times for each
the seven fundamental dictionary operations (search, insert, delete,
successor, predecessor, minimum and maximum) when the data structure is
implemented as:

- an unsorted array
- a sorted array

The basic dictionary operations can be implemented with the following costs
on sorted and unsorted arrays, respectively.

Operation | Unsorted array | Sorted array
----------|:--------------- | :------------ |
Search(L, k) | O(n) | O(log n)
Insert(L, x) | O(1) | O(n)
Delete(L, x) | O(1)* | O(n)
Successor(L, x) | O(n) | O(1)
Predecessor(L, x) | O(n) | O(1)
Minimum(L) | O(n) | O(1)
Maximum(L) | O(n) | O(1)

- _Deletion_ is somewhat trickier, hence the *. The definition states
  that we are given a pointer _x_ to the element to delete, so we need
  not spend any time searching for the element. But removing the _xth_
  element from the array _A_ leaves a hole that must be filled. We
  could fill the hole by moving each of the elements _A[x+1]_ to
  _A[n]_ up one position, but this requires O(n) time when the first
  element is deleted.
  The following idea is better: just write over _A[x]_ with _A[n]_,
  and decrement _n_. This only takes constant time.

> *Take-Home Lesson*: Data structure design must balance all the different
> operations it supports. The fastest data stucture to support both
> operations A and B may well not be the fastest structure to support
> either operation A or B.

_Problem_: What is the asymptotic worst-case running times for each of the
seven fundamental dictionary operations when the data structure is implemented
as:

1. A singly-linked unosrted list
1. A doubly-linked unsorted list
1. A singly-linked sorted list
1. A doubly-linked sorted list

