# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
ROWS, COLS = 10, 10
GRID_SIZE = 600
SQUARE_SIZE = GRID_SIZE // COLS

# Calculate padding to center the grid
PADDING_X = (WINDOW_WIDTH - GRID_SIZE) // 2
PADDING_Y = (WINDOW_HEIGHT - GRID_SIZE) // 2

# Colors
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
SQUARE_COLOR = (40, 40, 40)
OUTLINE_COLOR = (255, 255, 255)
SELECTED_OUTLINE_COLOR = (0, 0, 216)

BUTTON_SIZE = 50
BUTTON_PADDING = 20
BUTTON_AREA = [(PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + i * (BUTTON_SIZE + BUTTON_PADDING),
                BUTTON_SIZE, BUTTON_SIZE) for i in range(8)]

# Adjust the position of other buttons
BUTTON_AREA[4] = (PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + 4 * (BUTTON_SIZE + BUTTON_PADDING) + 40,
                  BUTTON_SIZE, BUTTON_SIZE)
BUTTON_AREA[5] = (PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + 5 * (BUTTON_SIZE + BUTTON_PADDING) + 40,
                  BUTTON_SIZE, BUTTON_SIZE)
BUTTON_AREA[6] = (PADDING_X + BUTTON_PADDING - 250,
                  PADDING_Y + BUTTON_PADDING + 7 * (BUTTON_SIZE + BUTTON_PADDING) - 487,
                  BUTTON_SIZE,
                  BUTTON_SIZE)
BUTTON_AREA[7] = (PADDING_X + BUTTON_PADDING - 250,
                  PADDING_Y + BUTTON_PADDING + 7 * (BUTTON_SIZE + BUTTON_PADDING) - 415,
                  BUTTON_SIZE,
                  BUTTON_SIZE)

# Buttons for algorithm menu
BUTTON_AREA_LEFT = [
    (50, 100 + 10 + i * (50 + 10),
     50, 50) for i in range(5)
]

ALGORITHM_COLORS = [(255, 0, 0), (255, 165, 0), (0, 255, 0), (255, 105, 180), (128, 0, 128), (128, 0, 0), (0, 0, 255)]

BUTTON_COLORS = [(100, 100, 100), (255, 0, 0), (0, 255, 0), (255, 105, 180), (0, 0, 0), (255, 255, 255), (255, 255, 0),
                 (255, 255, 255), (255, 255, 255)]
BUTTON_CONTROL_COLORS = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128),
                          (255, 165, 0), (0, 0, 255), (128, 0, 0)]

BUTTON_ALGORITHMS = ["DFS", "BFS", "Dijkstra", "A*", "Greedy BFS"]

BUTTON_FUNCTIONALITY = ["Walls", "Start Point", "End Point", "Erase", f"Select Algorithm ({str(len(BUTTON_ALGORITHMS))})", "Start Simulation", "Random Maze", "Reset"]

# Algorithm description:
ALGORITHM_DESCRIPTION = [
    # DFS:
    """
    Depth First Search (DFS) is a fundamental graph traversal algorithm that explores as far as possible 
    along each branch before backtracking. It begins at a selected node, often called the "start" or "root" node, 
    and explores as far as possible along each branch before backtracking. (Click the button below to see a detailed example!)
    """,
    # BFS:
    """
    Breadth First Search (BFS) is a fundamental graph traversal algorithm used to explore nodes in a graph or tree.
    Unlike Depth First Search (DFS), which explores as far as possible along each branch before backtracking,
    BFS explores all the neighboring nodes at the current depth before moving on to the nodes at the next depth level. 
    (Click the button below to see a detailed example!)
    """,
    # Dijkstra
    """
    Dijkstra's algorithm is a fundamental method in computer science used to find the shortest path between nodes in a graph.
    This algorithm efficiently calculates the shortest path from a starting node to all other nodes in a graph. 
    It works by iteratively exploring nodes in the graph, greedily selecting the node with the shortest known distance 
    from the starting node at each step. Through this process, it gradually builds a shortest-path tree rooted at the 
    starting node, ultimately yielding the shortest paths to all other nodes. (Click the button below to see a detailed example!)
    """,
    # A*
    """
    A* is guided by a heuristic function (h(n)) that estimates the cost of reaching the goal from any given node. 
    The quality of this heuristic significantly affects the efficiency and accuracy of A*. A* is guaranteed to find the 
    shortest path. Overall, A* is efficient and effective for finding optimal paths in many scenarios, 
    although its performance can vary depending on factors like the size and complexity 
    of the graph and the quality of the heuristic function. (Click the button below to see a detailed example!)
    """,
    # Greedy Best-First-Search
    """
    Greedy Best-First Search (GBFS) employs a heuristic-based approach to guide its search process. 
    Specifically, it utilizes a Euclidean heuristic, which estimates the distance between a current state 
    and the goal state in terms of straight-line distance. 
    This heuristic serves as the basis for the evaluation function, informing GBFS about the proximity of each node to the goal. 
    By prioritizing nodes based on this heuristic evaluation, GBFS tends to explore paths that appear to be closer to the goal 
    state in terms of straight-line distance. (Click the button below to see a detailed example!)
    """
]
