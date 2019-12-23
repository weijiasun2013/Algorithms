
# linkedlist addition

class node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

def display(node):
    n = node
    s = ''
    while n:
        s += str(n.value) + '->'
        n = n.next
    print(s)

def reverse(node):
    head, cur = node, node.next
    head.next = None
    while cur:
        next = cur.next
        cur.next = head
        head = cur
        cur = next
    return head

def helper(val1,val2,flag,head,cursor):
    v = val1 + val2 + flag
    if v > 9:
        tmp = node(v-10)
        flag = 1
    else:
        tmp = node(v)
        flag = 0

    if head is None:
        head = tmp
        cursor = head
    else:
        cursor.next = tmp
        cursor = tmp
    
    return head,cursor,flag

def addition(node1,node2):
    n1 = reverse(node1)
    n2 = reverse(node2)
    head,cursor = None, None
    flag = 0

    c1,c2 = n1,n2
    while c1 and c2:
        head,cursor,flag = helper(c1.value,c2.value,flag,head,cursor)
        c1 = c1.next
        c2 = c2.next

    if c1:
        c = c1
        while c:
            head,cursor,flag = helper(c.value,0,flag,head,cursor)
            c = c.next
    elif c2:
        c = c2
        head,cursor,flag = helper(0,c.value,flag,head,cursor)
        c = c.next

    if flag:
        head,cursor,flag = helper(0,0,flag,head,cursor)

    return reverse(head)

def main():
    n1 = node(1)
    n2 = node(2)
    n3 = node(3)
    n1.next,n2.next = n2, n3
    display(n1)

    n11 = node(9)
    n12 = node(8)
    n13 = node(7)
    n11.next,n12.next = n12, n13
    display(n11)
    ans = addition(n1,n11)
    display(ans)
    
if __name__ == "__main__":
    main()

