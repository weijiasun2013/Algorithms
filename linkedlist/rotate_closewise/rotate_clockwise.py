
'''
 rotate linked list (counter clock-wise)
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

def rotation(node,k):
    p = node
    _len = 1
    while p.next:
        _len += 1
        p = p.next
    p.next = node

    n = k%_len
    p1 = p
    while n > 0:
        n -= 1
        p = p.next
    head = p.next
    p.next = None

    return head

def test1():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    display(n1)
    rslt = rotation(n1,3)
    display(rslt)


def main():
    test1()



if __name__ == '__main__':
    main()

