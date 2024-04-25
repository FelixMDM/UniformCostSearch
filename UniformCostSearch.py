import heapq
import copy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
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
    if matrix == GOAL_STATE:
        print(matrix)

    if col > 0:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row][col-1]
        currMatrix[row][col-1] = 0
        newNode = Node(currMatrix, "right", node.get_depth() + 1, node, node.get_cost() + 1)
        return newNode
    return None


def leftShift(node):
    matrix = node.get_data()
    row, col = findIndex(matrix, 0)
    if matrix == GOAL_STATE:
        print(matrix)

    if col < 2:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row][col+1]
        currMatrix[row][col+1] = 0
        newNode = Node(currMatrix, "left", node.get_depth() + 1, node, node.get_cost() + 1)
        return newNode   
    return None     

def upShift(node):
    matrix = node.get_data()
    row, col = findIndex(matrix, 0)
    if matrix == GOAL_STATE:
        print(matrix)

    if row < 2:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row+1][col]
        currMatrix[row+1][col] = 0
        newNode = Node(currMatrix, "up", node.get_depth() + 1, node, node.get_cost() + 1)
        return newNode
    return None

def downShift(node):
    matrix = node.get_data()
    row, col = findIndex(matrix, 0)
    if matrix == GOAL_STATE:
        print(matrix)

    if row > 0:
        currMatrix = copy.deepcopy(matrix)
        currMatrix[row][col] = currMatrix[row-1][col]
        currMatrix[row-1][col] = 0
        newNode = Node(currMatrix, "down", node.get_depth() + 1, node, node.get_cost() + 1)
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
    iterations = 0
    frontier = []
    visited = []

    heapq.heapify(frontier)
    heapq.heappush(frontier, startNode)
    while frontier:
        currentNode = copy.deepcopy(heapq.heappop(frontier))
        print(f"CurrentNode: {currentNode.get_data()} | Iteration: {iterations}")

        if currentNode.get_data() == goal:
            print(f"solved")
            return currentNode
        
        rightNode = rightShift(currentNode)
        leftNode = leftShift(currentNode)
        upNode = upShift(currentNode)
        downNode = downShift(currentNode)

        # rightNode.printMatrix()
        # leftNode.printMatrix()
        # upNode.printMatrix()
        # downNode.printMatrix()

        # if currentNode not in visited:
        heapq.heappush(visited, currentNode)

        # check if the node exists in the frontier already
        if rightNode and rightNode.get_data() not in [node.get_data() for node in visited] :
            heapq.heappush(frontier, rightNode)
        if leftNode and leftNode.get_data() not in [node.get_data() for node in visited]:
            heapq.heappush(frontier, leftNode)
        if upNode and upNode.get_data() not in [node.get_data() for node in visited]:
            heapq.heappush(frontier, upNode)
        if downNode and downNode.get_data() not in [node.get_data() for node in visited]:
            heapq.heappush(frontier, downNode)    
    #if we make it out of the while loop then no solution exists
        iterations += 1
    return None

# ----------------------------- TESTS -------------------------------------- #
matrix = [
    [1, 0, 3],
    [4, 2, 6],
    [7, 5, 8]
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

# testNode = Node(matrix, "start", 0)

# list = []
# list.append(testNode)

# otherNode = copy.deepcopy(heapq.heappop(list))

# if not (any(otherNode.get_data() for node in list)):
#     print(f"True for {matrix} and {testNode.get_data()}")
# else:
#    print(f"Matrix {matrix} exists within list")

soln = ucs(matrix, GOAL_STATE)

if soln:
    print(f"{soln.get_data()}")
else:
    print(f"No Solution")