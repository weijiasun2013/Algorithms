
# sum2
# give aset of number and a sum, list all solutions to get sum
# no duplicates in the array, but element can bereused

import copy

def helper(src,idx,val,path,rslt):
    if idx >= len(src) or val <= 0:
        if val == 0:
            rslt.append(path)
        return

    path2 = copy.deepcopy(path)
    path2.append(src[idx])
    helper(src,idx,val-src[idx],path2,rslt)
    helper(src,idx+1,val,path,rslt)

def operation_sum(src,sum):
    rslt = []
    helper(src,0,sum,[],rslt)
    return rslt

def main():
    arr = [1,2,3,4]
    sum = 5
    rslt = operation_sum(arr,sum)
    for idx in range(len(rslt)):
        print(rslt[idx])

if __name__ == "__main__":
    main()

