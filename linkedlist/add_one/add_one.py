
'''
add 1 to a number that was represented by a linked list
1 -> 2 -> 3 -> null: 124
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

def add_one(head):
    if head is None:
        n = Node(1)
        return n

    r = reverse_linked_list(head)
    p = r
    ans = 1
    while p:
        v = p.val + ans
        ans = 0
        if v > 9:
            v -= 10
            ans = 1
        p.val = v
        if p.next is None:
            if ans > 0:
                n = Node(ans)
                ans = 0
                p.next = n
        p = p.next

    r2 = reverse_linked_list(r)
    return r2

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
    r = add_one(n1)
    show(r)

def test2():
    n1 = Node(9)
    show(n1)
    r = add_one(n1)
    show(r)

def test3():
    n1 = Node(1)
    n2 = Node(9)
    n1.next = n2
    show(n1)
    r = add_one(n1)
    show(r)

def test4():
    n1 = Node(2)
    n2 = Node(9)
    n3 = Node(9)
    n4 = Node(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    show(n1)
    r = add_one(n1)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()