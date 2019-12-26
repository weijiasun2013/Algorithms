
# sum 1:
# give a set of number and a sum, list all solutions to get the sum
# no duplicates in the array, and the element is not allowed to reuse

import copy

def helper(src,idx,val,path,rslt):
    if idx >= len(src) or val <= 0:
        if val == 0:
            rslt.append(path)
        return


    helper(src,idx+1,val,path,rslt)

    path2 = copy.deepcopy(path)
    path2.append(src[idx])
    helper(src,idx+1,val-src[idx],path2,rslt)

def operation_sum(src,sum):
    rslt = []
    helper(src,0,sum,[],rslt)
    return rslt

def main():
    arr = [1,2,3,4]
    sum = 5
    rslt = operation_sum(arr,sum)
    for row in rslt:
        print(row)

if __name__ == "__main__":
    main()

