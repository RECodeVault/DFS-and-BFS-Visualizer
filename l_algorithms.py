from collections import deque
from board import Board


def is_valid_move(grid, visited, row, col):
    rows = len(grid)
    cols = len(grid[0])

    return 0 <= row < rows and 0 <= col < cols and not visited[row][col] and grid[row][col] != "#"


def bfs(grid, start_point, end_point, squares):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    queue.append(start_point)
    visited[start_point[0]][start_point[1]] = True

    move_queue = deque()

    new_board = Board(10, 10, squares)

    while queue:
        row, col, dist = queue.popleft()

        # Check if the current node is the destination
        if (row, col) == end_point:
            return move_queue, new_board, dist

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new cell is a valid move
            if is_valid_move(grid, visited, new_row, new_col):
                # Mark the new cell as visited and add it to the queue
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))
                move_queue.append((new_row, new_col))
                new_board.update_board(visited)

    return -1


def dfs(grid, start_point, end_point, squares):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [(start_point[0], start_point[1], 0)]
    visited[start_point[0]][start_point[1]] = True

    move_queue = deque()
    new_board = Board(10, 10, squares)

    while stack:
        current = stack[-1]
        row, col, dist = current
        if (row, col) == end_point:
            return move_queue, new_board, dist

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        found_next_move = False
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if is_valid_move(grid, visited, new_row, new_col):
                stack.append((new_row, new_col, dist + 1))
                visited[new_row][new_col] = True
                found_next_move = True
                move_queue.append((new_row, new_col))
                new_board.update_board(visited)
                break

        if not found_next_move:
            stack.pop()

    return -1
