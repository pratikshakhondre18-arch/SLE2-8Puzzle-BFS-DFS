# Empirical Performance Analysis of BFS and DFS for 8-Puzzle

## Course
02AML204 – Introduction to Artificial Intelligence

## Project Title
Empirical Performance Analysis of BFS and DFS for 8-Puzzle Problem

## 1. Introduction

This project compares the performance of two uninformed search algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)

Both algorithms are applied to the same 8-Puzzle problem. The program takes the initial state and goal state from the user and measures the execution time and number of states expanded.

The purpose of this project is to perform an empirical performance analysis using actual measured data.

## 2. Problem Description

The 8-Puzzle consists of a 3 × 3 board containing eight numbered tiles and one blank space.

The blank space is represented by `0`.

Example:

Initial State:

    7 2 4
    5 0 6
    8 3 1

Goal State:

    1 2 3
    4 5 6
    7 8 0

BFS and DFS use the same initial state and goal state so that the comparison is fair.

## 3. Algorithms Used

### Breadth First Search (BFS)

BFS explores the search space level by level. It uses a queue to store the states that need to be explored.

### Depth First Search (DFS)

DFS explores one path deeply before backtracking. It uses a stack to store the states that need to be explored.

## 4. Profiling Method

Python's `timeit` module was used to measure execution time.

Each algorithm was executed 3 times.

The average execution time was calculated from the three runs.

The number of states expanded was also counted manually by the program.

The same initial and goal states were given to both algorithms.

## 5. Experimental Input

Initial State:

    7 2 4 5 0 6 8 3 1

Goal State:

    1 2 3 4 5 6 7 8 0

The program also checks whether the given puzzle is solvable before running the algorithms.

## 6. Results

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time (ms) | 124.331 | 251.130 |
| States Expanded | 55,409 | 99,900 |
| Number of Runs | 3 | 3 |

### Individual Run Times

BFS:
Run 1: 127.568 ms
Run 2: 125.964 ms
Run 3: 119.461 ms

DFS:
Run 1: 224.701 ms
Run 2: 275.733 ms
Run 3: 252.957 ms
## 7. Analysis

For the tested 8-Puzzle input, BFS expanded 55,409 states, while DFS expanded 99,900 states.

The average execution time of BFS was 124.331 ms, whereas DFS took 251.130 ms on average.

In this experiment, BFS expanded fewer states and also had a lower measured execution time than DFS.

This result is specific to the tested initial and goal states. The performance of search algorithms can change depending on the problem state and search space.

The experimental results show how actual measurements can be used to compare algorithm performance instead of relying only on theoretical complexity.

## 8. Project Files

## 8. Project Files

- `bfs_8puzzle.py` – BFS implementation
- `dfs_8puzzle.py` – DFS implementation
- `compare.py` – Performance measurement and comparison
- `README.md` – Project documentation
- `AI_Contribution_Log.md` – AI contribution record

## 9. Conclusion

This project performed an empirical comparison of BFS and DFS using the 8-Puzzle problem.

For the tested input, BFS expanded fewer states and had a lower average execution time than DFS. The experiment demonstrates the importance of measuring actual algorithm performance using the same problem input and comparing the results using numerical data.