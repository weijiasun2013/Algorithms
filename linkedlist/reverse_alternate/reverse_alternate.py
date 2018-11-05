
'''
reverse alternate in linked list
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

def reverse_alternate(head,k):
    rFlag,cnt = False,k
    p,prev,rH,rTail = head,None,None,None
    while p:
        if rFlag == False:
            p = p.next
            if prev is None:
                prev = head
            else:
                prev = prev.next
            cnt -= 1
            if cnt == 0:
                rFlag = True
                cnt = k
        else:   # doing reverse
            if cnt == k:
                rH = p
                p = p.next
                rH.next = None
                rTail = rH
            else:
                _next = p.next
                p.next = rH
                rH = p
                p = _next
            cnt -= 1
            if cnt == 0:
                prev.next = rH
                rTail.next = p
                prev = rTail
                rFlag = False
                cnt = k

    if rFlag and cnt < k:
        prev.next = rH
        rTail.next = None
    return head

def test1():
    print('test1------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9

    show(n1)
    r = reverse_alternate(n1,3)
    show(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9

    show(n1)
    r = reverse_alternate(n1,6)
    show(r)

def test3():
    print('test3------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8

    show(n1)
    r = reverse_alternate(n1,4)
    show(r)

def test4():
    print('test4------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9
    n9.next = n10

    show(n1)
    r = reverse_alternate(n1,4)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()