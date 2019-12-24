

def all_subarry_with_zero_sum(arr):
    # Print all subarrays with 0 sum

    d = dict()
    sum = 0
    for idx,ele in enumerate(arr):
        sum += ele
        if sum not in d:
            d[sum] = [idx]
        else:
            d[sum].append(idx)

    rslt = []
    for k,lst in d.items():
        if k == 0:
            tmp = [-1] + lst
        else:
            tmp = lst
        if len(tmp) == 2:
            print(tmp[0]+1,tmp[1])
        elif len(tmp) > 2:
            for sIdx in range(len(tmp)-1):
                for eIdx in range(sIdx+1,len(tmp)):
                    rslt.append((tmp[sIdx]+1, tmp[eIdx]))
    return rslt

def main():
    rslt = all_subarry_with_zero_sum([0,1,-1,0,1, 2,-1,-1])
    for r in rslt:
        print(r)

if __name__ == '__main__':
    main()
