# SLE-3: Architectural Design (Full C4 Model)

## Course

**02AML204 – Introduction to Artificial Intelligence**

## Student Details

- **PRN:** 25UAM109
- **Name:** Pratiksha Jagadish Khondre
- **Division:** B
- **Date:** 04/10/2026

---

## 1. System Title

### 8-Puzzle Solver Using BFS and DFS

The system solves the 8-Puzzle problem using Breadth-First Search (BFS) and Depth-First Search (DFS). The puzzle is represented as a 3×3 grid containing values from 0 to 8, where `0` represents the blank space. The user provides an initial state and a goal state, and the system checks the solvability before performing the search. The same system was used for the performance analysis completed in SLE-2.

---

## 2. Context Diagram (C4 Level 1)

The Context Diagram shows the relationship between the **User** and the **8-Puzzle Solver**.

The user enters the puzzle and selects the search algorithm. The system performs BFS or DFS and returns the search result and performance information to the user.

### Context Diagram

![C4 Level 1 - Context Diagram](c1_context.png)

**Figure 1: Context view of the 8-Puzzle BFS/DFS System**

---

## 3. Container Diagram (C4 Level 2)

The main containers of the system are:

| Container | Responsibility |
|---|---|
| **Input Module** | Takes and validates the initial and goal puzzle states. |
| **Search Engine** | Runs the selected BFS or DFS algorithm. |
| **Puzzle State Generator** | Generates valid neighboring puzzle states. |
| **Visited Set / Memory** | Stores explored states to avoid repeated exploration. |
| **Output Module** | Displays the search result and performance information. |

### Container Diagram

![C4 Level 2 - Container Diagram](c2_container.png)

**Figure 2: Main containers of the 8-Puzzle Solver**

---

## 4. Component Diagram (C4 Level 3)

The Search Engine contains the following components:

| Component | Responsibility |
|---|---|
| **Search Controller** | Controls the BFS/DFS search process. |
| **Frontier** | Maintains the queue for BFS or stack for DFS. |
| **State Expansion** | Generates the next valid puzzle states. |
| **Visited Set** | Tracks states that have already been explored. |
| **Goal Test** | Checks whether the current state is the required goal state. |

### Component Diagram

![C4 Level 3 - Component Diagram](c3_component.png)

**Figure 3: Components inside the Search Engine**

---

## 5. Code Level Overview (C4 Level 4)

The architecture is mapped to the actual project functions:

| File / Function | Responsibility |
|---|---|
| `bfs_8puzzle.py – get_neighbors()` | Generates valid neighboring 8-Puzzle states. |
| `bfs_8puzzle.py – bfs()` | Performs Breadth-First Search using a queue and visited set. |
| `dfs_8puzzle.py – get_neighbors()` | Generates valid neighboring puzzle states. |
| `dfs_8puzzle.py – dfs()` | Performs Depth-First Search using a stack and visited set. |
| `compare.py – get_valid_state()` | Validates the initial and goal puzzle states. |
| `compare.py – is_solvable()` | Checks whether the puzzle configuration is solvable. |
| `compare.py – main()` | Controls execution and displays the comparison. |
| `compare.py – timeit.repeat()` | Measures BFS and DFS execution time. |

---

## 6. Design Decisions

The system separates input validation, puzzle-state generation, search algorithms, and output processing. BFS uses a queue while DFS uses a stack according to their respective search strategies. A visited set is used to avoid repeated exploration of puzzle states. This modular structure also supports the performance comparison performed in SLE-2.

## 7. Learning Outcome

Through SLE-3, I learned how to represent an existing software system at different architectural levels using the C4 Model.

I understood the difference between system context, containers, components, and code-level details. I also learned how architectural decisions can be connected to the actual implementation of a project.

## 8. Conclusion

The SLE-3 architecture represents the same 8-Puzzle BFS/DFS system used in SLE-2. The C4 Model provides different levels of abstraction, from the complete system context to individual functions.

This SLE helped connect the implementation, performance analysis, and software architecture of the project.