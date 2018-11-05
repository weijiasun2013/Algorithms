
'''
delete last occurance of an item in linked list
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

def delete_last_occurance(head,item):
    if head is None:
        return head

    p1,p2,prev1,prev2 = head,None,None,None
    flag1 = True    # run p1 if True, else run p2
    while (p1 and flag1) or (p2 and flag1 == False):
        if flag1:
            if p1.val == item:
                flag1 = False
                p2 = p1.next
                prev2 = p1
            else:
                p1 = p1.next
                if prev1 is None:
                    prev1 = head
                else:
                    prev1 = prev1.next
        else:   #run p2
            if p2.val == item:
                flag1 = True
                p1 = p2.next
                prev1 = p2
            else:
                p2 = p2.next
                if prev2 is None:
                    prev2 = head
                else:
                    prev2 = prev2.next
    if flag1:
        if p2 and prev2:
            prev2.next = p2.next
    else:
        if prev1:
            prev1.next = p1.next
        else:
            head = p1.next
    return head

def test1():
    print('test1------------------')
    n1 = None
    show(n1)
    r = delete_last_occurance(n1,1)
    show(r)

def test2():
    print('test2------------------')
    n1 = Node(1)
    show(n1)
    r = delete_last_occurance(n1,1)
    show(r)

def test3():
    print('test3------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(1)
    n4 = Node(2)
    n5 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    show(n1)
    r = delete_last_occurance(n1,1)
    show(r)

def test4():
    print('test4------------------')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    show(n1)
    r = delete_last_occurance(n1,6)
    show(r)

def test5():
    print('test5------------------')
    n1 = Node(1)
    n2 = Node(2)

    n1.next = n2
    show(n1)
    r = delete_last_occurance(n1,3)
    show(r)

def main():#
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == '__main__':
    main()