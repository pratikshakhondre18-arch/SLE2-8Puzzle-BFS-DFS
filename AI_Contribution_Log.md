## 1. Tools Used

- ChatGPT
- Visual Studio Code
- Python
- GitHub

## 2. AI-Generated / AI-Assisted Parts

AI was used to help understand and develop the BFS and DFS implementations for the 8-Puzzle problem.

AI assistance was used for:

- Understanding the 8-Puzzle problem
- Understanding BFS and DFS logic
- Developing the initial Python code
- Explaining the code and algorithm steps
- Debugging programming errors
- Adding input validation
- Adding solvability checking
- Using the Python `timeit` module for performance measurement
- Preparing the project documentation

## 3. Student's Own Work

The student:

- Selected BFS and DFS for the SLE-2 comparison
- Selected the 8-Puzzle problem
- Created and organized the project files
- Entered and tested the initial and goal states
- Ran both algorithms using the same input
- Performed the final profiling runs
- Recorded the measured execution times
- Recorded the number of states expanded
- Compared the experimental results
- Reviewed and verified the final project output

## 4. Experimental Results

The final experiment was performed using the same initial and goal state for both algorithms.

Initial State:

    7 2 4
    5 0 6
    8 3 1

Goal State:

    1 2 3
    4 5 6
    7 8 0

Final measured results:

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time (ms) | 124.331 | 251.130 |
| States Expanded | 55,409 | 99,900 |
| Number of Runs | 3 | 3 |

### Individual Run Times

#### BFS

- Run 1: 127.568 ms
- Run 2: 125.964 ms
- Run 3: 119.461 ms

#### DFS

- Run 1: 224.701 ms
- Run 2: 275.733 ms
- Run 3: 252.957 ms
## 5. Issues and Risks

- Execution time can vary slightly between different runs because of system conditions.
- Therefore, three runs were performed and their average was used.
- Both algorithms were tested using the same initial and goal state for a fair comparison.
- The measured results represent the tested 8-Puzzle input and should not be considered universal for every possible 8-Puzzle state.

## 6. Transparency Statement

AI was used as an assistance tool during the development and documentation of this SLE-2 activity. The student tested the code, ran the experiments, verified the output, and used the measured results for the final analysis.