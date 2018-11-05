
'''
flattening a linked list
'''

class Node(object):
    def __init__(self,value):
        self.val = value
        self.right = None
        self.down = None

def show_down(head):
    h = head
    rslt = ''
    while h:
        rslt += str(h.val) + ' -> '
        h = h.down
    rslt += 'null'
    print(rslt)

def show_right(head):
    h = head
    rslt = ''
    while h:
        rslt += str(h.val) + ' -> '
        h = h.right
    rslt += 'null'
    print(rslt)

def merge(a,b):
    if a is None:
        return b
    elif b is None:
        return a

    rslt = None
    p1,p2 = a,b
    while p1 and p2:
        if p1.val < p2.val:
            if rslt is None:
                rslt = p1
                cur = p1
            else:
                cur.down = p1
                cur = cur.down
            p1 = p1.down
        else:
            if rslt is None:
                rslt = p2
                cur = p2
            else:
                cur.down = p2
                cur = cur.down
            p2 = p2.down

    if p1:
        cur.down = p1
    elif p2:
        cur.down = p2
    return rslt

def flattening(root):
    if root is None or root.right is None:
        return root

    root.right = flattening(root.right)
    root = merge(root,root.right)
    return root

def test_merge():
    print('test merge------------------')
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n1.down = n2
    n2.down = n3

    n4 = Node(2)
    n5 = Node(4)
    n6 = Node(6)

    n4.down = n5
    n5.down = n6

    show_down(n1)
    show_down(n4)
    r = merge(n1,n4)
    show_down(r)

def test1():
    '''
    5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
    :return:
    '''
    print('test1------------------')
    n11,n12,n13,n14 = Node(5),Node(7),Node(8),Node(30)
    n21,n22 = Node(10),Node(20)
    n31,n32,n33 = Node(19),Node(22),Node(50)
    n41,n42,n43,n44 = Node(28),Node(35),Node(40),Node(45)

    n11.down = n12
    n12.down = n13
    n13.down = n14
    n21.down = n22
    n31.down = n32
    n32.down = n33
    n41.down = n42
    n42.down = n43
    n43.down = n44

    n11.right = n21
    n21.right = n31
    n31.right = n41

    root = flattening(n11)
    show_down(root)

def main():#
    test_merge()
    test1()

if __name__ == '__main__':
    main()