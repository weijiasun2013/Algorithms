

def count_subarray_with_given_xor(arr,m):
    # count the number of subarrays having a given xor

    d = {0:-1}  #initial befor index 0 (index -1)
    xor = 0
    rng,rslt = [],[]
    for idx,ele in enumerate(arr):
        if ele == m and idx != 0:   # idx == 0 case will be checked by initial index -1, otherwise duplicates
            rng.append((idx,idx))
        xor = xor ^ ele
        if xor not in d:
            d[xor] = idx
        other = xor ^ m
        if other in d:
            rng.append((d[other]+1,idx))

    for r in rng:
        rslt.append(arr[r[0]:r[1]+1])
    return len(rslt),rslt

def main():
    c1,rslt1 = count_subarray_with_given_xor([4, 2, 2, 6, 4],6)
    print(c1,': ',rslt1)

    c2,rslt2 = count_subarray_with_given_xor([5, 6, 7, 8, 9],5)
    print(c2,': ',rslt2)

if __name__ == '__main__':
    main()