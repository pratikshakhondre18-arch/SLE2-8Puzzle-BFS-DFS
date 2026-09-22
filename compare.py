import timeit
from statistics import mean

from bfs_8puzzle import bfs
from dfs_8puzzle import dfs


def is_solvable(start, goal):
    start_values = [value for value in start if value != 0]
    goal_values = [value for value in goal if value != 0]

    start_inversions = 0
    goal_inversions = 0

    for i in range(len(start_values)):
        for j in range(i + 1, len(start_values)):
            if start_values[i] > start_values[j]:
                start_inversions += 1

    for i in range(len(goal_values)):
        for j in range(i + 1, len(goal_values)):
            if goal_values[i] > goal_values[j]:
                goal_inversions += 1

    return (start_inversions % 2) == (goal_inversions % 2)


def get_valid_state(message):
    while True:
        try:
            values = list(map(int, input(message).split()))

            if len(values) != 9:
                print("Please enter exactly 9 numbers.")
                continue

            if sorted(values) != list(range(9)):
                print("Use each number from 0 to 8 exactly once.")
                continue

            return tuple(values)

        except ValueError:
            print("Please enter numbers only.")


def main():
    print("==============================================")
    print("      BFS vs DFS - 8 Puzzle Performance")
    print("==============================================")

    start = get_valid_state(
        "\nEnter initial state (9 numbers, use 0 for blank): "
    )

    goal = get_valid_state(
        "Enter goal state (9 numbers, use 0 for blank): "
    )

    if not is_solvable(start, goal):
        print("\nThis puzzle cannot be solved from the given initial state.")
        print("Please enter a solvable puzzle.")
        return

    print("\nPuzzle is solvable.")
    print("Running BFS and DFS...")

    number_of_runs = 3

    # Measure BFS
    bfs_times = timeit.repeat(
        lambda: bfs(start, goal),
        repeat=number_of_runs,
        number=1
    )

    # Measure DFS
    dfs_times = timeit.repeat(
        lambda: dfs(start, goal),
        repeat=number_of_runs,
        number=1
    )

    # Convert seconds to milliseconds
    bfs_times_ms = [time * 1000 for time in bfs_times]
    dfs_times_ms = [time * 1000 for time in dfs_times]

    # Calculate averages
    bfs_average = mean(bfs_times_ms)
    dfs_average = mean(dfs_times_ms)

    # Count states expanded
    bfs_states = bfs(start, goal)
    dfs_states = dfs(start, goal)

    print("\n================ PERFORMANCE RESULTS ================")

    print("\nBFS Run Times:")
    for i, time in enumerate(bfs_times_ms, start=1):
        print(f"Run {i}: {time:.3f} ms")

    print(f"Average: {bfs_average:.3f} ms")
    print(f"States Expanded: {bfs_states}")

    print("\nDFS Run Times:")
    for i, time in enumerate(dfs_times_ms, start=1):
        print(f"Run {i}: {time:.3f} ms")

    print(f"Average: {dfs_average:.3f} ms")
    print(f"States Expanded: {dfs_states}")

    print("\n================ COMPARISON TABLE ================")

    print(f"{'Metric':<25}{'BFS':<20}{'DFS':<20}")
    print("-" * 65)
    print(f"{'Average Time (ms)':<25}{bfs_average:<20.3f}{dfs_average:<20.3f}")
    print(f"{'States Expanded':<25}{bfs_states:<20}{dfs_states:<20}")
    print(f"{'Number of Runs':<25}{number_of_runs:<20}{number_of_runs:<20}")

    print("\n====================================================")


if __name__ == "__main__":
    main()