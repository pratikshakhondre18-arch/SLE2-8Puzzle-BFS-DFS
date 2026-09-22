# AI Contribution Log

## 1. Tools Used

- ChatGPT
- Visual Studio Code
- Python
- Python `timeit`
- py-spy
- GitHub

## 2. AI-Generated / AI-Assisted Parts

AI was used as an assistance tool during the development of the BFS and DFS 8-Puzzle performance analysis.

AI assistance was used for:

- Understanding the 8-Puzzle problem
- Understanding BFS and DFS logic
- Developing the initial Python implementations
- Explaining the algorithms and code
- Adding input validation
- Adding solvability checking
- Adding state expansion counters
- Using Python `timeit` for execution-time measurement
- Using py-spy for performance profiling
- Organizing the experimental results
- Preparing project documentation

## 3. Student's Own Work

The student:

- Selected BFS and DFS for the SLE-2 comparison
- Selected the 8-Puzzle problem
- Created and organized the project files
- Created the GitHub repository
- Entered and tested the initial and goal states
- Selected the experimental Best, Average, and Worst test cases
- Ran BFS and DFS using the same input for each case
- Ran the py-spy profiling experiments
- Generated the six py-spy flame graph files
- Ran each algorithm three times using `timeit`
- Recorded the measured execution times
- Recorded the number of states expanded
- Compared the experimental results
- Verified the final outputs
- Analyzed the measured data

## 4. Experimental Test Cases

### Best Case

Initial State:

    1 2 3
    4 5 6
    7 8 0

Goal State:

    1 2 3
    4 5 6
    7 8 0

### Average Case

Initial State:

    1 2 3
    5 0 6
    4 7 8

Goal State:

    1 2 3
    4 5 6
    7 8 0

### Worst Case

Initial State:

    8 6 7
    2 5 4
    3 0 1

Goal State:

    1 2 3
    4 5 6
    7 8 0

These are selected experimental test cases. They are not intended to prove the absolute theoretical best, average, or worst complexity of BFS or DFS.

## 5. Measured Results

### Best Case

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 0.008 | 0.002 |
| Run 2 Time (ms) | 0.003 | 0.002 |
| Run 3 Time (ms) | 0.001 | 0.001 |
| Average Time (ms) | 0.004 | 0.002 |
| States Expanded | 1 | 1 |

### Average Case

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 0.089 | 0.077 |
| Run 2 Time (ms) | 0.057 | 0.052 |
| Run 3 Time (ms) | 0.071 | 0.055 |
| Average Time (ms) | 0.072 | 0.061 |
| States Expanded | 33 | 27 |

### Worst Case

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 261.823 | 241.761 |
| Run 2 Time (ms) | 263.662 | 195.894 |
| Run 3 Time (ms) | 281.993 | 171.444 |
| Average Time (ms) | 269.159 | 203.033 |
| States Expanded | 181,439 | 98,124 |

## 6. py-spy Profiling

py-spy version used:

    0.4.2

The following flame graph files were generated:

- `bfs_best.svg`
- `dfs_best.svg`
- `bfs_average.svg`
- `dfs_average.svg`
- `bfs_worst.svg`
- `dfs_worst.svg`

All six py-spy profiling runs completed with zero errors.

The number of py-spy samples collected was:

| Case | BFS Samples | DFS Samples |
|---|---:|---:|
| Best | 6 | 9 |
| Average | 3 | 7 |
| Worst | 3 | 5 |

The sample count is profiling information and is not treated as a performance score.

## 7. Issues and Risks

- Execution time can vary slightly between different runs because of system conditions.
- Three runs were performed for each case and the average was calculated.
- The same initial and goal state were used for BFS and DFS within each case.
- Very short test cases produced fewer py-spy samples because the program finished quickly.
- The measured results represent the selected experimental inputs and should not be considered universal results for every possible 8-Puzzle state.

## 8. Transparency Statement

AI was used as an assistance tool during the development and documentation of this SLE-2 activity.

The student performed the actual experiments, entered the test cases, ran the programs, generated the py-spy profiling files, collected the measured results, verified the outputs, and analyzed the experimental data.