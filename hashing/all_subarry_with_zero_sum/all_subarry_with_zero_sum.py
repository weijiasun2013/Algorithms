

def all_subarry_with_zero_sum(arr):
    # Print all subarrays with 0 sum

    d = {0:[-1]}
    sum = 0
    for idx,ele in enumerate(arr):
        sum += ele
        if sum not in d:
            d[sum] = [idx]
        else:
            d[sum].append(idx)

    rslt = []
    for k,lst in d.items():
        if len(lst) > 1:
            for sIdx in range(len(lst)-1):
                for eIdx in range(sIdx+1,len(lst)):
                    rslt.append((lst[sIdx]+1, lst[eIdx]))
    return rslt

def main():
    rslt = all_subarry_with_zero_sum([0,1,-1,0,1, 2,-1,-1])
    for r in rslt:
        print(r)

if __name__ == '__main__':
    main()