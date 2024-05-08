import heapq
from collections import deque
from queue import PriorityQueue
from board import Board


def is_valid_move(board, visited, row, col):
    """
    Checks for if the certain move is valid
    :param board: Board list
    :param visited: List of visited cells
    :param row: Row
    :param col: Column
    :return: True | False
    """
    rows = len(board)
    cols = len(board[0])

    return 0 <= row < rows and 0 <= col < cols and not visited[row][col] and board[row][col] != "#"


def bfs(board, start_point, end_point, squares):
    """
    BFS algorithm to find the shortest path from start_point to end_point
    :param board: Board list
    :param start_point: Starting point
    :param end_point: End point
    :param squares: List of squares
    :return: move_queue, new_board, dist, shortest_path
    """
    rows = len(board)
    cols = len(board[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    queue.append(start_point[0:2])
    visited[start_point[0]][start_point[1]] = True

    move_queue = deque()
    new_board = Board(10, 10, squares)

    while queue:
        row, col = queue.popleft()

        if (row, col) == end_point:
            shortest_path = []
            current = end_point
            while current is not None:
                shortest_path.append(current)
                current = parent[current[0]][current[1]]
            shortest_path.reverse()
            return move_queue, new_board, len(shortest_path) - 1, shortest_path

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(board, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))
                parent[new_row][new_col] = (row, col)
                move_queue.append((new_row, new_col))
                new_board.update_board(visited)

    return move_queue, new_board, -1, []


def dfs(board, start_point, end_point, squares):
    """
    DFS algorithm to find the shortest path from start_point to end_point
    :param board: Board list
    :param start_point: Starting point
    :param end_point: End point
    :param squares: Square list
    :return: move_queue, new_board, dist, shortest_path
    """
    rows = len(board)
    cols = len(board[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [(start_point[0], start_point[1], 0)]
    visited[start_point[0]][start_point[1]] = True
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    move_queue = deque()
    new_board = Board(10, 10, squares)

    while stack:
        current = stack[-1]
        row, col = current[0:2]
        if (row, col) == end_point:
            shortest_path = []
            while current is not None:
                shortest_path.append((current[0], current[1]))
                current = parent[current[0]][current[1]]
            shortest_path.reverse()
            return move_queue, new_board, len(shortest_path) - 1, shortest_path

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        found_next_move = False

        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if is_valid_move(board, visited, new_row, new_col):
                stack.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[new_row][new_col] = (row, col)
                found_next_move = True
                move_queue.append((new_row, new_col))
                new_board.update_board(visited)
                break

        if not found_next_move:
            stack.pop()

    return move_queue, new_board, -1, []


def dijkstra(board, start_point, end_point, squares):
    """
    Dijkstra's algorithm to find the shortest path from start_point to end_point
    :param board: Board list
    :param start_point: Starting point
    :param end_point: End point
    :param squares: Square list
    :return: move_queue, new_board, dist, shortest_path
    """
    rows = len(board)
    cols = len(board[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start_point[0]][start_point[1]] = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    pq = [(0, start_point)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    move_queue = deque()
    new_board = Board(10, 10, squares)

    while pq:
        dist, node = heapq.heappop(pq)
        if node == end_point:
            shortest_path = []
            current = end_point
            while current is not None:
                shortest_path.append((current[0], current[1]))
                current = parent[current[0]][current[1]]
            shortest_path.reverse()
            return move_queue, new_board, dist, shortest_path

        if visited[node[0]][node[1]]:
            continue
        visited[node[0]][node[1]] = True

        row, col = node[0:2]
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if is_valid_move(board, visited, n_row, n_col):
                new_dist = dist + 1
                if new_dist < distances[n_row][n_col]:
                    distances[n_row][n_col] = new_dist
                    heapq.heappush(pq, (new_dist, (n_row, n_col)))
                    parent[n_row][n_col] = (row, col)
                    move_queue.append((n_row, n_col))
                    new_board.update_board(visited)

    return move_queue, new_board, -1, []


def man_heuristic(node, end):
    """
    Calculates the manhattan distance between the start point and the end point
    :param node: Node
    :param end: End point
    :return: Manhattan distance
    """
    return abs(node[0] - end[0]) + abs(node[1] - end[1])


def a_star(board, start_point, end_point, squares):
    """
    A* algorithm that finds the shortest point from the start point to the end point using
    :param board: Board list
    :param start_point: Start point
    :param end_point: End point
    :param squares: Squares list
    :return: move_queue, new_board, dist, shortest_path
    """
    rows = len(board)
    cols = len(board[0])
    pq = [(0, start_point)]
    heapq.heapify(pq)
    came_from = {}
    cost_so_far = {start_point: 0}
    dist = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    move_queue = deque()
    new_board = Board(10, 10, squares)

    visited[start_point[0]][start_point[1]] = True

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_node == end_point:
            path = []
            current_node = end_point
            while current_node != start_point:
                path.append(current_node)
                current_node = came_from[current_node]
                dist += 1
            path.append(start_point)
            path.reverse()
            return move_queue, new_board, dist, path

        row, col = current_node[0:2]
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for next_node in neighbors:
            n_row, n_col = next_node
            new_cost = cost_so_far[current_node] + 1
            if 0 <= n_row < rows and 0 <= n_col < cols and board[n_row][n_col] != "#":
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + man_heuristic(next_node, end_point)
                    heapq.heappush(pq, (priority, next_node))
                    came_from[next_node] = current_node
                    visited[n_row][n_col] = True
                    move_queue.append((n_row, n_col))
                    new_board.update_board(visited)

    return move_queue, new_board, -1, []


def euclid_heuristic(curr_pos, goal_pos):
    """
    Calculates the euclidean distance between the start point and end point
    :param curr_pos: Current pos
    :param goal_pos: End point
    :return: The euclidean distance
    """
    return ((curr_pos[0] - goal_pos[0]) ** 2 + (curr_pos[1] - goal_pos[1]) ** 2) ** 0.5


def greedy_bfs(board, start_point, end_point, squares):
    """
    Greedy BFS algorithm that calculates the shortest distance from the start point to the end point
    :param board: board list
    :param start_point: start point
    :param end_point: end_point
    :param squares: squares list
    :return: move_queue, new_board, dist, shortest_path
    """
    rows = len(board)
    cols = len(board[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    pq = PriorityQueue()
    pq.put((0, start_point, 0))
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    move_queue = deque()
    new_board = Board(10, 10, squares)

    visited[start_point[0]][start_point[1]] = True

    while not pq.empty():
        _, current, dist = pq.get()

        if current == end_point:
            shortest_path = []
            while current is not None:
                shortest_path.append((current[0], current[1]))
                current = parent[current[0]][current[1]]
            shortest_path.reverse()
            return move_queue, new_board, dist, shortest_path

        row, col = current[0:2]
        visited[row][col] = True
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < rows and 0 <= n_col < cols and board[n_row][n_col] != "#" and not visited[n_row][n_col]:
                priority = euclid_heuristic(neighbor, end_point)
                pq.put((priority, neighbor, dist + 1))
                visited[n_row][n_col] = True
                move_queue.append((n_row, n_col))
                parent[n_row][n_col] = current
                new_board.update_board(visited)

    return move_queue, new_board, -1, []
