

'''
 root to leaf
 Given a binary tree and a sum, find if there is a path from root to leaf which sums to this sum
'''

import copy

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def helper(root,sum,path,ans):
    if root is None:
        return False

    if sum < root.val:
        return False

    if root.left is None and root.right is None:
        if root.val == sum:
            path.append(root.val)
            ans.append(path)
            return True
        return False

    _path = copy.deepcopy(path)
    _path.append(root.val)
    r1 = helper(root.left,sum-root.val,_path,ans)
    if r1:
        return r1
    r2 = helper(root.right,sum-root.val,_path,ans)
    return r2

def rootToLeaf(root,sum):
    ans = []
    rslt = helper(root,sum,[],ans)
    return rslt,ans

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.left, n1.right = n2,n3
    n2.left = n4


    rslt,ans = rootToLeaf(n1,7)
    print(rslt)
    print(ans)

if __name__ == '__main__':
    main()

