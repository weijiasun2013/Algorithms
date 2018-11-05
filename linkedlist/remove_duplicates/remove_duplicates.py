
'''
remove duplicates in linked list
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

def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    d = dict()
    cur,prev = head.next,head
    d[head.val] = 1
    while cur:
        if cur.val not in d:
            d[cur.val] = 1
            cur = cur.next
            prev = prev.next
        else:
            prev.next = cur.next
            cur = prev.next
    return head

def test1():
    n1 = None
    show(n1)
    r = remove_duplicates(n1)
    show(r)

def test2():
    n1 = Node(1)
    show(n1)
    r = remove_duplicates(n1)
    show(r)

def test3():
    n1 = Node(1)
    n2 = Node(1)
    n1.next = n2
    show(n1)
    r = remove_duplicates(n1)
    show(r)

def test4():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(1)
    n4 = Node(2)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    show(n1)
    r = remove_duplicates(n1)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()