import heapq
import copy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

class Node():
    # order is data, operation, depth, parent, cost
    def __init__(self, data, operation, depth, parent=None, cost=0, heuristic=0):
        self.data = data
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost
        self.heuristic = heuristic
    def __lt__(self, other):
        return (self.cost, self.heuristic) < (other.cost, other.heuristic)

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
    
    def get_heuristic(self):
        return self.heuristic

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

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    #helper functions - print

    def printMatrix(self):
        # for i, row in enumerate(self.data):
        #     for j, value in enumerate(row):
        #         print(f"{value}", end="")
        #     print("\n")
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                print(f"{value} ", end="")
                if j < 2:
                    print("| ", end="")
            print()
            if i < 2:
                print("-" * 9)
        print("\n")


# these functions perform the 4 operations that we can do within the 8 puzzle
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

#helper function that allows us to locate the index of the empty space - used by the 4 above
def findIndex(matrix, element):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == element:
                return i, j
    return None

# euclidean distance heuristic function used in A* search
def euclideanHeuristic(currState, goal):
    totalDistance = 0
    for i in range(3):
        for j in range(3):
            tile = currState[i][j]
            if tile != 0:
                # find position of tile in goal state
                goal_i, goal_j = findIndex(goal, tile)
                # calculate euclidean distance and add it to the total
                totalDistance += ((goal_i - i) ** 2 + (goal_j - j) ** 2) ** 0.5
    return totalDistance

# A* search algorithm with euclidean distance heuristic
def aStar(start, goal):
    #define the starting node to consist of the starter matrix 'start,' iterations 0, define frontier & visited arrays
    startNode = Node(start, None, 0, 0) 
    iterations = 0
    frontier = []
    visited = []

    #heapify to ensure that the smallest cost node is always first to be processed & push 
    heapq.heapify(frontier)
    heapq.heappush(frontier, startNode)
    while frontier:
        #while the frontier is not empty, set currentnode to be a [deepcopy] of the top node, pop the node we copied from frontier (we are visiting it)
        currentNode = copy.deepcopy(heapq.heappop(frontier))
        print(f"CurrentNode: {currentNode.get_data()} | Iteration: {iterations}")

        #if this current node is the goal state, return that
        if currentNode.get_data() == goal:
            print("\n")
            print(f"** SOLVED **")
            print("\n")
            return currentNode

        if currentNode.get_data() not in [node.get_data() for node in visited]:
            visited.append(currentNode)

            rightNode = rightShift(currentNode)
            leftNode = leftShift(currentNode)
            upNode = upShift(currentNode)
            downNode = downShift(currentNode)

            for node in [rightNode, leftNode, upNode, downNode]:
                if node:
                    # calculate cost for the child node and heuristic
                    node.set_heuristic(euclideanHeuristic(node.get_data(), goal))
                    node.set_cost(currentNode.get_cost() + 1)
                    # add child node to the frontier
                    heapq.heappush(frontier, node)

        iterations += 1

    return None

def main():
    print("------------------------------------------- UCS -------------------------------------------\n")

    print("Enter 9 integers separated by spaces to represent the 3x3 matrix:\n")

    matrix = []
    for i in range(3):
        a = []
        for j in range(3):
            a.append(int(input()))
        matrix.append(a)

    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end = " ")
        print()

    soln = aStar(matrix, GOAL_STATE)

    if soln:
        soln.printMatrix()

    else:
        print(f"No Solution")

    print("------------------------------------------- TRACE -------------------------------------------")

    trace_node = copy.deepcopy(soln)

    while trace_node.get_parent():
        print(f"Move to get here: {trace_node.get_operation()}")
        trace_node.printMatrix()
        trace_node = trace_node.get_parent()

# ----------------------------- TESTS -------------------------------------- #
# matrix = [
#     [1, 2, 3],
#     [4, 8, 0],
#     [7, 6, 5]
# ]

if __name__ == "__main__":
    main()