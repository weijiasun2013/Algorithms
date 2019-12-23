
# sum 1:
# give a set of number and a sum, list all solutions to get the sum
# no duplicates in the array, and the element is not allowed to reuse

import copy

def helper(arr,idx,curSum,path,rslt):
    if idx >= len(arr) or curSum <= 0:
        if curSum == 0:
            rslt.append(path)
        return


    helper(arr,idx+1,curSum,path,rslt)

    path2 = copy.deepcopy(path)
    path2.append(arr[idx])
    helper(arr,idx+1,curSum-arr[idx],path2,rslt)

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

