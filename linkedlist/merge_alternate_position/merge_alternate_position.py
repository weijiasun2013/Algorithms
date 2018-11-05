
'''
merge alternate position
'''

class Node(object):
    def __init__(self,value):
        self.val = value
        self.next = None

def show(head):
    h = head
    rslt = ''
    while h:
        rslt += str(h.val) + ' -> '
        h = h.next
    rslt += 'null'
    print(rslt)

def merge_alnernate_position(head1,head2):
    p1= head1
    while p1 and head2:
        _next2 = head2.next
        _next1 = p1.next

        p1.next = head2
        head2.next = _next1
        p1 = _next1
        head2 = _next2

    return head1, head2

def test1():
    print('test1------------------')
    n1 = None

    n11 = Node(1)
    n12 = Node(2)

    n11.next = n12

    show(n1)
    show(n11)
    r1,r2 = merge_alnernate_position(n1,n11)
    show(r1)
    show(r2)

def test2():
    print('test2------------------')
    n11 = None

    n1 = Node(1)
    n2 = Node(2)

    n1.next = n2

    show(n1)
    show(n11)
    r1,r2 = merge_alnernate_position(n1,n11)
    show(r1)
    show(r2)

def test3():
    print('test3------------------')
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2

    n11 = Node(11)
    n12 = Node(12)

    n11.next = n12

    show(n1)
    show(n11)
    r1,r2 = merge_alnernate_position(n1,n11)
    show(r1)
    show(r2)

def test4():
    print('test4------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    n11 = Node(11)
    n12 = Node(12)

    n11.next = n12

    show(n1)
    show(n11)
    r1,r2 = merge_alnernate_position(n1,n11)
    show(r1)
    show(r2)

def test5():
    print('test5------------------')
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2

    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)
    n14 = Node(14)

    n11.next = n12
    n12.next = n13
    n13.next = n14

    show(n1)
    show(n11)
    r1,r2 = merge_alnernate_position(n1,n11)
    show(r1)
    show(r2)

def main():#
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == '__main__':
    main()