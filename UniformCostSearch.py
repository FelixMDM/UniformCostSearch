import heapq
import copy

class Node():
    def __init__(self, data, operation, depth, parent=None, cost=0):
        self.data = data
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost

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




# ----------------------------- TESTS -------------------------------------- #
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

testNode = Node(matrix, "root", 0)
testNode.printMatrix()

leftTest = leftShift(testNode)
leftTest.printMatrix()

rightTest = rightShift(testNode)
rightTest.printMatrix()

upTest = upShift(testNode)
upTest.printMatrix()

downTest = downShift(testNode)
downTest.printMatrix()