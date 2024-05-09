# Graph-Algorithm-Visualizer

This program utilizes many different graph algorithms to efficiently find the shortest route between a start point and an endpoint. This tool will allow you to create your own custom maze, and watch how the different algorithm finds their way through to the goal.

## How to Install:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RECodeVault/Graph-Algorithm-Visualizer.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Graph-Algorithm-Visualizer
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
7. When one of the algorithms is chosen, click the Start simulation button and watch the magic happen as the algorithm finds its way through the maze.
8. Once the simulation is finished, you can click the Reset button to try it again.

## Examples of running program:

### Setting up the program:
![Setting up program](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnFjdzNqbjhkazkxYXFiOWhmMzhlODUwNzJ4cTY2Y2hydHR1bnhtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vqvOJdiCbm0pBMcK2y/giphy.gif)

### Running Program:
![Running program(A*)](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXpkeHQ4ZnBvcjBvMXd2Y3luOXZsa2hsbnlqeGt3czNvZ2E4bXp0NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4povkk8QqNAWwZerEV/giphy.gif)

![Running program(Dijkstra)](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHI2OGgyajAxNmNuNTYyaGp6d2l3a3RieXp3cnVlbXhzYXBnbDZxdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kR2bJJjb2AnGA2CPck/giphy.gif)

# Algorithms implemented:

## What is DFS?

Depth-First Search (DFS) is a graph traversal algorithm used to explore and analyze graphs or trees. It starts at a designated "root" node and explores as far as possible along each branch before backtracking.

### Example of DFS:
![DFS diagram](https://www.interviewbit.com/blog/wp-content/uploads/2021/12/DFS-Algorithm-800x620.png)

## What is BFS?

Breadth-First Search (BFS) is another graph traversal algorithm used to explore and analyze graphs or trees. Unlike DFS, which explores as far as possible along each branch before backtracking, BFS explores all nodes at the current depth before moving to the next level.

### Example of BFS:
![BFS diagram](https://cdn.hackr.io/uploads/posts/attachments/41Y3Tl3kaPqGDVBPKFjJ1dYYrA33iss48iMklm7h.png)

## What is dijkstra's Algorithm?

Dijkstra's algorithm is a fundamental method in computer science used to find the shortest path between nodes in a graph.
This algorithm efficiently calculates the shortest path from a starting node to all other nodes in a graph. 
It works by iteratively exploring nodes in the graph, greedily selecting the node with the shortest known distance 
from the starting node at each step. Through this process, it gradually builds a shortest-path tree rooted at the 
starting node, ultimately yielding the shortest paths to all other nodes.

### Example of dijkstra's Algorithm:
![Dijkstra's algorithm diagram](https://www.researchgate.net/profile/Atta-Ur-Rehman-6/publication/331484960/figure/fig1/AS:732550733512704@1551665113143/Illustration-of-Dijkstras-algorithm.ppm)

## What is A*?

A* is guided by a heuristic function (h(n)) that estimates the cost of reaching the goal from any given node. 
The quality of this heuristic significantly affects the efficiency and accuracy of A*. A* is guaranteed to find the 
shortest path. Overall, A* is efficient and effective for finding optimal paths in many scenarios, 
although its performance can vary depending on factors like the size and complexity 
of the graph and the quality of the heuristic function.

### Example of A*:
![A* diagram](https://www.101computing.net/wp/wp-content/uploads/A-Star-Search-Algorithm.png)

## What is Greedy Best-First-Search?

Greedy Best-First Search (GBFS) employs a heuristic-based approach to guide its search process. 
Specifically, it utilizes a Euclidean heuristic, which estimates the distance between a current state 
and the goal state in terms of straight-line distance. 
This heuristic serves as the basis for the evaluation function, informing GBFS about the proximity of each node to the goal. 
By prioritizing nodes based on this heuristic evaluation, GBFS tends to explore paths that appear to be closer to the goal 
state in terms of straight-line distance.

### Example of Greedy Best-First-Search:
![Greedy Best-First-Search diagram](https://raw.githubusercontent.com/Codecademy/docs/main/media/greedy-best-first-search-tree-3.png)

# Future implementation:

- Adding algorithms like:
- Bellman-Ford Algorithm
- Flood Fill Algorithm

# Change-log:

- Added 3 new algorithms
- Added shortest path visual
- Bug fixes
- Updated font style
