

def largest_zero_sum_subarray(arr):
    # given an array, find the larget subarray whose sum is zero

    dct_pre_sum = dict()
    sum = 0
    length,rslt = 0,None
    for idx,ele in enumerate(arr):
        sum += ele
        if sum not in dct_pre_sum:
            dct_pre_sum[sum] = idx
        else:
            l = idx - dct_pre_sum[sum]
            if l > length:
                length = l
                rslt = (dct_pre_sum[sum]+1,idx)
    return length, rslt

def main():
    length,rng = largest_zero_sum_subarray([-1,1,2,3,-1,-1,-1,2,1,-1])
    print(length,rng)

if __name__ == '__main__':
    main()