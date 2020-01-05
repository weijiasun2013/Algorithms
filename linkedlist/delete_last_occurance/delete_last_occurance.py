

# reserve first, then delete the iirst occurance, then reverse

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def display(node):
    n = node
    ans = ''
    while n:
        ans += str(n.val) + ' -> '
        n = n.next
    ans += 'null'
    print(ans)

def reverse(node):
    if node is None:
        return node

    head,cur = node, node.next
    head.next = None
    while cur:
        tmp = cur.next
        cur.next = head
        head = cur
        cur = tmp

    return head

def delete_last_occurance(node,item):
    _node = reverse(node)
    if _node.val == item:
        _node = _node.next
        return reverse(_node)

    pre,cur = _node,_node.next
    while cur:
        if cur.val == item:
            pre.next = cur.next
            break
        cur = cur.next
        pre = pre.next

    return reverse(_node)

def test1():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    display(n1)

    head = delete_last_occurance(n1,1)
    display(head)
    print("")

def test2():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(3)
    n6 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    display(n1)
    display(delete_last_occurance(n1,3))
    print("")

def test3():
    n1 = Node(1)
    display(n1)
    display(delete_last_occurance(n1,1))
    print("")

def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()

