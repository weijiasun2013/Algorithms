

'''
 lowest common ancestor in binary tree (value of each node is arbitrary)
 traversal the tree, if got the object node then return it. otherwise return None
 judge the ancestor based on return object
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root,node1,node2):
    if root is None:
        return None
    if root == node1 or root == node2:
        return root

    left = lowest_common_ancestor(root.left,node1,node2)
    right = lowest_common_ancestor(root.right,node1,node2)

    if left and right:
        return root
    elif left:
        return left
    else:
        return right

def test1():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.left, n1.right = n2,n3
    n2.left,n2.right = n4,n5
    n3.left,n3.right = n6,n7

    rslt = lowest_common_ancestor(n1,n2,n7)
    print(rslt.val)

def main():
    test1()

if __name__ == '__main__':
    main()

