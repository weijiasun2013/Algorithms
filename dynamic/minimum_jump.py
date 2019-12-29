
# minimum jump
# starts from an array's beginning, count the minimum steps to get the array's end
# the value of each element represents the maximum span from the current index

import sys

def minimum_jump(arr):
    dp = [sys.maxsize for x in range(len(arr))]
    dp[0] = 0

    for idx in range(1, len(arr)):
        for pIdx in range(idx):
            if pIdx + arr[pIdx] >= idx and dp[pIdx] + 1 < dp[idx]:
                    dp[idx] = dp[pIdx] + 1
    return dp[-1]

def main():
    arr = [2,3,1,1,2,4,2,0,1,1]
    rslt = minimum_jump(arr)
    print(rslt)

if __name__ == "__main__":
    main()

