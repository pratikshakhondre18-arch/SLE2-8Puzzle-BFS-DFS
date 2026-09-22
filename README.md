# Empirical Performance Analysis of BFS and DFS for 8-Puzzle

## Course
02AML204 – Introduction to Artificial Intelligence

## Project Title
Empirical Performance Analysis of BFS and DFS for 8-Puzzle Problem

## 1. Introduction

This project performs an empirical performance analysis of two uninformed search algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)

Both algorithms are applied to the 8-Puzzle problem.

The same initial state and goal state are given to BFS and DFS for each test case so that the comparison is fair.

The experiment measures:

- Execution time
- Average execution time
- States expanded
- Function-level profiling using py-spy

Three selected test cases were used:

- Best Case
- Average Case
- Worst Case

## 2. Problem Description

The 8-Puzzle consists of a 3 × 3 board containing eight numbered tiles and one blank space.

The blank space is represented by `0`.

Example Goal State:

    1 2 3
    4 5 6
    7 8 0

BFS and DFS search for the goal state starting from the given initial state.

The program accepts the initial state and goal state from the user.

A solvability check is also performed before running the algorithms.

## 3. Algorithms Used

### Breadth First Search (BFS)

BFS explores the search space level by level.

It uses a queue to store states that need to be explored.

### Depth First Search (DFS)

DFS explores one path deeply before backtracking.

It uses a stack to store states that need to be explored.

## 4. Profiling Method

The following tools were used:

### timeit

Python's `timeit` module was used to measure execution time.

Each algorithm was executed 3 times for each test case.

The average execution time was calculated from the three runs.

### Manual State Counter

A state counter was added to both BFS and DFS.

It counts the number of states expanded during the search.

### py-spy

`py-spy` was used for function-level performance profiling.

Flame graph files were generated for BFS and DFS for each test case.

The generated files are:

- `bfs_best.svg`
- `dfs_best.svg`
- `bfs_average.svg`
- `dfs_average.svg`
- `bfs_worst.svg`
- `dfs_worst.svg`

## 5. Test Cases

### Best Case

Initial State:

    1 2 3
    4 5 6
    7 8 0

Goal State:

    1 2 3
    4 5 6
    7 8 0

The initial state is already the goal state.

### Average Case

Initial State:

    1 2 3
    5 0 6
    4 7 8

Goal State:

    1 2 3
    4 5 6
    7 8 0

This represents a moderate search case for the experiment.

### Worst Case

Initial State:

    8 6 7
    2 5 4
    3 0 1

Goal State:

    1 2 3
    4 5 6
    7 8 0

This produced a very large search workload in the experiment.

The cases are selected experimental test cases and are not intended to prove the absolute theoretical best, average, or worst complexity of the algorithms.

## 6. Experimental Results

### 6.1 Best Case

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 0.008 | 0.002 |
| Run 2 Time (ms) | 0.003 | 0.002 |
| Run 3 Time (ms) | 0.001 | 0.001 |
| Average Time (ms) | 0.004 | 0.002 |
| States Expanded | 1 | 1 |

### 6.2 Average Case

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 0.089 | 0.077 |
| Run 2 Time (ms) | 0.057 | 0.052 |
| Run 3 Time (ms) | 0.071 | 0.055 |
| Average Time (ms) | 0.072 | 0.061 |
| States Expanded | 33 | 27 |

### 6.3 Worst Case

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 261.823 | 241.761 |
| Run 2 Time (ms) | 263.662 | 195.894 |
| Run 3 Time (ms) | 281.993 | 171.444 |
| Average Time (ms) | 269.159 | 203.033 |
| States Expanded | 181,439 | 98,124 |

## 7. Overall Comparison

| Case | BFS Avg. Time (ms) | DFS Avg. Time (ms) | BFS States | DFS States |
|---|---:|---:|---:|---:|
| Best | 0.004 | 0.002 | 1 | 1 |
| Average | 0.072 | 0.061 | 33 | 27 |
| Worst | 269.159 | 203.033 | 181,439 | 98,124 |

## 8. py-spy Profiling Results

The py-spy profiler successfully generated flame graphs for all six algorithm-case combinations.

| Case | BFS Profile | DFS Profile |
|---|---|---|
| Best | `bfs_best.svg` | `dfs_best.svg` |
| Average | `bfs_average.svg` | `dfs_average.svg` |
| Worst | `bfs_worst.svg` | `dfs_worst.svg` |

All six profiling runs completed with zero py-spy errors.

The number of samples collected varied because the execution time of each test case was different, especially for the very short Best and Average cases.

The py-spy sample count is used as profiling information and is not treated as a performance score.

## 9. Justification and Analysis

The experimental results show that the performance of BFS and DFS changes according to the input state.

In the Best Case, both algorithms expanded only one state because the initial state was already the goal state.

In the Average Case, BFS expanded 33 states while DFS expanded 27 states. The measured average execution times were 0.072 ms for BFS and 0.061 ms for DFS.

In the selected Worst Case, BFS expanded 181,439 states while DFS expanded 98,124 states. The average measured execution times were 269.159 ms for BFS and 203.033 ms for DFS.

The results demonstrate that the number of states explored can strongly affect execution time.

The experiment also shows why empirical profiling is useful. The actual number of states expanded and measured execution time can vary depending on the particular puzzle configuration.

The py-spy flame graphs provide additional information about where execution time is spent inside the Python program.

## 10. AI Contribution Note

AI assistance was used during the development of this project for:

- Understanding BFS and DFS
- Understanding the 8-Puzzle problem
- Developing and explaining Python code
- Adding input validation
- Adding solvability checking
- Adding state counters
- Using `timeit`
- Using py-spy
- Organizing the project documentation

The student selected the problem, created the project repository, entered the test cases, executed the experiments, collected the profiling results, verified the outputs, and analyzed the measured data.

## 11. Conclusion

This project performed an empirical performance analysis of BFS and DFS using the 8-Puzzle problem.

Three selected test cases were evaluated using execution time, states expanded, and py-spy profiling.

The results demonstrate that search performance depends strongly on the input configuration. Measuring actual execution time and states expanded provides practical information about algorithm behavior in addition to theoretical analysis.

## 12. Project Files

- `bfs_8puzzle.py` – BFS implementation
- `dfs_8puzzle.py` – DFS implementation
- `compare.py` – Performance measurement and comparison
- `README.md` – Project documentation
- `AI_Contribution_Log.md` – AI contribution record
- `bfs_best.svg` – BFS Best Case flame graph
- `dfs_best.svg` – DFS Best Case flame graph
- `bfs_average.svg` – BFS Average Case flame graph
- `dfs_average.svg` – DFS Average Case flame graph
- `bfs_worst.svg` – BFS Worst Case flame graph
- `dfs_worst.svg` – DFS Worst Case flame graph