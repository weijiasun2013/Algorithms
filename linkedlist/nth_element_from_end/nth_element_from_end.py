
'''
find nth element from the end of given linked list
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

def nth_element_from_end(head,n):
    if n <= 0:
        return None

    p = head
    for i in range(n):
        if p is None:
            return None
        p = p.next

    p1 = head
    while p:
        p = p.next
        p1 = p1.next
    return p1.val

def test1():
    print('test1------------------')
    n1 = None
    show(n1)
    r = nth_element_from_end(n1,3)
    print(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    show(n1)
    r = nth_element_from_end(n1,2)
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

    show(n1)
    r = nth_element_from_end(n1,5)
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

    show(n1)
    r = nth_element_from_end(n1,1)
    print(r)

def main():#
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()