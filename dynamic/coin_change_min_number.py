
# coin change with minimum numbers
# given a set of coins with different value and a total, pick up minimum number of coins whose sum equals total
# the same coin could only be picked up one time for each time

import sys

def coin_change_min_number(arr,total):
    dp = [ [x for x in range(total+1)] for y in range(len(arr)+1) ]
    for row in range(len(arr)+1):
        for col in range(total+1):
            if row == 0 and col == 0:
                dp[row][col] = 0
            elif row == 0:
                dp[row][col] = sys.maxsize
            elif col == 0:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row-1][col]
                if arr[row-1] <= col:
                    diff = col - arr[row-1]
                    dp[row][col] = min(dp[row][col], 1+dp[row-1][diff])
    return dp[-1][-1]

def main():
    arr = [1,2,5,10]
    total = 17
    rslt = coin_change_min_number(arr, total)
    print(rslt)

if __name__ == "__main__":
    main()
