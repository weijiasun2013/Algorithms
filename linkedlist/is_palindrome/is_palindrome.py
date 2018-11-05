
'''
check if the linked list is palindrome
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

def is_palindrome(head):
    if head is None:
        return True

    _stack = list()
    h,cur = head,head.next
    h.next = None
    _stack.append(head.val)
    while cur:
        _stack.append(cur.val)
        _next = cur.next
        cur.next = h
        h = cur
        cur = _next

    h1,cur1 = h,h.next
    h1.next = None
    if h1.val != _stack[0]:
        return False
    del _stack[0]
    while cur1:
        if cur1.val != _stack[0]:
            return False
        del _stack[0]
        _next = cur1.next
        cur1.next = h1
        h1 = cur1
        cur1 = _next

    return True

def test1():
    print('test1------------------')
    n1 = None
    show(n1)
    r = is_palindrome(n1)
    print(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    show(n1)
    r = is_palindrome(n1)
    print(r)

def test3():
    print('test3------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(2)
    n5 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    show(n1)
    r = is_palindrome(n1)
    print(r)

def test4():
    print('test4------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(3)
    n5 = Node(2)
    n6 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    show(n1)
    r = is_palindrome(n1)
    print(r)

def test5():
    print('test5------------------')
    n1 = Node(1)
    n2 = Node(2)

    n1.next = n2
    show(n1)
    r = is_palindrome(n1)
    print(r)

def main():#
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == '__main__':
    main()