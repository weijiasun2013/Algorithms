
# combination
# give a set of numbers, list all combination with different order

import copy

def helper(src,tgt,rslt):
    if len(src) == 0:
        rslt.append(tgt)
        return

    for idx in range(len(src)):
        tgt2 = copy.deepcopy(tgt)
        tgt2.append(src[idx])
        src2 = copy.deepcopy(src)
        del src2[idx]
        helper(src2,tgt2,rslt)

def combination(arr):
    rslt = []
    helper(copy.deepcopy(arr),[],rslt)
    return rslt

def main():
    arr = [1,2,3]
    rslt = combination(arr)
    for idx in range(len(rslt)):
        print(rslt[idx])

if __name__ == "__main__":
    main()

