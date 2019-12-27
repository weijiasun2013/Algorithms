
'''
  merge two sorted linked list
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


def merge_two_sorted_lnks(node1,node2):
    rslt,cur = None,None
    p1,p2 = node1,node2

    while p1 and p2:
        if p1.val < p2.val:
            if rslt is None:
                rslt = p1
                cur = p1
            else:
                cur.next = p1
                cur = cur.next
            p1 = p1.next
        else:
            if rslt is None:
                rslt = p2
                cur = p2
            else:
                cur.next = p2
                cur = p2
            p2 = p2.next

    if p1:
        cur.next = p1
    elif p2:
        cur.next = p2

    return rslt

def test1():
    n11 = Node(1)
    n12 = Node(5)
    n11.next = n12

    n21 = Node(2)
    n22 = Node(3)
    n23 = Node(11)
    n21.next = n22
    n22.next = n23
    display(n11)
    display(n21)
    display(merge_two_sorted_lnks(n11,n21))

def main():
    test1()



if __name__ == '__main__':
    main()

