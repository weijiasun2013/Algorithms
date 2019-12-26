
# sum 3
# give a set of numbers and a sum, list all solutions to get the sum
# the set has duplicates and element is allowed to reuse

import copy

def helper(src,idx,val,path,rslt):
    if idx >= len(src) or val <= 0:
        if val == 0:
            rslt.append(path)
        return

    if idx == 0 or src[idx] != src[idx-1]:
        path2 = copy.deepcopy(path)
        path2.append(src[idx])
        helper(src,idx,val-src[idx],path2,rslt)
    helper(src,idx+1,val,path,rslt)

def operation_sum(src,sum):
    rslt = []
    helper(src,0,sum,[],rslt)
    return rslt

def main():
    arr = [1,1,2,2,3,4]
    sum = 5
    rslt = operation_sum(arr,sum)
    for row in rslt:
        print(row)

if __name__ == "__main__":
    main()

