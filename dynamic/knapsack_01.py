
# 0 1 knapsack problem
# give a set of items with value and weight, give a capacity of a knapsack. 
# find out how to pick up items whose sum of weight is not beyond the knapsack's capacity and whose value is most

def knapsack01(capacity,wArr,vArr):
    dp = [ [0 for x in range(capacity+1)] for y in range(len(vArr)+1)]
    for row in range(len(vArr)+1):
        for col in range(capacity+1):
            if row == 0 or col == 0:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row-1][col]
                if wArr[row-1] <= col:
                    diff = col - wArr[row-1]
                    dp[row][col] = max(dp[row][col], vArr[row-1]+dp[row-1][diff])
    return dp[-1][-1]

def main():
    capacity = 7
    wArr = [1,2,3,4]
    vArr = [1,3,3,4]
    rslt = knapsack01(capacity,wArr,vArr)
    print(rslt)

if __name__ == "__main__":
    main()

