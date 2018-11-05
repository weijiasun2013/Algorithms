
'''
remove loop in linked list
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

def remove_loop(head):
    p1,p2 = head,head
    found = False
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            found = True
            break
    if found == False:
        return head

    p = head
    while p != p1:
        p = p.next
        p1 = p1.next

    p.next = None
    return head

def test1():
    print('test1------------------')
    n1 = None
    show(n1)
    r = remove_loop(n1)
    show(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    show(n1)
    r = remove_loop(n1)
    show(r)

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

    r = remove_loop(n1)
    show(r)

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

    r = remove_loop(n1)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()