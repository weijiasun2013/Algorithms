

'''
 symmetric tree
 mirror image rule
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def helper(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False

    return helper(root1.left,root2.right) and helper(root1.right,root2.left)

def is_symmetric(root):
    if root is None:
        return True
    return helper(root.left,root.right)

def test1():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(3)
    n5 = Node(4)
    n6 = Node(4)
    n7 = Node(3)
    n1.left, n1.right = n2,n3
    n2.left,n2.right = n4,n5
    n3.left,n3.right = n6,n7

    rslt = is_symmetric(n1)
    print(rslt)

def main():
    test1()

if __name__ == '__main__':
    main()

