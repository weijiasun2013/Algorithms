
# reserve first, then delete the iirst occurance, then reverse

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

def delete_middle(node):
    if node == Node or node.next == None:
        return None

    p1,p2 = node,node.next.next
    while p2 and p2.next:
        p2 = p2.next.next
        p1 = p1.next
    p1.next = p1.next.next

    return node

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
    rslt = delete_middle(n1)
    display(rslt)

def test2():
    rslt = delete_middle(Node)
    display(rslt)

def test3():
    n1 = Node(1)
    rslt = delete_middle(n1)
    display(rslt)

def test4():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    rslt = delete_middle(n1)
    display(rslt)

def test5():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    rslt = delete_middle(n1)
    display(rslt)

def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == '__main__':
    main()

