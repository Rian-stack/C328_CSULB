#

class OceanNode:
    def __init__(self, animal = set(), left = None, right = None):
        self.animal = animal
        self.left = left
        self.right = right

def ocean_explore (area, our_animal):
    found_depths = []
    depth = 0
    stack = [(area, depth)]

    while stack:
        currentNode, depth = stack.pop()

        #checks node 
        if our_animal.issubset(currentNode.animal):
            found_depths.append(depth)

        #pushes left and right child nodes
        if currentNode.right:
            stack.append((currentNode.right, depth + 1))
        if currentNode.left:
            stack.append((currentNode.left, depth + 1))

    if len(found_depths) != 0:
        found_depths.sort()
        return (True, found_depths[0])
    
    return (False, 0)
