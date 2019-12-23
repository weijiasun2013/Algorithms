
# subset
# give a set of number, list all subsets of it

import copy

def helper(arr,idx,path,rslt):
    rslt.append(path)
    if idx >= len(arr):
        return

    for i in range(idx,len(arr)):
        path2 = copy.deepcopy(path)
        path2.append(arr[i])
        helper(arr,i+1,path2,rslt)

def subset(arr):
    rslt = []
    helper(arr,0,[],rslt)
    return rslt

def main():
    arr = [1,2,3]
    rslt = subset(arr)
    for idx in range(len(rslt)):
        print(rslt[idx])

if __name__ == "__main__":
    main()

