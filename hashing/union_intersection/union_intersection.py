class Node(object):
    def __init__(self,value):
        self.val = value
        self.next = None

def show(lsk):
    rslt = ''
    p = lsk
    while p is not None:
        rslt += str(p.val) + '->'
        p = p.next
    rslt += 'null'
    print(rslt)

def helper(val,link,pnt):
    node = Node(val)
    if link:
        pnt.next = node
        pnt = node
    else:
        link = node
        pnt = node
    return link,pnt

def union_intersection(lnk1,lnk2):
    # given two linked list, output the union and intersection elements of them as a linked list as well
    # sequence order does not matter

    uLnk, iLnk = None, None
    p1,p2 = None, None

    d1 = dict()

    p = lnk1
    while p:
        d1[p.val] = 1
        uLnk,p1 = helper(p.val,uLnk,p1)
        p = p.next

    p = lnk2
    while p:
        if p.val not in d1:
            d1[p.val] = 1
            uLnk,p1 = helper(p.val,uLnk,p1)
        else:
            iLnk,p2 = helper(p.val,iLnk,p2)
        p = p.next

    return uLnk,iLnk

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
    print("")
    show(u)
    show(i)

if __name__ == '__main__':
    main()

