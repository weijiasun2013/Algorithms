
# sum2
# give aset of number and a sum, list all solutions to get sum
# no duplicates in the array, but element can bereused

import copy

def helper(arr,idx,curSum,path,rslt):
    if idx >= len(arr) or curSum <= 0:
        if curSum == 0:
            rslt.append(path)
        return

    path2 = copy.deepcopy(path)
    path2.append(arr[idx])
    helper(arr,idx,curSum-arr[idx],path2,rslt)
    helper(arr,idx+1,curSum,path,rslt)

def operation_sum(arr,sum):
    rslt = []
    helper(arr,0,sum,[],rslt)
    return rslt

def main():
    arr = [1,2,3,4]
    sum = 5
    rslt = operation_sum(arr,sum)
    for idx in range(len(rslt)):
        print(rslt[idx])

if __name__ == "__main__":
    main()

