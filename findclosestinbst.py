def findClosestValueInBst(tree, target):
    return findClosestHelper(tree, target, tree.value)


def findClosestHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestHelper(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
