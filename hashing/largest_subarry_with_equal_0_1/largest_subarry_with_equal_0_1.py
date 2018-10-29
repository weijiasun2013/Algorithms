
def largest_subarry_with_equal_0_1(arr):
    # given an array, find the largest subarray with equal number of 0's and 1's

    d = {0:-1}  # befor index 0 (index -1), the sum is 0
    sum = 0
    ans,low,high = 0,None,None
    for idx,ele in enumerate(arr):
        if ele == 1:
            sum += 1
        else:
            sum -= 1
        if sum not in d:
            d[sum] = idx
        else:
            length = idx - d[sum]
            if length > ans:
                ans = length
                low,high = d[sum]+1,idx
    return ans, (low,high)

def main():
    rslt1 = largest_subarry_with_equal_0_1([1,1,0,0])
    print(rslt1)

    rslt2 = largest_subarry_with_equal_0_1([1,1,1,0,0,1,0,1,1])
    print(rslt2)
if __name__ == '__main__':
    main()