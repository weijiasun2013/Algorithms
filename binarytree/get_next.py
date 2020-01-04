

'''
 get the next value in binary search tree
 given a node in a BST, using left,right and up pointer to get the node
 whose value is next bigger to the current

 if the current is already the biggest, then navigat the smallest one
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.up = None

def helper(root):
    n = root
    while n.up and n.up.right == n:
        n = n.up

    if n.up:
        return n.up
    else:
        while n.left:
            n = n.left
        return n

def get_next(root,node):
    if root is None or node is None:
        return None

    # condition 1
    if node.right:
        n = node.right
        while n.left:
            n = n.left
        return n
    else:
        n = helper(node)
        return n

def test1():
    n1 = Node(8)
    n2 = Node(4)
    n3 = Node(12)
    n4 = Node(2)
    n5 = Node(6)
    n6 = Node(10)
    n7 = Node(14)
    n8 = Node(1)
    n9 = Node(3)
    n10 = Node(5)
    n11 = Node(7)
    n12 = Node(9)
    n13 = Node(11)
    n14 = Node(13)
    n15 = Node(15)

    n1.left, n1.right = n2,n3
    n2.left,n2.right,n2.up = n4,n5,n1
    n3.left,n3.right,n3.up = n6,n7,n1
    n4.left,n4.right,n4.up = n8,n9,n2
    n5.left,n5.right,n5.up = n10,n11,n2
    n6.left,n6.right,n6.up = n12,n13,n3
    n7.left,n7.right,n7.up = n14,n15,n3

    n8.up,n9.up = n4,n4
    n10.up,n11.up = n5,n5
    n12.up,n13.up = n6,n6
    n14.up,n15.up = n7,n7

    print('current: ',n1.val,"answer: ", get_next(n1,n1).val)
    print('current: ',n2.val,"answer: ", get_next(n1,n2).val)
    print('current: ',n3.val,"answer: ", get_next(n1,n3).val)
    print('current: ',n4.val,"answer: ", get_next(n1,n4).val)
    print('current: ',n5.val,"answer: ", get_next(n1,n5).val)
    print('current: ',n6.val,"answer: ", get_next(n1,n6).val)
    print('current: ',n7.val,"answer: ", get_next(n1,n7).val)
    print('current: ',n8.val,"answer: ", get_next(n1,n8).val)
    print('current: ',n9.val,"answer: ", get_next(n1,n9).val)
    print('current: ',n10.val,"answer: ", get_next(n1,n10).val)
    print('current: ',n11.val,"answer: ", get_next(n1,n11).val)
    print('current: ',n12.val,"answer: ", get_next(n1,n12).val)
    print('current: ',n13.val,"answer: ", get_next(n1,n13).val)
    print('current: ',n14.val,"answer: ", get_next(n1,n14).val)
    print('current: ',n15.val,"answer: ", get_next(n1,n15).val)


def main():
    test1()

if __name__ == '__main__':
    main()

