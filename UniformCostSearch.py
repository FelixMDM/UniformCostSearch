import heapq
import copy

GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

class Node():
    # order is data, operation, depth, parent, cost
    def __init__(self, data, operation, depth, parent=None, cost=0):
        self.data = data
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost
    def __lt__(self, other):
        return self.depth < other.depth

    #getter methods

    def get_data(self):
        return self.data
    
    def get_depth(self):
        return self.depth

    def get_cost(self):
        return self.cost

    def get_parent(self):
        return self.parent

    def get_operation(self):
        return self.operation

    #setter methods

    def set_data(self, data):
        self.data = data
    
    def set_depth(self, depth):
        self.depth = depth

    def set_cost(self, cost):
        self.cost = cost

    def set_parent(self, parent):
        self.parent = parent

    def set_operation(self, operation):
        self.operation = operation

    #helper functions - print

    def printMatrix(self):
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                print(f"{value}", end="")
            print("\n")
        print("------------------------")


# order is data, operation, depth, parent, cost
def rightShift(node):
    matrix = node.get_data()
    row, col = findIndex(matrix, 0)

    if col > 0:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row][col-1]
        currMatrix[row][col-1] = 0
        newNode = Node(currMatrix, "right", node.get_depth() + 1, node, 0)
        return newNode
    return None


def leftShift(node):
    matrix = node.get_data()
    row, col = findIndex(matrix, 0)

    if col < 2:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row][col+1]
        currMatrix[row][col+1] = 0
        newNode = Node(currMatrix, "left", node.get_depth() + 1, node, 0)
        return newNode   
    return None     

def upShift(node):
    matrix = node.get_data()
    row, col = findIndex(matrix, 0)

    if row < 2:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row+1][col]
        currMatrix[row+1][col] = 0
        newNode = Node(currMatrix, "up", node.get_depth() + 1, node, 0)
        return newNode
    return None

def downShift(node):
    matrix = node.get_data()
    row, col = findIndex(matrix, 0)

    if row > 0:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row-1][col]
        currMatrix[row-1][col] = 0
        newNode = Node(currMatrix, "down", node.get_depth() + 1, node, 0)
        return newNode
    return None

def findIndex(matrix, element):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == element:
                return i, j
    return None

def ucs(start, goal):
    startNode = Node(start, None, 0, 0)
    frontier = []
    visited = []

    heapq.heapify(frontier)
    heapq.heappush(frontier, startNode)
    while frontier:
        currentNode = heapq.heappop(frontier)
        currentNode.printMatrix()

        if currentNode.get_data() == goal:
            return currentNode
        
        rightNode = rightShift(currentNode)
        leftNode = leftShift(currentNode)
        upNode = upShift(currentNode)
        downNode = downShift(currentNode)

        if currentNode not in visited:
            heapq.heappush(visited, currentNode)

        # check if the node exists in the frontier already
        if rightNode and rightNode not in visited:
            heapq.heappush(frontier, rightNode)
        if leftNode and leftNode not in visited:
            heapq.heappush(frontier, leftNode)
        if upNode and upNode not in visited:
            heapq.heappush(frontier, upNode)
        if downNode and downNode not in visited:
            heapq.heappush(frontier, downNode)
    
    #if we make it out of the while loop then no solution exists
    return None

# ----------------------------- TESTS -------------------------------------- #
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

# testNode = Node(matrix, "root", 0)
# testNode.printMatrix()

# leftTest = leftShift(testNode)
# leftTest.printMatrix()

# rightTest = rightShift(testNode)
# rightTest.printMatrix()

# upTest = upShift(testNode)
# upTest.printMatrix()

# downTest = downShift(testNode)
# downTest.printMatrix()

ucs(matrix, GOAL_STATE)