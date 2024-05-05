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

def ucs(start, goal):
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

        print(f"CurrentNode: {currentNode.get_data()} | Cost: {currentNode.get_cost()} | Nodes expanded: {iterations}")

        #if this current node is the goal state, return that
        if currentNode.get_data() == goal:
            print("\n")
            print(f"** SOLVED **")
            print("\n")
            return currentNode
        
        #not goal state -> expand all 4 possible operations to get children [left, right, up, down], any impossible operations will return a value of None
        rightNode = rightShift(currentNode)
        leftNode = leftShift(currentNode)
        upNode = upShift(currentNode)
        downNode = downShift(currentNode)

        # if currentNode not in visited, add it to list of visited nodes (ensure we never repeat states):
        heapq.heappush(visited, currentNode)

        '''
        remember how we established that only valid operations will generate children for us to explore?
        here we check if any of those 4 produced a valid state AND whether we have already expanded this child state before (already exists in visited)

        essentially chechking for existence and uniqueness of the currentnodes children

        if the children exist AND are unique, append them to the frontier -> we will visit/expand them in time
        '''
        if rightNode and rightNode.get_data() not in [node.get_data() for node in visited] :
            heapq.heappush(frontier, rightNode)
        if leftNode and leftNode.get_data() not in [node.get_data() for node in visited]:
            heapq.heappush(frontier, leftNode)
        if upNode and upNode.get_data() not in [node.get_data() for node in visited]:
            heapq.heappush(frontier, upNode)
        if downNode and downNode.get_data() not in [node.get_data() for node in visited]:
            heapq.heappush(frontier, downNode)    
        iterations += 1

    #if we manage to make it out of the while loop somehow that must mean we've expanded all nodes in frontier and found NO solution, therefore none exists
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

    soln = ucs(matrix, GOAL_STATE)

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
