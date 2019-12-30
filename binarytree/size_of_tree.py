

'''
 size of BinaryTree
 count non-empty nodes
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def sizeOfTree(root):
    if root is None:
        return 0
    return 1 + sizeOfTree(root.left) + sizeOfTree(root.right)

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.left, n1.right = n2,n3
    n2.left = n4


    rslt = sizeOfTree(n1)
    print(rslt)


if __name__ == '__main__':
    main()

