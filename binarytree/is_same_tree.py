

'''
 checking if two binary trees are the same
 value,structure
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isSameTree(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False

    return isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.left, n1.right = n2,n3

    n11 = Node(1)
    n12 = Node(2)
    n13 = Node(3)
    n11.left, n11.right = n12,n13

    rslt = isSameTree(n1,n11)
    print(rslt)
    

if __name__ == '__main__':
    main()

