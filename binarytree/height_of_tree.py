

'''
 height of binary tree
 max height of tree from top to the deepest node
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def heightOfTree(root):
    if root is None:
        return 0

    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)
    return 1 + max(leftHeight,rightHeight)

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.left, n1.right = n2,n3
    n2.left = n4


    rslt = heightOfTree(n1)
    print(rslt)


if __name__ == '__main__':
    main()

