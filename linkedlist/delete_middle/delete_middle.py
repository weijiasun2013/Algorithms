
'''
delete middle of linked list
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

def delete_middle(head):
    if head is None:
        return None
    if head.next is None:
        return None

    p1,p2,prev = head,head,head
    first = True
    while p1 and p1.next:
        if first == True:
            first = False
        else:
            prev = prev.next
        p1 = p1.next.next
        p2 = p2.next

    prev.next = p2.next
    return head

def test1():
    n1 = None
    show(n1)
    r = delete_middle(n1)
    show(r)

def test2():
    n1 = Node(1)
    show(n1)
    r = delete_middle(n1)
    show(r)

def test3():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    show(n1)
    r = delete_middle(n1)
    show(r)

def test4():
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
    r = delete_middle(n1)
    show(r)

def test5():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    show(n1)
    r = delete_middle(n1)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == '__main__':
    main()