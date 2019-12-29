
# longest increasing subsequence
# give an array, find out the longest increasing subsequence

def longest_increasing_subsequence(arr):
    dp = [1 for x in range(len(arr))]
    _max = 0
    for idx in range(1,len(arr)):
        for pIdx in range(idx):
            if arr[pIdx] < arr[idx] and dp[pIdx] + 1 > dp[idx]:
                dp[idx] = dp[pIdx] + 1
                _max = max(_max,dp[idx])
    return _max

def main():
    arr = [2,3,1,8,4,5]
    rslt = longest_increasing_subsequence(arr)
    print(rslt)

if __name__ == "__main__":
    main()

