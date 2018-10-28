
def aPlusB_cPlusD(arr):
    # given an array, find a and b, c and d in array that a + b = c + d

    d_sum = dict()
    for idx1 in range(len(arr)-1):
        for idx2 in range(idx1+1,len(arr)):
            a,b = arr[idx1],arr[idx2]
            sum = a + b
            if sum not in d_sum:
                d_sum[sum] = (a,b)
            else:
                return (d_sum[sum]),(a,b)

    return None

def main():
    rslt = aPlusB_cPlusD([1,2,3,4,11,22])
    print(rslt)

if __name__ == '__main__':
    main()