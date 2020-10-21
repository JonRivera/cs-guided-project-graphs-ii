# Given the root node of a binary search tree, return the sum of values of all nodes
# with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
# Given
# root

# Want
# find the sum btw  nodes having values btw lower and upper inclusive

# recall
# a binary search tree has nodes to the right of the parent, which have greater value
# the nodes to the left of the parent nodes, which have less value

# Plan
#  Use a depth first search approach
# when the root is note terminate the current iteration
# if roots.value is in btw lower and upper constraints then add it to total
# include two other if statements that run int the recursion and check for wheater the current node values is either greater than lower or less than upper limit=> if so then run recusion on it

def csBSTRangeSum(root, L, R):
    total = 0

    def dfs(root):
        nonlocal total
        if root is None:
            return

        if root.value >= L and root.value <= R:
            total += root.value

        if root.value >= L:
            dfs(root.left)
        if root.value <= R:
            dfs(root.right)

    dfs(root)
    return total


# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# PROBLEM#2
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#

# Recall
# Binary trees  have at most two children nodes
# Given
# Were trying to flip the tri over a line passing directly through the root
# Plan
# Solve this problem using a binary search traversal
# When root is nothing return None
# were going to have a queue that appends the root were currently in
# Perform a while loop that runs so long as there is something in the queue
# Eventually queue will be called again if there are childs that get saved(append back into the queue),
# this will let the breadth search traveral to continue, level by level,
# If either childs of the parent node have a node then reverse the children node by setting the root.left
# and root,right equal to there opposites
# When we reverse the nodes, they keep the childs they originilly possessed
# In the end return the root which will contain the left and right branch inverted, this inverting the tree

def csBinaryTreeInvert(root):
    if not root:
        return None
    queue = []
    queue.append(root)
    while (queue):
        root1 = queue[0]
        queue = queue[1:]  # clears the queue
        if (root1.left != None or root1.right != None):
            root1.left, root1.right = root1.right, root1.left
            if (root1.left != None):
                queue.append(root1.left)
            if (root1.right != None):
                queue.append(root1.right)
    return root

from collections import deque
#def csFindAllPathsFromAToB(graph):
def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    # GIVEN
    # No cycles in the graph
    # Nodes are labeled n-1, where n are the total number of nodes
    # Graph[i] represents all the the nodes one can visit from node i
    # ---->Within this graph we have relatioships or edges
    # Which means that we find a neighboor node at index[i][j]

    # WANT find all the possible paths from node 0 to node n - 1
    # Start a node 0 and end at node n-1 and we want all the valid directed paths

    # RECALL
    # A graph consists of nodes/vertices and these nodes/vertices contain values
    # Here they are represented as labels

    # PLAN
    # Find the target label
    # For current node, check it neighboors and for each neighboor check if target is there, if itsn't recursively look into each of the neighboors neighboors and
    # When we hit base case of find the target, then append the target to

    target = len(graph) - 1
    results = []

    def backtrack(currNode, path):
        # if we reach the target, no need to explore further.
        if currNode == target:
            results.append(list(path))
            return
        # explore the neighbor nodes one after another.
        for nextNode in graph[currNode]:
            path.append(nextNode)
            # go back to 0 node when we perform path.pop by recursion ,pop .. .pop (backwards recursion)
            backtrack(nextNode, path)
            path.pop()

    # kick of the backtracking, starting from the source node (0).
    path = deque([0])
    backtrack(0, path)

    return results
