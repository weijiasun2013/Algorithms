
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

def delete_n_nodes_after_m_nodes(node,m,n):
    if m == 0:
        return None
    if n == 0:
        return node

    p1 = node
    flag = True
    sum = m - 1
    while p1:
        display(node)
        if flag:
            if sum > 0:
                sum -= 1
                p1 = p1.next
            elif sum == 0:
                flag = False
                sum = n
        else:
            if sum > 0:
                if p1 and p1.next:
                    tmp = p1.next
                    p1.next = tmp.next
                    sum -= 1
                else:
                    break
            else:
                flag = True
                sum = m - 1
                p1 = p1.next

    return node

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    rslt = delete_n_nodes_after_m_nodes(n1,2,1)
    display(rslt)


if __name__ == '__main__':
    main()

