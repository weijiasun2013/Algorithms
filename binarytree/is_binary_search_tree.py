

'''
 checking if the tree is binary search BinaryTree
 left_val < node_val <= right_val
'''

import sys

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def helper(root,minVal,maxVal):
    if root is None:
        return True
    if root.val <= minVal or root.val > maxVal:
        return False

    return helper(root.left,minVal,root.val) and helper(root.right,root.val,maxVal)

def isBST(root):
    return helper(root,-sys.maxsize,sys.maxsize)

def main():
    n1 = Node(10)
    n2 = Node(5)
    n3 = Node(15)
    n4 = Node(1)
    n5 = Node(6)
    n6 = Node(12)
    n7 = Node(20)
    n1.left,n1.right = n2,n3
    n2.left,n2.right = n4,n5
    n3.left,n3.right = n6, n7

    rslt = isBST(n1)
    print(rslt)

if __name__ == '__main__':
    main()

