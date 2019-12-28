
'''
remove elements in linked list whose sum is equal to zero

Strategy description:
    Since it is linked list, not an array, using dict only is not enough when deleting.
    we use a stack and a queue, insert all position node in stack,
    if got negative node, count sum with past positive nodes and move them from stack to quene
    if sum got zero, delete all positive nodes directly from queue,
    if sum never got zero when stack was consumed, move all from queue to stack
 
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

def remove_elements_with_zero_sum(head):
    start = head
    _stack = list()
    _lst = list()
    while start:
        if start.val > 0:
            _stack.append(start)
        else:
            sum = start.val
            flag = False
            while len(_stack) > 0:
                temp = _stack[-1]
                del _stack[-1]
                _lst.append(temp)
                sum += temp.val
                if sum == 0:
                    flag = True
                    _lst = []
                    break
            if flag == False:
                for ele in _lst:
                    _stack.append(ele)
                _stack.append(start)
        start = start.next

    for idx in range(len(_stack)-1):
        _stack[idx].next = _stack[idx+1]
    h1 = None
    if len(_stack) > 0:
        h1 = _stack[0]
        _stack[-1].next = None
    return h1

def test1():
    print('test1------------------')
    n1 = Node(6)
    n2 = Node(-6)
    n3 = Node(6)
    n4 = Node(8)
    n5 = Node(4)
    n6 = Node(-12)
    n7 = Node(9)
    n8 = Node(8)
    n9 = Node(-8)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9

    show(n1)
    r = remove_elements_with_zero_sum(n1)
    show(r)

def test2():
    # 4, 6, -10, 8, 9, 10, -19, 10, -18, 20, 25
    print('test1------------------')
    n1 = Node(4)
    n2 = Node(6)
    n3 = Node(-10)
    n4 = Node(8)
    n5 = Node(9)
    n6 = Node(10)
    n7 = Node(-19)
    n8 = Node(10)
    n9 = Node(-18)
    n10 = Node(20)
    n11 = Node(25)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9
    n9.next = n10
    n10.next = n11

    show(n1)
    r = remove_elements_with_zero_sum(n1)
    show(r)

def main():#
    test1()
    test2()
if __name__ == '__main__':
    main()
