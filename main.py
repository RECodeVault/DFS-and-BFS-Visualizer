import pygame
import sys

import constants
from l_algorithms import dfs, bfs
from board import Board
import time
from mazes import mazes
import random
import webbrowser

pygame.init()

# 2D list to track the state of each square (True for filled, False for empty)
grid_state = [[False for _ in range(constants.COLS)] for _ in range(constants.ROWS)]

# List to store square properties
squares = [{'row': row, 'col': col, 'color_index': 4} for row in range(constants.ROWS) for col in range(constants.COLS)]

font = pygame.font.SysFont(None, 30)

small_font = pygame.font.Font(None, 25)

start_simulation_check = False

simulation_finished = False

dist = 0


def render_text_with_line_breaks(text, font, max_width):
    """
    Renders the text with line breaks, so it can wrap and not overflow
    :param text: text to be rendered
    :param font: font to be rendered
    :param max_width: max width of the text
    :return: list of wrapped text
    """
    words = text.split()
    lines = []
    current_line = ''
    for word in words:
        if font.size(current_line + ' ' + word)[0] <= max_width:
            current_line += ' ' + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines


def open_algorithm_menu():
    """
    Opens the algorithm menu and renders everything on the screen
    :return: The selected algorithm by the user
    """
    algorithm_selected_index = 0
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption("Select An Algorithm")
    screen.fill((0, 0, 0))
    running = True

    button_rect = pygame.Rect(150, 600, 300, 50)
    pygame.draw.rect(screen, (255, 255, 255), button_rect)

    button_text = font.render("Apply", True, (0, 0, 0))
    screen.blit(button_text, button_text.get_rect(center=button_rect.center))

    pygame.draw.line(screen, (255, 255, 255), (constants.WINDOW_WIDTH // 2, 0), (constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT), 2)

    TEXT_AREA_RECT = pygame.Rect(constants.WINDOW_WIDTH // 2, 0, constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT)

    # Create text surfaces for "Algorithm:" and "Description:"
    algorithm_text_surface = font.render("Select An Algorithm:", True, (255, 255, 255))
    description_text_surface = font.render("Description:", True, (255, 255, 255))

    algorithm_text_rect = algorithm_text_surface.get_rect(midtop=(constants.WINDOW_WIDTH // 4, 30))
    description_text_rect = description_text_surface.get_rect(midtop=(3 * constants.WINDOW_WIDTH // 4, 30))

    # Link Button
    button_rect_link = pygame.Rect(constants.WINDOW_WIDTH - 450, constants.WINDOW_HEIGHT - 100, 300, 50)

    pygame.display.flip()

    while running:

        # for loop through the event queue
        for event in pygame.event.get():

            button_text = font.render(f"{constants.BUTTON_ALGORITHMS[algorithm_selected_index]} example (Click!)",True, (0, 0, 0))

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(150, 600, 300, 50)
                if button_rect.collidepoint(mouse_pos):
                    running = False

                for i, button_area in enumerate(constants.BUTTON_AREA_LEFT):
                    if button_area[0] <= event.pos[0] <= button_area[0] + button_area[2] \
                            and button_area[1] <= event.pos[1] <= button_area[1] + button_area[3]:
                        algorithm_selected_index = i

                if button_rect_link.collidepoint(mouse_pos):
                    if algorithm_selected_index == 0:
                        webbrowser.open("https://www.youtube.com/watch?v=Urx87-NMm6c")
                    elif algorithm_selected_index == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=HZ5YTanv5QE")

        # Draw buttons
        for i, (button_area, button_control_color) in enumerate(zip(constants.BUTTON_AREA_LEFT, constants.ALGORITHM_COLORS)):
            if i == algorithm_selected_index:
                pygame.draw.rect(screen, constants.SELECTED_OUTLINE_COLOR, button_area, 3)  # Draw selected outline
            else:
                pygame.draw.rect(screen, constants.OUTLINE_COLOR, button_area, 3)  # Draw white outline

            pygame.draw.rect(screen, button_control_color, button_area, border_radius=15)

            text = font.render(constants.BUTTON_ALGORITHMS[i], True, (255, 255, 255))

            text_rect = text.get_rect(
                midleft=(button_area[0] + button_area[2] + 10, button_area[1] + button_area[3] // 2))
            screen.blit(text, text_rect)

        pygame.draw.rect(screen, constants.ALGORITHM_COLORS[algorithm_selected_index], button_rect, 3)

        # Draw text area
        pygame.draw.rect(screen, (30, 30, 30), TEXT_AREA_RECT)

        text = constants.ALGORITHM_DESCRIPTION[algorithm_selected_index]
        lines = render_text_with_line_breaks(text, small_font, TEXT_AREA_RECT.width - 20)
        for i, line in enumerate(lines):
            text_surface = small_font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(left=TEXT_AREA_RECT.left + 10,
                                              top=TEXT_AREA_RECT.top + 110 + i * (small_font.get_height() + 5))
            screen.blit(text_surface, text_rect)

        # Draw headers
        screen.blit(algorithm_text_surface, algorithm_text_rect)
        screen.blit(description_text_surface, description_text_rect)

        draw_line(-270, -1200, 300, screen)

        # Draw link button
        pygame.draw.rect(screen, (255, 255, 255), button_rect_link)
        screen.blit(button_text, button_text.get_rect(center=button_rect_link.center))

        pygame.display.flip()

    return constants.BUTTON_ALGORITHMS[algorithm_selected_index]


def draw_grid(screen):
    """
    Draw grid on the screen
    :param screen: Pygame screen
    :return: None
    """
    # Draw vertical lines
    for x in range(constants.PADDING_X, constants.PADDING_X + constants.GRID_SIZE + 1, constants.SQUARE_SIZE):
        pygame.draw.line(screen, constants.GRID_COLOR, (x, constants.PADDING_Y), (x, constants.PADDING_Y + constants.GRID_SIZE))
    # Draw horizontal lines
    for y in range(constants.PADDING_Y, constants.PADDING_Y + constants.GRID_SIZE + 1, constants.SQUARE_SIZE):
        pygame.draw.line(screen, constants.GRID_COLOR, (constants.PADDING_X, y), (constants.PADDING_X + constants.GRID_SIZE, y))


def draw_line(y_constant, x_constant_end, x_constant_start, screen):
    """
    Draws a line on the screen to separate buttons/information
    :param y_constant: Change value of y
    :param x_constant_end: Change value of x endpoint
    :param x_constant_start: Change value of x tart value
    :param screen: Pygame screen
    :return: None
    """
    line_y1 = constants.PADDING_Y + constants.BUTTON_SIZE * 4 + constants.BUTTON_PADDING * 5 + y_constant
    line_start_x1 = constants.PADDING_X + constants.GRID_SIZE + constants.BUTTON_PADDING + x_constant_start
    line_end_x1 = constants.PADDING_X + constants.GRID_SIZE + constants.BUTTON_PADDING * 11 + constants.BUTTON_SIZE + x_constant_end
    pygame.draw.line(screen, constants.GRID_COLOR, (line_start_x1, line_y1),
                     (line_end_x1, line_y1), width=5)


def fill_square(screen, row, col, color):
    """
    Fills a square with the indicated color
    :param screen: Pygame screen
    :param row: Row of square
    :param col: Column of square
    :param color: Chosen color
    :return: None
    """
    pygame.draw.rect(screen, color, (constants.PADDING_X + col * constants.SQUARE_SIZE, constants.PADDING_Y + row * constants.SQUARE_SIZE, constants.SQUARE_SIZE, constants.SQUARE_SIZE))


def save_square(row, col, color_index):
    """
    Saves square to the squares array, and updates grid_state
    :param row: Row of square
    :param col: Column of square
    :param color_index: Chosen color
    :return: None
    """
    for square in squares[:]:
        if square['color_index'] == 1 and color_index == 1:
            squares.remove(square)
            grid_state[square['row']][square['col']] = False
        elif square['color_index'] == 2 and color_index == 2:
            squares.remove(square)
            grid_state[square['row']][square['col']] = False
    squares.append({'row': row, 'col': col, 'color_index': color_index})
    grid_state[row][col] = True


def simulate_moves(updated_board, simulation_queue, screen, button_colors):
    """
    Simulates the moves made by the algorithm, and displays it to the screen
    :param updated_board: Board containing the ascii representation of start_point, end_point and walls
    :param simulation_queue: Queue that contains the order of moves in what was made by the algorithm
    :param screen: Pygame screen
    :param button_colors: Chosen color
    :return: None
    """
    # Show text info
    moves = font.render("Moves:", True, (255, 255, 255))
    text_rect = moves.get_rect(midleft=(105, constants.WINDOW_HEIGHT // 2 - 10))
    screen.blit(moves, text_rect)

    moves_text = font.render("(0, 0)", True, (255, 255, 255))
    text_rect = moves_text.get_rect(midleft=(110, constants.WINDOW_HEIGHT // 2 + 20))
    screen.blit(moves_text, text_rect)

    for row, col in simulation_queue:
        if updated_board[row][col] == 'V':
            for square in squares:
                if square['row'] == row and square['col'] == col and square['color_index'] == 4:
                    square['color_index'] = 5

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
    """
    Initiates the simulation
    :param chosen_algorithm: Chosen algorithm by user
    :param screen: Pygame screen
    :param button_colors: Chosen color
    :return: None
    """
    global start_simulation_check, simulation_finished, dist

    start_simulation_check = True
    board = Board(10, 10, squares)
    start_point, end_point = board.get_pos()
    grid = board.get_board()

    if chosen_algorithm == "BFS":
        simulation_queue, new_board, dist = bfs(grid, start_point, end_point, squares)
    else:
        simulation_queue, new_board, dist = dfs(grid, start_point, end_point, squares)

    updated_board = new_board.get_board()
    simulate_moves(updated_board, simulation_queue, screen, button_colors)
    simulation_finished = True


def load_random_maze(squares, screen, button_colors, grid_state):
    """
    Loads random maze from mazes.py
    :param squares: Squares list
    :param screen: Pygame screen
    :param button_colors: Chosen color
    :param grid_state: Grid_state list
    :return: None
    """
    # Reset grid_state list to False
    for row in range(len(grid_state)):
        for col in range(len(grid_state[row])):
            grid_state[row][col] = False

    squares.clear()

    # Reset board
    for square in squares:
        fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
        draw_grid(screen)
        pygame.display.flip()

    chosen_maze = mazes["Maze " + str(random.randint(1, len(mazes)))]

    # Save information from the chosen maze to the squares list
    for row in chosen_maze:
        for col in row:
            save_square(col['row'], col['col'], col['color_index'])

    # Fill squares
    for square in squares:
        fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
        draw_grid(screen)
        pygame.display.flip()


def reset(grid_state, squares, screen, button_colors):
    """
    Resets the board
    :param grid_state: Grid state list
    :param squares: squares list
    :param screen: Pygame screen
    :param button_colors: Chosen color
    :return: None
    """
    global start_simulation_check, simulation_finished

    start_simulation_check = False
    simulation_finished = False

    # Reset grid_state list to False
    for row in range(len(grid_state)):
        for col in range(len(grid_state[row])):
            grid_state[row][col] = False

    squares.clear()

    # Reset all squares back to its original state
    for row in range(10):
        for col in range(10):
            square = {'row': row, 'col': col, 'color_index': 4}
            squares.append(square)

    # Reset visual on board
    for square in squares:
        fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
        draw_grid(screen)
        pygame.display.flip()


def main():
    """
    Main function that does most of the work
    :return: None
    """
    global squares, start_simulation_check, simulation_finished

    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption("Graph Algorithm Visualizer")
    original_background = screen.copy()  # Store the original background

    button_colors = constants.BUTTON_COLORS.copy()
    button_control_colors = constants.BUTTON_CONTROL_COLORS.copy()

    selected_color_index = 0
    selected_algorithm = "No Chosen Algorithm"

    running = True
    drawing = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Unlocking only the reset button after simulation is complete
            elif event.type == pygame.MOUSEBUTTONDOWN and simulation_finished:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check button clicks
                for i, button_area in enumerate(constants.BUTTON_AREA):
                    if button_area[0] < mouse_x < button_area[0] + button_area[2] and \
                            button_area[1] < mouse_y < button_area[1] + button_area[3]:
                        if constants.BUTTON_FUNCTIONALITY[i] == "Reset":
                            reset(grid_state, squares, screen, button_colors)

            elif event.type == pygame.MOUSEBUTTONDOWN and not start_simulation_check:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check button clicks
                for i, button_area in enumerate(constants.BUTTON_AREA):
                    if button_area[0] < mouse_x < button_area[0] + button_area[2] and \
                            button_area[1] < mouse_y < button_area[1] + button_area[3]:
                        if i < len(constants.BUTTON_FUNCTIONALITY) - 3 and constants.BUTTON_FUNCTIONALITY[i] != f"Select Algorithm ({str(len(constants.BUTTON_ALGORITHMS))})":
                            selected_color_index = i  # Update the selected color index

                        # Checks for if functionality buttons are pressed
                        if constants.BUTTON_FUNCTIONALITY[i] == f"Select Algorithm ({str(len(constants.BUTTON_ALGORITHMS))})":
                            selected_algorithm = open_algorithm_menu()
                        elif constants.BUTTON_FUNCTIONALITY[i] == "Random Maze":
                            load_random_maze(squares, screen, button_colors, grid_state)
                        elif constants.BUTTON_FUNCTIONALITY[i] == "Reset":
                            reset(grid_state, squares, screen, button_colors)
                        elif constants.BUTTON_FUNCTIONALITY[i] == "Start Simulation" and not start_simulation_check:
                            if selected_algorithm == "No Chosen Algorithm":
                                print("You need to choose an algorithm! Navigate over to \"Select Algorithm\" to choose an option")
                            elif sum(1 for square in squares if square['color_index'] == 1) == 1 and sum(1 for square in squares if square['color_index'] == 2) == 1:
                                start_simulation(selected_algorithm, screen, button_colors)
                            else:
                                print("You must place at least one Start and End point")

                # Check if the left mouse button is pressed down while over the grid
                if event.button == 1 and constants.PADDING_X < mouse_x < constants.PADDING_X + constants.GRID_SIZE and \
                        constants.PADDING_Y < mouse_y < constants.PADDING_Y + constants.GRID_SIZE:
                    drawing = True
                    col = (mouse_x - constants.PADDING_X) // constants.SQUARE_SIZE
                    row = (mouse_y - constants.PADDING_Y) // constants.SQUARE_SIZE
                    if 0 <= row < constants.ROWS and 0 <= col < constants.COLS and constants.BUTTON_FUNCTIONALITY[selected_color_index] != f"Select Algorithm ({str(len(constants.BUTTON_ALGORITHMS))})":
                        if constants.BUTTON_FUNCTIONALITY[selected_color_index] == "Erase":
                            squares = [square for square in squares if
                                       not (square['row'] == row and square['col'] == col)]
                            fill_square(screen, row, col, constants.BACKGROUND_COLOR)
                            squares.append({'row': row, 'col': col, 'color_index': 4})
                            grid_state[row][col] = False
                        else:
                            if not grid_state[row][col]:
                                fill_square(screen, row, col, button_colors[selected_color_index])
                                grid_state[row][col] = True
                                save_square(row, col, selected_color_index)

            # Checks for if the mouse is released
            elif event.type == pygame.MOUSEBUTTONUP and not start_simulation_check:
                drawing = False
            # Checks for dragging motion of mouse
            elif event.type == pygame.MOUSEMOTION and drawing and not start_simulation_check:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if constants.PADDING_X < mouse_x < constants.PADDING_X + constants.GRID_SIZE and \
                        constants.PADDING_Y < mouse_y < constants.PADDING_Y + constants.GRID_SIZE:
                    col = (mouse_x - constants.PADDING_X) // constants.SQUARE_SIZE
                    row = (mouse_y - constants.PADDING_Y) // constants.SQUARE_SIZE
                    if 0 <= row < constants.ROWS and 0 <= col < constants.COLS and constants.BUTTON_FUNCTIONALITY[selected_color_index] not in [f"Select Algorithm ({str(len(constants.BUTTON_ALGORITHMS))})", "Start Simulation"]:
                        if constants.BUTTON_FUNCTIONALITY[selected_color_index] == "Erase":
                            squares = [square for square in squares if
                                       not (square['row'] == row and square['col'] == col)]
                            grid_state[row][col] = False  # Set the state to False (erase)
                            fill_square(screen, row, col, constants.BACKGROUND_COLOR)
                            squares.append({'row': row, 'col': col, 'color_index': 4})
                            grid_state[row][col] = False
                        else:
                            if not grid_state[row][col]:
                                fill_square(screen, row, col, button_colors[selected_color_index])
                                grid_state[row][col] = True
                                save_square(row, col, selected_color_index)

        screen.blit(original_background, (0, 0))
        draw_grid(screen)

        # Draw filled squares
        for square in squares:
            fill_square(screen, square['row'], square['col'], button_colors[square['color_index']])
            draw_grid(screen)

        # Draw buttons with text
        for i, (button_area, button_color, button_control_color) in enumerate(zip(constants.BUTTON_AREA, button_colors, button_control_colors)):
            if i == selected_color_index:
                pygame.draw.rect(screen, constants.SELECTED_OUTLINE_COLOR, button_area, 3)  # Draw selected outline
            else:
                pygame.draw.rect(screen, constants.OUTLINE_COLOR, button_area, 3)  # Draw white outline
            # Draw buttons for drawing and control buttons
            if i < 4:
                pygame.draw.rect(screen, button_color, button_area, border_radius=15)
            else:
                pygame.draw.rect(screen, button_control_color, button_area, border_radius=15)

            # Render text onto the buttons
            if i < len(constants.BUTTON_FUNCTIONALITY):
                if i == 1:  # If it is start point
                    red_tiles_placed = sum(1 for square in squares if square['color_index'] == 1)
                    text = font.render(f"Start Point - {str(1 - red_tiles_placed)}", True, (255, 255, 255))
                elif i == 2:  # If it is end point
                    green_tiles_placed = sum(1 for square in squares if square['color_index'] == 2)
                    text = font.render(f"End Point - {str(1 - green_tiles_placed)}", True, (255, 255, 255))
                else:
                    text = font.render(constants.BUTTON_FUNCTIONALITY[i], True, (255, 255, 255))

                text_rect = text.get_rect(
                    midleft=(button_area[0] + button_area[2] + 10, button_area[1] + button_area[3] // 2))
                screen.blit(text, text_rect)

            # Information text:
            chosen_algorithm = font.render("Chosen Algorithm:", True, (255, 255, 255))
            text_rect = chosen_algorithm.get_rect(midleft=(55, constants.WINDOW_HEIGHT // 2 - 100))
            screen.blit(chosen_algorithm, text_rect)

            algorithm_text = font.render(selected_algorithm, True, (255, 255, 255))
            text_rect = algorithm_text.get_rect(midleft=(55, constants.WINDOW_HEIGHT // 2 - 60))
            screen.blit(algorithm_text, text_rect)

            if simulation_finished:
                result = font.render("Results:", True, (255, 255, 255))
                text_rect = result.get_rect(midleft=(100, constants.WINDOW_HEIGHT // 2 - 10))
                screen.blit(result, text_rect)

                if dist > 0:
                    result_text = font.render(f"{dist} moves to destination", True, (255, 255, 255))
                else:
                    result_text = font.render(f"End point is unreachable", True, (255, 255, 255))
                text_rect = result_text.get_rect(midleft=(35, constants.WINDOW_HEIGHT // 2 + 20))
                screen.blit(result_text, text_rect)

            # Draws lines to separate buttons
            draw_line(10, 0, 0, screen)
            draw_line(-130, -900, -895, screen)
            draw_line(-35, -895, -900, screen)

        # Check if mouse is over a button and change cursor accordingly
        for button_area in constants.BUTTON_AREA:
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
