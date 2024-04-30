class Constants:
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
    BACKGROUND_COLOR = (0, 0, 0)  # Black
    GRID_COLOR = (200, 200, 200)
    SQUARE_COLOR = (40, 40, 40)
    OUTLINE_COLOR = (255, 255, 255)  # White outline color
    SELECTED_OUTLINE_COLOR = (0, 0, 216)  # Yellow outline color for selected buttons

    # Define button colors and functionalities
    BUTTON_SIZE = 50
    BUTTON_PADDING = 20
    BUTTON_AREA = [(PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + i * (BUTTON_SIZE + BUTTON_PADDING),
                    BUTTON_SIZE, BUTTON_SIZE) for i in range(9)]
    BUTTON_COLORS = [(100, 100, 100), (255, 0, 0), (0, 255, 0), (255, 105, 180), (0, 0, 0), (255, 255, 255), (255, 255, 255),
                     (255, 255, 255), (255, 255, 255)]
    BUTTON_CONTROL_COLORS = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (164, 219, 232),
                              (255, 255, 224), (255, 165, 0), (0, 0, 255), (255, 0, 255)]
    BUTTON_FUNCTIONALITY = ["Walls", "Start Point", "End Point", "Erase", "DFS", "BFS", "Start Simulation", "Random Maze", "Reset"]