# Data structures and algorithms
This repository contains the implementation of different popular data structures and algorithms written in Python and C++. Partially related to lectures from the KIT but also related to different coding challenges of different judges like [Leetcode](https://leetcode.com/), [Codeforces](https://codeforces.com/), ... The main purpose of this repository is to get hands-dirty with all of the popular data structures and algorithms and for coding experience.

<br />

# Algorithms

## Sorting algorithms
Algorithm | Python | C++
:------------ | :-------------| :-------------
Merge sort | :white_check_mark: | :x:
Quick sort | :white_check_mark: | :x:
Bubble sort | :white_check_mark: | :x:
Insertion sort | :white_check_mark: | :x:

## Search algorithms
### Shortest path
Algorithm | Python | C++
:------------ | :-------------| :-------------
Dijkstras algorithm | :x: | :x:
A-star | :x: | :x:
Bellman ford | :x: | :x:
### Minimum spanningtree
Algorithm | Python | C++
:------------ | :-------------| :-------------
Prims algorithm | :x: | :x:
Kruskal | :x: | :x:
### Depths first search
Algorithm | Python | C++
:------------ | :-------------| :-------------
DFS algorithm | :white_check_mark: | :x:
### Maximum flow/Minimum s-t cut
Algorithm | Python | C++
:------------ | :-------------| :-------------
Linear programming | :x: | :x:
Ford fulkerson | :x: | :x:
Dinitz algorithm | :x: | :x:
Preflow-push algorithm | :x: | :x:
### Matching
Algorithm | Python | C++
:------------ | :-------------| :-------------
Maximum matching | :x: | :x:
Maximum cardinality matching | :x: | :x:

## Randomized algorithms
Algorithm | Python | C++
:------------ | :-------------| :-------------
Sort checker (permutation characteristic)
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Polynom | :x: | :x:
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Hash table | :x: | :x:
Hashing
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Cuckoo hashing | :x: | :x:
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Blocked cuckoo hashing | :x: | :x:
Quick sort | :x: | :x:

## External algorithms
Algorithm | Python | C++
:------------ | :-------------| :-------------
Multiway merge | :x: | :x:
Semiexternal Kruskal | :x: | :x:

## Approximation algorithms
Algorithm | Python | C++
:------------ | :-------------| :-------------
List scheduling | :x: | :x:
Metrical traveling salesman problem | :x: | :x:
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Nearest addition algorithm | :x: | :x:
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Double tree algorithm | :x: | :x:
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Christofides algorithm | :x: | :x:
Knapsack
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Dynamic programming | :x: | :x:

## Fixed parameter algorithms
Algorithm | Python | C++
:------------ | :-------------| :-------------
Vertex cover | :x: | :x:

## Parallel algorithms
Algorithm | Python | C++
:------------ | :-------------| :-------------
Prefix sum | :x: | :x:
Parallel quicksort | :x: | :x:
Parallel multiway mergesort | :x: | :x:

## Geometric algorithms
Algorithm | Python | C++
:------------ | :-------------| :-------------

<br />

# Data structures

## Priority queues
Datastruct | Python | C++
:------------ | :-------------| :-------------
Binary heap | :white_check_mark: | :x:
Binomial heap | :x: | :x:
External priority queue | :x: | :x:
Pairing heap | :x: | :x:
Fibonacci heap | :x: | :x:
Bucket queue | :x: | :x:
Radix heap | :x: | :x:

## Search trees
Datastruct | Python | C++
:------------ | :-------------| :-------------
Binary search tree | :x: | :x:
External search tree | :x: | :x:

## [Legend](https://gist.github.com/rxaviers/7360908)
- :white_check_mark: Finished
- :warning: Fix needed
- :x: Todo

</br>

# Testing
To start the tests make sure you are in root dir and then execute
```
python -m pytest tests
```
