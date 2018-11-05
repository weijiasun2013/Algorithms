
'''
delete n nodes after m nodes in linked list
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

def delete_n_nodes_after_m_nodes(head,m,n):
    c1,c2 = m,n
    p,prev = head,None
    while c1 > 0:
        c1 -= 1
        p = p.next
        if prev is None:
            prev = head
        else:
            prev = prev.next
    p2 = p
    while c2 > 0:
        c2 -= 1
        p2 = p2.next

    if prev is None:
        return p2
    else:
        prev.next = p2
        return head

def test1():
    print('test1------------------')
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
    r = delete_n_nodes_after_m_nodes(n1,2,2)
    show(r)

def test2():
    print('test2------------------')
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
    r = delete_n_nodes_after_m_nodes(n1,0,3)
    show(r)

def test3():
    print('test3------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3
    show(n1)
    r = delete_n_nodes_after_m_nodes(n1,0,3)
    show(r)

def main():#
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()