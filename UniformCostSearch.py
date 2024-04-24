import heapq

class Node():
    def __init__(self, data, parent=None, cost=0):
        self.data = data
        self.parent = parent
        self.cost = cost
        self.children = []

    def expand(self):
        self.leftMove()
        self.rightMove()
        self.upMove()
        self.downMove()     

    def leftMove(self):
        for i in range(3):
            for j in range(3):
                if self.data[i][j] == '*' and j < 2:
                    new_node = Node(self.data)

                    new_node.data[i][j] = new_node.data[i][j+1]
                    new_node.data[i][j+1] = '*'

                    # print("leftMove: \n")
                    # new_node.printMatrix()
                    # print("---")

                    self.children.append(new_node)
                    break

    def rightMove(self):
        for i in range(3):
            for j in range(3):
                if self.data[i][j] == '*' and j > 0:
                    new_node = Node(self.data)

                    new_node.data[i][j] = new_node.data[i][j-1]
                    new_node.data[i][j-1] = '*'

                    # print("rightMove: \n")
                    # new_node.printMatrix()
                    # print("---")

                    self.children.append(new_node)
                    break
                
    def upMove(self):
        for i in range(0, 2):
            for j in range(0, 2):
                if self.data[i][j] == '*' and i < 2:
                    new_node = Node(self.data)

                    new_node.data[i][j] = new_node.data[i+1][j]
                    new_node.data[i+1][j] = '*'

                    # print("upMove: \n")
                    # new_node.printMatrix()
                    # print("---")

                    self.children.append(new_node)
                    break  

    def downMove(self):
        for row in range(3):
            for col in range(3):
                if self.data[row][col] == '*':
                    new_node = Node(self.data)

                    new_node.data[row][col] = new_node.data[row-1][col]
                    new_node.data[row-1][col] = '*'

                    # print("downMove: \n")
                    # new_node.printMatrix()
                    # print("---")

                    self.children.append(new_node)
                    break

    def printMatrix(self):
        for i in range(3):
            for j in range(3):
                print(self.data[i][j], end="")
            print("\n")

    def printChildren(self):
        if not self.children:
            print("No Children")
            return
        
        for child in self.children:
            child.printMatrix()
            print("---")

def rightShift(node) {
    row, col = findIndex(node, 0)
}

def findIndex(matrix, element):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == element:
                return i, j
    return None

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

element_to_find = 4
index = find_index(matrix, element_to_find)

if index:
    print(f"Element {element_to_find} found at index: {index}")
else:
    print(f"Element {element_to_find} not found in the matrix.")


# d = Node(matrix)

# d.printMatrix()

# print("---------down--------\n")

# d.downMove()
# d.printMatrix()

# print("-------up----------\n")

# d.upMove()
# d.printMatrix()

# print("----------left--------\n")

# d.leftMove()
# d.printMatrix()

# print("---------right----------\n")

# d.rightMove()
# d.printMatrix()