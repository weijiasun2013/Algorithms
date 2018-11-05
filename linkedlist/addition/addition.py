
'''
addition of two numbersthat are represented by a linked list
1 -> 2 -> 3 -> null: 124
9 -> 8 -> null: 98
result: 2 -> 2 -> 2 -> null
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

def addition(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    r1 = reverse_linked_list(head1)
    r2 = reverse_linked_list(head2)

    rslt,p3 = None,None
    p1,p2 = r1,r2
    ans = 0
    while p1 and p2:
        v = p1.val + p2.val + ans
        ans = 0
        if v > 9:
            v -= 10
            ans = 1
        if rslt is None:
            rslt = Node(v)
            p3 = rslt
        else:
            p3.next = Node(v)
            p3 = p3.next
        p1,p2 = p1.next, p2.next

    def fun(pSrc,pRslt,a):
        p = pSrc
        ans = a
        while p:
            v = p.val + ans
            ans = 0
            if v > 9:
                v -= 10
                ans = 1
            pRslt.next = Node(v)
            pRslt = pRslt.next
            if p.next is None:
                if ans > 0:
                    pRslt.next = Node(ans)
                    pRslt = pRslt.next
            p = p.next
    if p1:
        fun(p1,p3,ans)
    elif p2:
        fun(p2,p3,ans)
    elif ans > 0:
        p3.next = Node(ans)
        p3 = p3.next

    rslt = reverse_linked_list(rslt)
    return rslt

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
    print('test1------------------')
    n1,n2 = None,None
    show(n1)
    show(n2)
    r = addition(n1,n2)
    show(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    n2 = None
    show(n1)
    show(n2)
    r = addition(n1,n2)
    show(r)

def test3():
    print('test3------------------')
    n1 = None
    n2 = Node(1)
    show(n1)
    show(n2)
    r = addition(n1,n2)
    show(r)


def test4():
    print('test4------------------')
    n1 = Node(9)
    n2 = Node(9)

    show(n1)
    show(n2)
    r = addition(n1,n2)
    show(r)

def test5():
    print('test4------------------')
    n1 = Node(2)
    n2 = Node(9)
    n3 = Node(9)

    n1.next = n2
    n2.next = n3

    n11 = Node(1)
    n12 = Node(8)
    n11.next = n12
    
    show(n1)
    show(n11)
    r = addition(n1,n11)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == '__main__':
    main()