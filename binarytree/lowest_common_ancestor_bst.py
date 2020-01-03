

'''
 lowest common ancestor in binary search tree
 since binary search tree has rule: left_val < node_val <= right_val
 we can solve the it from root to leaf
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root,node1,node2):
    n = root
    while n:
        if node1.val == n.val or node2.val == n.val:
            return n
        elif min(node1.val,node2.val) > n.val:
            n = n.right
        elif max(node1.val,node2.val) < n.val:
            n = n.left
        else:
            return n
    return None

def test1():
    n1 = Node(10)
    n2 = Node(5)
    n3 = Node(15)
    n4 = Node(1)
    n5 = Node(8)
    n6 = Node(12)
    n7 = Node(20)
    n1.left, n1.right = n2,n3
    n2.left,n2.right = n4,n5
    n3.left, n3.right = n6, n7

    rslt = lowest_common_ancestor(n1,n4,n7)
    if rslt:
        print(rslt.val)
    else:
        print(rslt)

def main():
    test1()

if __name__ == '__main__':
    main()

