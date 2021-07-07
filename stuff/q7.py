# Branch Sum


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calcBranchSums(root, 0, sums)
    return sums


def calcBranchSums(node, runningSum, sums):
    if node is None:
        return sums

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calcBranchSums(node.left, newRunningSum, sums)
    calcBranchSums(node.right, newRunningSum, sums)
