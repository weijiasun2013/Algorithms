
class Node(object):
    def __init__(self,value):
        self.val = value
        self.next = None

def union_intersection(lnk1,lnk2):
    # given two linked list, output the union and intersection elements of them as a linked list as well
    # sequence order does not matter

    uLnk, iLnk = None, None
    p1,p2 = None, None
    d1 = dict()

    p = lnk1
    while p is not None:
        d1[p.val] = 1
        node = Node(p.val)
        if uLnk is None:
            uLnk = node
            p1 = node
        else:
            p1.next = node
            p1 = p1.next
        p = p.next

    p = lnk2
    while p is not None:
        if p.val not in d1:
            node = Node(p.val)
            if uLnk is None:
                uLnk = node
                p1 = node
            else:
                p1.next = node
                p1 = p1.next
        else:
            node = Node(p.val)
            if iLnk is None:
                iLnk = node
                p2 = node
            else:
                p2.next = node
                p2 = p2.next
        p = p.next

    return uLnk,iLnk

def show(lsk):
    rslt = ''
    p = lsk
    while p is not None:
        rslt += str(p.val) + '->'
        p = p.next
    rslt += 'null'
    print(rslt)

def main():
    lnk1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    lnk1.next = n2
    n2.next = n3
    n3.next = n4

    lnk2 = Node(11)
    _n3 = Node(3)
    lnk2.next = _n3


    show(lnk1)
    show(lnk2)
    u,i = union_intersection(lnk1,lnk2)
    show(u)
    show(i)

if __name__ == '__main__':
    main()