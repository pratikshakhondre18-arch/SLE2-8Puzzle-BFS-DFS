def get_neighbors(state):
    neighbors = []

    zero_position = state.index(0)
    row = zero_position // 3
    col = zero_position % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for move_row, move_col in moves:
        new_row = row + move_row
        new_col = col + move_col

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_position = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero_position], new_state[new_position] = (
                new_state[new_position],
                new_state[zero_position]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(start, goal):
    stack = [start]
    visited = {start}

    states_expanded = 0

    while stack:
        current = stack.pop()
        states_expanded += 1

        if current == goal:
            return states_expanded

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return states_expanded


if __name__ == "__main__":

    print("DFS - 8 Puzzle")

    start_input = input(
        "Enter initial state (9 numbers, use 0 for blank): "
    )

    goal_input = input(
        "Enter goal state (9 numbers, use 0 for blank): "
    )

    start = tuple(map(int, start_input.split()))
    goal = tuple(map(int, goal_input.split()))

    states = dfs(start, goal)

    print("States Expanded:", states)