
'''
keep M nodes and delete N nodes, continously do it until getting the ending
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def show(node):
    if node is None:
        print('null')
        return

    rslt = ''
    n = node
    while n:
        rslt += str(n.val) + " -> "
        n = n.next
    rslt += ' null '
    print(rslt)

def reverse(node):
    if node is None:
        return node

    head,cur = node,node.next
    head.next = None
    while cur:
        tmp = cur.next
        cur.next = head
        head = cur
        cur = tmp
    return head

def delete_n_nodes_after_m_nodes(head,m,n):
    if m == 0:
        return None
    if n == 0:
        return head
    prev,cur = None,head
    keep = True
    count = m
    while cur:
        if keep:
            prev = cur
            cur = cur.next
            count -= 1
            if count == 0:
                count = n
                keep = False
        else:
            tmp = cur.next
            prev.next = tmp
            cur = tmp
            count -= 1
            if count == 0:
                count = m
                keep = True

    return head

def test1():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    show(n1)
    m,n = 2,1
    print("m:",m,"n:",n)
    rslt = delete_n_nodes_after_m_nodes(n1,m,n)
    show(rslt)

def main():
    test1()


if __name__ == "__main__":
    main()

