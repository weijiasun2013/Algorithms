
'''
add 1 to a number that was represented by a linked list
1 -> 2 -> 3 -> null: 124
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

def helper(val,flag,pnt,prev):
    v = val + flag
    if v > 9:
        v = v - 10
        flag = 1
    else:
        flag = 0
    pnt.val = v
    prev = pnt

    return pnt,flag,prev


def add_one(head):
    if head is None:
        return Node(1)

    h1 = reverse(head)
    pnt,flag,prev = h1,1,None
    while pnt:
        pnt,flag,prev = helper(pnt.val,flag,pnt,prev)
        pnt = pnt.next
    if flag:
        n = Node(flag)
        prev.next = n
    return reverse(h1)

def test1():
    n1 = None
    show(n1)
    r = add_one(n1)
    show(r)
    print("")

def test2():
    n1 = Node(9)
    show(n1)
    r = add_one(n1)
    show(r)
    print("")

def test3():
    n1 = Node(1)
    n2 = Node(9)
    n1.next = n2
    show(n1)
    r = add_one(n1)
    show(r)
    print("")

def test4():
    n1 = Node(2)
    n2 = Node(9)
    n3 = Node(9)
    n4 = Node(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    show(n1)
    r = add_one(n1)
    show(r)
    print("")

def main():
    test1()
    test2()
    test3()
    test4()

if __name__ == "__main__":
    main()

