import pygame
import sys
from l_algorithms import dfs, bfs

# Initialize Pygame
pygame.init()

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
GRID_COLOR = (255, 255, 255)  # Light gray
SQUARE_COLOR = (40, 40, 40)
OUTLINE_COLOR = (255, 255, 255)  # White outline color
SELECTED_OUTLINE_COLOR = (0, 0, 216)  # Yellow outline color for selected buttons

# Define button colors and functionalities
BUTTON_SIZE = 50
BUTTON_PADDING = 20
BUTTON_AREA = [(PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + i * (BUTTON_SIZE + BUTTON_PADDING),
                BUTTON_SIZE, BUTTON_SIZE) for i in range(7)]
BUTTON_COLORS = [(100, 100, 100), (255, 0, 0), (0, 255, 0), (255, 105, 180), (0, 0, 0), (255, 255, 255), (255, 255, 255),
                 (255, 255, 255)]
BUTTON_CONTROL_COLORS = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (164, 219, 232),
                          (255, 255, 224), (255, 165, 0), (255, 255, 255)]
BUTTON_FUNCTIONALITY = ["Walls", "Start Point", "End Point", "Erase", "DFS", "BFS", "Start Simulation"]

# 2D list to track the state of each square (True for filled, False for empty)
grid_state = [[False for _ in range(COLS)] for _ in range(ROWS)]

# List to store square properties
squares = [{'row': row, 'col': col, 'color_index': 4} for row in range(ROWS) for col in range(COLS)]

# Load the font
font = pygame.font.SysFont(None, 30)

start_simulation_check = False

# Function to draw the grid
def draw_grid(screen):
    # Draw vertical lines
    for x in range(PADDING_X, PADDING_X + GRID_SIZE + 1, SQUARE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, PADDING_Y), (x, PADDING_Y + GRID_SIZE))
    # Draw horizontal lines
    for y in range(PADDING_Y, PADDING_Y + GRID_SIZE + 1, SQUARE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (PADDING_X, y), (PADDING_X + GRID_SIZE, y))

# Function to fill a square with color
def fill_square(screen, row, col, color):
    pygame.draw.rect(screen, color, (PADDING_X + col * SQUARE_SIZE, PADDING_Y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to save square properties
def save_square(row, col, color_index):
    global squares
    for square in squares[:]:  # Iterate over a copy of squares to avoid modifying it while iterating
        if square['color_index'] == 1 and color_index == 1:  # If the square is red and the new one is also red
            squares.remove(square)  # Remove the existing red square
            grid_state[square['row']][square['col']] = False  # Set grid_state to False for the removed red square
        elif square['color_index'] == 2 and color_index == 2:  # If the square is green and the new one is also green
            squares.remove(square)  # Remove the existing green square
            grid_state[square['row']][square['col']] = False  # Set grid_state to False for the removed green square
    squares.append({'row': row, 'col': col, 'color_index': color_index})  # Add the new square
    grid_state[row][col] = True

# Starts simulation function
def start_simulation(chosen_algorithm):
    global start_simulation_check
    print(f"Starting simulation: {chosen_algorithm}")
    start_simulation_check = True
    print(get_board())
    if chosen_algorithm == "BFS":
        bfs()
    else:
        dfs()
    # TODO: IMPLEMENT THE REST OF THE CODE LOGIC HAVING IT UPDATE THE BOARD AFTER EACH STATE CHANGE

def get_board():
    board = [['.' for _ in range(COLS)] for _ in range(ROWS)]

    for square in squares:
        row = square['row']
        col = square['col']
        color_index = square['color_index']

        if color_index == 0:
            board[row][col] = '#'  # Walls represented by #
        elif color_index == 1:
            board[row][col] = 'S'  # Start Point represented by S
        elif color_index == 2:
            board[row][col] = 'E'  # End Point represented by E

    return board

# Main function
def main():
    global squares
    global start_simulation_check

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("DFS and BFS Visualizer")
    original_background = screen.copy()  # Store the original background

    # Initialize button colors
    button_colors = BUTTON_COLORS.copy()
    button_control_colors = BUTTON_CONTROL_COLORS.copy()

    # Initialize the selected color index
    selected_color_index = 0  # Default to dark gray
    selected_color_controls_index = 4  # Default to DFS
    selected_algorithm = "DFS"

    running = True
    drawing = False

    # Adjust the position of the DFS and BFS buttons
    BUTTON_AREA[4] = (PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + 4 * (BUTTON_SIZE + BUTTON_PADDING) + 40,
                      BUTTON_SIZE, BUTTON_SIZE)
    BUTTON_AREA[5] = (PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + 5 * (BUTTON_SIZE + BUTTON_PADDING) + 40,
                      BUTTON_SIZE, BUTTON_SIZE)
    BUTTON_AREA[6] = (PADDING_X + GRID_SIZE + BUTTON_PADDING, PADDING_Y + BUTTON_PADDING + 6 * (BUTTON_SIZE + BUTTON_PADDING) + 40,
                      BUTTON_SIZE, BUTTON_SIZE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not start_simulation_check:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check button clicks
                for i, button_area in enumerate(BUTTON_AREA):
                    if button_area[0] < mouse_x < button_area[0] + button_area[2] and \
                            button_area[1] < mouse_y < button_area[1] + button_area[3]:
                        if i < len(BUTTON_FUNCTIONALITY) - 1 and BUTTON_FUNCTIONALITY[i] != "DFS" and BUTTON_FUNCTIONALITY[i] != "BFS":
                            selected_color_index = i  # Update the selected color index
                        else:
                            if selected_algorithm is not None and BUTTON_FUNCTIONALITY[i] == "Start Simulation":
                                if sum(1 for square in squares if square['color_index'] == 1) == 1 and sum(1 for square in squares if square['color_index'] == 2) == 1:
                                    start_simulation(selected_algorithm)
                                else:
                                    print("You must place at least one Start and End point")
                        if BUTTON_FUNCTIONALITY[i] == "DFS" or BUTTON_FUNCTIONALITY[i] == "BFS":
                            selected_algorithm = BUTTON_FUNCTIONALITY[i]
                            selected_color_controls_index = i
                # Check if the left mouse button is pressed down while over the grid
                if event.button == 1 and PADDING_X < mouse_x < PADDING_X + GRID_SIZE and PADDING_Y < mouse_y < PADDING_Y + GRID_SIZE:
                    drawing = True
                    col = (mouse_x - PADDING_X) // SQUARE_SIZE
                    row = (mouse_y - PADDING_Y) // SQUARE_SIZE
                    if 0 <= row < ROWS and 0 <= col < COLS and BUTTON_FUNCTIONALITY[selected_color_index] != "DFS" and BUTTON_FUNCTIONALITY[selected_color_index] != "BFS" and BUTTON_FUNCTIONALITY[selected_color_index] != "Start Simulation":
                        if BUTTON_FUNCTIONALITY[selected_color_index] == "Erase":
                            squares = [square for square in squares if
                                       not (square['row'] == row and square['col'] == col)]
                            fill_square(screen, row, col, BACKGROUND_COLOR)  # Fill with background color
                            squares.append({'row': row, 'col': col, 'color_index': 4})
                            grid_state[row][col] = False
                        else:
                            if not grid_state[row][col]:
                                color_index = selected_color_index  # Use the selected color index
                                fill_square(screen, row, col, button_colors[color_index])
                                grid_state[row][col] = True
                                save_square(row, col, color_index)
            elif event.type == pygame.MOUSEBUTTONUP and not start_simulation_check:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing and not start_simulation_check:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if PADDING_X < mouse_x < PADDING_X + GRID_SIZE and PADDING_Y < mouse_y < PADDING_Y + GRID_SIZE:
                    col = (mouse_x - PADDING_X) // SQUARE_SIZE
                    row = (mouse_y - PADDING_Y) // SQUARE_SIZE
                    if 0 <= row < ROWS and 0 <= col < COLS and BUTTON_FUNCTIONALITY[selected_color_index] != "DFS" and BUTTON_FUNCTIONALITY[selected_color_index] != "BFS" and BUTTON_FUNCTIONALITY[selected_color_index] != "Start Simulation":
                        if BUTTON_FUNCTIONALITY[selected_color_index] == "Erase":
                            squares = [square for square in squares if
                                       not (square['row'] == row and square['col'] == col)]
                            grid_state[row][col] = False  # Set the state to False (erase)
                            fill_square(screen, row, col, BACKGROUND_COLOR)  # Fill with background color
                            squares.append({'row': row, 'col': col, 'color_index': 4})
                            grid_state[row][col] = False
                        else:
                            if not grid_state[row][col]:
                                color_index = selected_color_index  # Use the selected color index
                                fill_square(screen, row, col, button_colors[color_index])
                                grid_state[row][col] = True
                                save_square(row, col, color_index)

        screen.blit(original_background, (0, 0))  # Redraw the original background
        draw_grid(screen)

        # Draw filled squares
        for square in squares:
            fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
            draw_grid(screen)

        # Draw buttons with text
        for i, (button_area, button_color, button_control_color) in enumerate(zip(BUTTON_AREA, button_colors, button_control_colors)):
            if i == selected_color_index:
                pygame.draw.rect(screen, SELECTED_OUTLINE_COLOR, button_area, 3)  # Draw selected outline
            elif i == selected_color_controls_index:
                pygame.draw.rect(screen, SELECTED_OUTLINE_COLOR, button_area, 3)  # Draw selected outline
            else:
                pygame.draw.rect(screen, OUTLINE_COLOR, button_area, 3)  # Draw white outline
            if i < 4:
                pygame.draw.rect(screen, button_color, button_area, border_radius=15)
            else:
                pygame.draw.rect(screen, button_control_color, button_area, border_radius=15)
            # Render text onto the buttons
            if i < len(BUTTON_FUNCTIONALITY):
                text = None
                if i == 0:
                    text = font.render("Walls - inf", True, (255, 255, 255))
                elif i == 1:  # If it is start point
                    red_tiles_placed = sum(1 for square in squares if square['color_index'] == 1)
                    text = font.render(f"Start Point - {str(1 - red_tiles_placed)}", True, (255, 255, 255))
                elif i == 2:  # If it is end point
                    green_tiles_placed = sum(1 for square in squares if square['color_index'] == 2)
                    text = font.render(f"End Point - {str(1 - green_tiles_placed)}", True, (255, 255, 255))
                elif i == 3:
                    text = font.render("Erase", True, (255, 255, 255))  # Render text with white color
                elif i == 4:
                    text = font.render("DFS", True, (255, 255, 255))
                elif i == 5:
                    text = font.render("BFS", True, (255, 255, 255))
                else:
                    text = font.render("Start Simulation", True, (255, 255, 255))
                text_rect = text.get_rect(
                    midleft=(button_area[0] + button_area[2] + 10, button_area[1] + button_area[3] // 2))
                screen.blit(text, text_rect)

            # Draw additional horizontal line to separate buttons
            line_y = PADDING_Y + BUTTON_SIZE * 4 + BUTTON_PADDING * 5 + 10  # Adjusted y-coordinate
            line_start_x = PADDING_X + GRID_SIZE + BUTTON_PADDING
            line_end_x = PADDING_X + GRID_SIZE + BUTTON_PADDING * 11 + BUTTON_SIZE  # Adjusted x-coordinate
            pygame.draw.line(screen, GRID_COLOR, (line_start_x, line_y),
                             (line_end_x, line_y), width=5)  # Thicker line

        # Check if mouse is over a button and change cursor accordingly
        for button_area in BUTTON_AREA:
            if pygame.Rect(button_area).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
                break
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()