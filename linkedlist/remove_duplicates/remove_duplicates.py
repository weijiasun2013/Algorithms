
'''
remove duplicates in sorted linked list
if unsorted, need a dictionary to support when processing the value
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
    p = head
    while p and p.next:
        if p.val == p.next.val:
            _next = p.next.next
            p.next = _next
        else:
            p = p.next
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




def main():#
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
