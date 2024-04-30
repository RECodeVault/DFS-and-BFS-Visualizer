import pygame
import sys

import constants
from l_algorithms import dfs, bfs
from board import Board
import time
from mazes import mazes
import random
from constants import Constants

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

# 2D list to track the state of each square (True for filled, False for empty)
grid_state = [[False for _ in range(constants.Constants.COLS)] for _ in range(constants.Constants.ROWS)]

# List to store square properties
squares = [{'row': row, 'col': col, 'color_index': 4} for row in range(ROWS) for col in range(COLS)]

# Load the font
font = pygame.font.SysFont(None, 30)

start_simulation_check = False

simulation_finished = False

dist = 0


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


def simulate_moves(updated_board, simulation_queue, screen, button_colors):
    # Show text info
    moves = font.render("Moves:", True, (255, 255, 255))
    text_rect = moves.get_rect(midleft=(105, WINDOW_HEIGHT // 2 - 10))
    screen.blit(moves, text_rect)

    moves_text = font.render("(0, 0)", True, (255, 255, 255))
    text_rect = moves_text.get_rect(midleft=(110, WINDOW_HEIGHT // 2 + 20))
    screen.blit(moves_text, text_rect)

    for row_index, row in enumerate(updated_board):
        for col_index, value in enumerate(row):
            if value == 'V':
                for square in squares:
                    if square['row'] == row_index and square['col'] == col_index and square['color_index'] == 4:
                        square['color_index'] = 5
    for row, col in simulation_queue:
        if updated_board[row][col] == 'V':
            for square in squares:
                if square['row'] == row and square['col'] == col and square['color_index'] == 5:
                    moves_text = font.render(f"({square['row']}, {square['col']})", True, (255, 255, 255))
                    screen.fill((0, 0, 0), text_rect)
                    screen.blit(moves_text, text_rect)
                    fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
                    draw_grid(screen)
                    time.sleep(0.2)
                    pygame.display.flip()


# Starts simulation function
def start_simulation(chosen_algorithm, screen, button_colors):
    global start_simulation_check
    global simulation_finished
    global dist
    start_simulation_check = True
    board = Board(10, 10, squares)
    grid, start_point, end_point = board.get_board_and_pos()
    if chosen_algorithm == "BFS":
        simulation_queue, new_board, dist = bfs(grid, start_point, end_point, squares)
        updated_board, _, _ = new_board.get_board_and_pos()
        simulate_moves(updated_board, simulation_queue, screen, button_colors)
    else:
        simulation_queue, new_board, dist = dfs(grid, start_point, end_point, squares)
        updated_board, _, _ = new_board.get_board_and_pos()
        simulate_moves(updated_board, simulation_queue, screen, button_colors)
    simulation_finished = True


def load_random_maze(squares, screen, button_colors, grid_state):
    # Reset grid_state list to False
    for row in range(len(grid_state)):
        for col in range(len(grid_state[row])):
            grid_state[row][col] = False

    # Reset squares list
    squares.clear()

    # Reset board
    for square in squares:
        fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
        draw_grid(screen)
        pygame.display.flip()

    chosen_maze = mazes["Maze " + str(random.randint(1, len(mazes)))]
    for row in chosen_maze:
        for col in row:
            color_index = col['color_index']
            save_square(col['row'], col['col'], color_index)
    for square in squares:
        fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
        draw_grid(screen)
        pygame.display.flip()


def reset(grid_state, squares, screen, button_colors):
    global start_simulation_check
    global simulation_finished

    start_simulation_check = False
    simulation_finished = False

    # Reset grid_state list to False
    for row in range(len(grid_state)):
        for col in range(len(grid_state[row])):
            grid_state[row][col] = False

    # Reset squares list
    squares.clear()

    for row in range(10):
        for col in range(10):
            square = {'row': row, 'col': col, 'color_index': 4}
            squares.append(square)

    for square in squares:
        fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
        draw_grid(screen)
        pygame.display.flip()

def draw_line(y_constant, x_constant_end, x_constant_start, screen):
    # Draw additional horizontal line to separate other buttons
    line_y1 = PADDING_Y + BUTTON_SIZE * 4 + BUTTON_PADDING * 5 + y_constant
    line_start_x1 = PADDING_X + GRID_SIZE + BUTTON_PADDING + x_constant_start
    line_end_x1 = PADDING_X + GRID_SIZE + BUTTON_PADDING * 11 + BUTTON_SIZE + x_constant_end
    pygame.draw.line(screen, GRID_COLOR, (line_start_x1, line_y1),
                     (line_end_x1, line_y1), width=5)


# Main function
def main():
    global squares
    global start_simulation_check
    global simulation_finished

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
    BUTTON_AREA[7] = (PADDING_X + BUTTON_PADDING - 250,
                      PADDING_Y + BUTTON_PADDING + 7 * (BUTTON_SIZE + BUTTON_PADDING) - 487,
                      BUTTON_SIZE,
                      BUTTON_SIZE)
    BUTTON_AREA[8] = (PADDING_X + BUTTON_PADDING - 250,
                      PADDING_Y + BUTTON_PADDING + 7 * (BUTTON_SIZE + BUTTON_PADDING) - 415,
                      BUTTON_SIZE,
                      BUTTON_SIZE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Unlocking only the reset button after simulation is complete
            elif event.type == pygame.MOUSEBUTTONDOWN and simulation_finished:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check button clicks
                for i, button_area in enumerate(BUTTON_AREA):
                    if button_area[0] < mouse_x < button_area[0] + button_area[2] and \
                            button_area[1] < mouse_y < button_area[1] + button_area[3]:
                        if BUTTON_FUNCTIONALITY[i] == "Reset" and simulation_finished:
                            reset(grid_state, squares, screen, button_colors)
            elif event.type == pygame.MOUSEBUTTONDOWN and not start_simulation_check:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check button clicks
                for i, button_area in enumerate(BUTTON_AREA):
                    if button_area[0] < mouse_x < button_area[0] + button_area[2] and \
                            button_area[1] < mouse_y < button_area[1] + button_area[3]:
                        if i < len(BUTTON_FUNCTIONALITY) - 3 and BUTTON_FUNCTIONALITY[i] != "DFS" and BUTTON_FUNCTIONALITY[i] != "BFS":
                            selected_color_index = i  # Update the selected color index
                        else:
                            if selected_algorithm is not None and BUTTON_FUNCTIONALITY[i] == "Start Simulation" and not start_simulation_check:
                                if sum(1 for square in squares if square['color_index'] == 1) == 1 and sum(1 for square in squares if square['color_index'] == 2) == 1:
                                    start_simulation(selected_algorithm, screen, button_colors)
                                else:
                                    print("You must place at least one Start and End point")
                        if BUTTON_FUNCTIONALITY[i] == "DFS" or BUTTON_FUNCTIONALITY[i] == "BFS":
                            selected_algorithm = BUTTON_FUNCTIONALITY[i]
                            selected_color_controls_index = i
                        if BUTTON_FUNCTIONALITY[i] == "Random Maze":
                            load_random_maze(squares, screen, button_colors, grid_state)
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
                if i == 1:  # If it is start point
                    red_tiles_placed = sum(1 for square in squares if square['color_index'] == 1)
                    text = font.render(f"Start Point - {str(1 - red_tiles_placed)}", True, (255, 255, 255))
                elif i == 2:  # If it is end point
                    green_tiles_placed = sum(1 for square in squares if square['color_index'] == 2)
                    text = font.render(f"End Point - {str(1 - green_tiles_placed)}", True, (255, 255, 255))
                else:
                    text = font.render(BUTTON_FUNCTIONALITY[i], True, (255, 255, 255))
                text_rect = text.get_rect(
                    midleft=(button_area[0] + button_area[2] + 10, button_area[1] + button_area[3] // 2))
                screen.blit(text, text_rect)

            # Information text:
            chosen_algorithm = font.render("Chosen Algorithm:", True, (255, 255, 255))
            text_rect = chosen_algorithm.get_rect(midleft=(55, WINDOW_HEIGHT // 2 - 100))
            screen.blit(chosen_algorithm, text_rect)

            algorithm_text = font.render(selected_algorithm, True, (255, 255, 255))
            text_rect = algorithm_text.get_rect(midleft=(120, WINDOW_HEIGHT // 2 - 60))
            screen.blit(algorithm_text, text_rect)

            if simulation_finished:
                result = font.render("Results:", True, (255, 255, 255))
                text_rect = result.get_rect(midleft=(100, WINDOW_HEIGHT // 2 - 10))
                screen.blit(result, text_rect)

                result_text = font.render(f"{dist} moves to destination", True, (255, 255, 255))
                text_rect = result_text.get_rect(midleft=(35, WINDOW_HEIGHT // 2 + 20))
                screen.blit(result_text, text_rect)

            # Draws lines to separate buttons
            draw_line(10, 0, 0, screen)
            draw_line(-130, -900, -895, screen)
            draw_line(-35, -895, -900, screen)

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