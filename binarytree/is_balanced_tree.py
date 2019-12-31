

'''
 balanced binary tree
 the difference between height of left and right is less than 2
 each node should be a balanced binary tree root
'''


class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def helper(root):
    if root is None:
        return 0

    left = helper(root.left)
    right = helper(root.right)
    return 1 + max(left,right)

def is_balanced_binary_tree(root):
    if root is None:
        return True

    leftHeight = helper(root.left)
    rightHeight = helper(root.right)
    if abs(leftHeight-rightHeight) < 2 and is_balanced_binary_tree(root.left) and is_balanced_binary_tree(root.right):
        return True
    return False

def test1():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.left, n1.right = n2,n3
    n2.left,n2.right = n4,n5
    n3.left, n3.right = n6, n7

    rslt = is_balanced_binary_tree(n1)
    print(rslt)

def test2():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.left,n1.right = n2,n3
    n2.left = n4
    n4.left = n5

    rslt = is_balanced_binary_tree(n1)
    print(rslt)

def test3():
  n1 = Node(1)
  n2 = Node(2)
  n3 = Node(3)
  n4 = Node(4)
  n5 = Node(5)
  n6 = Node(6)
  n7 = Node(7)

  n1.left,n1.right = n2,n3
  n2.left = n4
  n3.right = n5
  n4.left = n6
  n5.right = n7

  rslt = is_balanced_binary_tree(n1)
  print(rslt)

def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()

