
'''
reverse a  linked list
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

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    h,cur = head,head.next
    h.next = None
    while cur:
        _next = cur.next
        cur.next = h
        h = cur
        cur = _next

    return h

def test1():
    n1 = None
    show(n1)
    r = reverse_linked_list(n1)
    show(r)

def test2():
    n1 = Node(1)
    show(n1)
    r = reverse_linked_list(n1)
    show(r)

def test3():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    show(n1)
    r = reverse_linked_list(n1)
    show(r)

def test4():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    show(n1)
    r = reverse_linked_list(n1)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()