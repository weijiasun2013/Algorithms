
# coin change with differnt number of ways
# givne a set of coins with different value and a total, count how many ways to do the change

import sys

def coin_change_num_ways(arr,total):
    dp = [ [x for x in range(total+1)] for y in range(len(arr)+1)]
    for row in range(len(arr)+1):
        for col in range(total+1):
            if row == 0 and col == 0:
                dp[row][col] = 1
            elif row == 0:
                dp[row][col] = 0
            elif col == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-1][col]
                if arr[row-1] <= col:
                    diff = col - arr[row-1]
                    dp[row][col] = dp[row][col] + dp[row][diff]
    return dp[-1][-1]

def main():
    arr = [1,2,5,10]
    total = 5
    rslt = coin_change_num_ways(arr, total)
    print(rslt)

if __name__ == "__main__":
    main()
