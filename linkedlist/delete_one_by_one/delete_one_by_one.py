
'''
delete a linked list, one by one element
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

def delete_one_by_one(head):
    while head:
        _next = head.next
        del head
        head = _next
    return head

def test1():
    print('test1------------------')
    n1 = None

    show(n1)
    r = delete_one_by_one(n1)
    show(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    n2 = Node(2)

    n1.next = n2

    show(n1)
    r = delete_one_by_one(n1)
    show(r)

def main():#
    test1()
    test2()

if __name__ == '__main__':
    main()