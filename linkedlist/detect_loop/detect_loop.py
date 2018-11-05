
'''
detect loop in linked list
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

def detect_loop(head):

    p1,p2 = head, head
    while p2 and p2.next:
        p2 = p2.next.next
        p1 = p1.next
        if p1 == p2:
            return True
    return False

def test1():
    print('test1------------------')
    n1 = None
    show(n1)
    r = detect_loop(n1)
    print(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    show(n1)
    r = detect_loop(n1)
    print(r)

def test3():
    print('test3------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1

    r = detect_loop(n1)
    print(r)

def test4():
    print('test4------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3

    r = detect_loop(n1)
    print(r)

def main():#
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()