# You are given the root of a binary tree. Find the level for the binary tree with the
# minimum sum, and return that value.

# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and
# 4 + 1 + 2 = 7. So, the answer here should be 7.

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def minimum_level_sum(root, level):
    if root.left:
        minimum_level_sum(root.left, level+1)
    if root.right:
        minimum_level_sum(root.right, level+1)
    if level in score:
        score[level] += root.val
    else:
        score[level] = root.val

    if level == 0:
        print(score[min(score, key=score.get)])


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

score = {}

minimum_level_sum(node, 0)
