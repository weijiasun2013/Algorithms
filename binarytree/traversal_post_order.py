'''
 binary search tree - post proder traversal
 left,right,node
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def traversal_post_order(root):
    if root is None:
        return
   
    traversal_post_order(root.left)
    traversal_post_order(root.right)
    print(root.val)

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.left,n1.right = n2,n3
    n2.left,n2.right = n4,n5
    n3.left,n3.right = n6, n7

    traversal_post_order(n1)

if __name__ == '__main__':
    main()

