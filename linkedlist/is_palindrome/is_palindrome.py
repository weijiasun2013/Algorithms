'''
check if the linkedlist is palindrome
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def display(node):
    if node is None:
        print('null')
        return

    n = node
    ans = ''
    while n:
        ans += str(n.val) + ' -> '
        n = n.next
    ans += 'null'
    print(ans)

def is_palindrome(node):
    _stack = list()
    p = node
    while p:
        _stack.append(p.val)
        p = p.next
    if len(_stack) == 0:
        return True

    idx1,idx2 = 0,len(_stack)-1
    while idx1 < idx2:
        if _stack[idx1] != _stack[idx2]:
            return False
        idx1 += 1
        idx2 -= 1

    return True


def test1():
    display(None)
    print(is_palindrome(None))

def test2():
    n1 = Node(1)
    display(n1)
    print(is_palindrome(n1))

def test3():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(1)
    n1.next = n2
    n2.next = n3
    display(n1)
    print(is_palindrome(n1))

def test4():
    n1 = Node(1)
    n2 = Node(1)
    n1.next = n2
    display(n1)
    print(is_palindrome(n1))

def test5():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    display(n1)
    print(is_palindrome(n1))

def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == '__main__':
    main()

