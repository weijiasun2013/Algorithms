

'''
 level order print
 Program to print tree in level order fashion.
'''


class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def helper(root,level,ans):
    if root is None:
        return

    if len(ans) < level + 1:
        ans.append([])
    ans[level].append(root.val)

    helper(root.left,level+1,ans)
    helper(root.right,level+1,ans)

def level_order(root):
    ans = []
    helper(root,0,ans)
    return ans

def main():
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

    ans = level_order(n1)
    print(ans)

if __name__ == '__main__':
    main()

