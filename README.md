# DFS-and-BFS-Visualizer

This program utilizes many different graph algorithms to efficiently find the shortest route between a start point and an end point. This tool will allow you to create your own custom maze, and watch how the different algorithm finds its way through to the goal.

## How to Install:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RECodeVault/DFS-and-BFS-Visualizer.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd DFS-and-BFS-Visualizer
    ```
    
3. **Install dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

4. **Start the application:**
    ```bash
    python main.py
    ```

## How to use:
1. There will be a list of buttons on the right side of the grid. You can choose to create your own maze using three buttons: Walls, Start point, End point, and Erase.
2. If you do not want to create your own maze, on the left side of the grid you can choose the Random maze button to create a random maze.
3. Once you have a maze made, navigate over to the "Select Algorithm" Option.
4. Once inside the menu you can choose your desired algorithm here 
5. Explore around the menu! There are detailed descriptions for all algorithms as well as a helpful button at the bottom to redirect you to an in depth YouTube video!
6. Once you have your desired algorithm select the "Apply" option to save it!
7. When one of the algorithms are chosen, click the Start simulation button and watch the magic happen as the algorithm finds its way through the maze.
8. Once the simulation is finished, you can click the Reset button to try it again.

## Examples of running program:

### Setting up the program:
![Running program](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGljY3M2MXd2ZmRod3ptbmg5ZHNidml6MGVyZDAzdHYxdXJxcDY4NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p4Z6LCj6K1KDSmy4Gg/giphy.gif)

### Running Program:
![Running program](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnF4cDQweng2MzFya2F3eHhnMWJqNndzNjE4aGkzOXlqaXJidTYwbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZrpcB8eh58RVrP52UO/giphy.gif)

# BFS and DFS algorithm:

## What is DFS?

Depth-First Search (DFS) is a graph traversal algorithm used to explore and analyze graphs or trees. It starts at a designated "root" node and explores as far as possible along each branch before backtracking.

### Steps of DFS:

1. DFS begins at a selected starting node.
2. It explores as far as possible along each branch before backtracking.
3. If a dead end is reached or all adjacent nodes have been visited, it backtracks to the most recent node with unexplored options.
4. DFS traverses the entire graph, ensuring that all reachable nodes are visited.

### Example of DFS:
![DFS diagram](https://www.interviewbit.com/blog/wp-content/uploads/2021/12/DFS-Algorithm-800x620.png)


## What is BFS?

Breadth-First Search (BFS) is another graph traversal algorithm used to explore and analyze graphs or trees. Unlike DFS, which explores as far as possible along each branch before backtracking, BFS explores all nodes at the current depth before moving to the next level.

### Steps of BFS:

1. BFS begins at a selected starting node.
2. It explores all neighbor nodes at the current depth level before moving to the next depth level.
3. BFS systematically explores nodes level by level, ensuring that nodes closer to the starting point are visited first.
4. BFS typically uses a queue data structure to keep track of the nodes to be explored, ensuring that nodes are visited in the order they were discovered.
5. BFS traverses the entire graph, ensuring that all reachable nodes are visited.

### Example of BFS:
![BFS diagram](https://cdn.hackr.io/uploads/posts/attachments/41Y3Tl3kaPqGDVBPKFjJ1dYYrA33iss48iMklm7h.png)

# Future implementation:

- Adding algorithms like:
- Dijkstra's algorithm
- A* algorithm
- Greedy Best-First Search
- Bellman-Ford Algorithm
- Flood Fill Algorithm

# Change-log:

- Completely reworked the algorithm choosing process
- Added new menu (Select Algorithm)
- Added Description for each algorithm
- Added a button link at the bottom that redirects to YouTube video on certain algorithm
- Redesigned button colors
