import math
from collections import defaultdict
from queue import PriorityQueue


class Node:
    def __init__(self, x : int, y : int, h : int) -> None:
        self.x = x
        self.y = y
        self.neighbors : list[Node]
        
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
def distance(p1 : Node, p2 : Node) -> float:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    
def manhattan_distance(p1, p2) -> float:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)
    
def reconstruct_path(came_from : dict, current : list[Node]):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path
    
def A_star(start: Node, goal : Node) -> list[Node]:
    openSet : PriorityQueue[Node] = PriorityQueue()
    came_from = dict()
    g_score : defaultdict[Node, float] = defaultdict(lambda : float('inf'))
    f_score : defaultdict[Node, float] = defaultdict(lambda : float('inf'))
    
    while not openSet.empty():
        current = openSet.get()
        
        
        for neighbor in current.neighbors:
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + 1
                if neighbor not in openSet.queue:
                    openSet.put(neighbor)
    
    return list()

input_file = open("day12.txt")

nodemap : list[list[Node]] = list()
x = 0
y = 0
for line in input_file:
    current_line_heights : list[Node] = list()
    for char in line.strip():
        if char == 'S':
            height = 1
        elif char == 'E':
            height = 26
        else:
            height = ord(char) - 96
        current_line_heights.append(Node(y, x, height)) #-96 maps 'a' to 1 and 'z' to 26
        if len(str(height)) == 2:
            print(height, end=' ')
        else:
            print('0' + str(height), end=' ')
        
        x += 1
    nodemap.append(current_line_heights)
    print('\n')
    
    y += 1

#doing it again to compute neighbors
y = 0
x = 0
for line in nodemap:
    for curr_node in line:
        if x - 1 >= 1:
            curr_node.neighbors.append(nodemap[y][x - 1])
        if x + 1 <= len(line):
            curr_node.neighbors.append(nodemap[y][x + 1])
        if y + 1 <= len(nodemap):
            curr_node.neighbors.append(nodemap[y + 1][x])
        if y - 1 >= 1:
            curr_node.neighbors.append(nodemap[y - 1][x])
        x += 1
    y += 1
    
