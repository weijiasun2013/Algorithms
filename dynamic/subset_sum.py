
# subset sum
# give a set of number and a sum, determin if the addition of some elements can reach the sum

def subset_sum(arr,sum):
    dp = [ [None for x in range(sum+1)] for y in range(len(arr)+1)]
    for row in range(len(arr)+1):
        for col in range(sum+1):
            if row == 0 and col == 0:
                dp[row][col] = True
            elif row == 0:
                dp[row][col] = False
            elif col == 0:
                dp[row][col] = True 
            else:
                dp[row][col] = dp[row-1][col]
                if col >= arr[row-1]:
                    diff = col - arr[row-1]
                    dp[row][col] |= dp[row-1][diff]
                    if dp[row][col] == True and col == sum:
                        return True
    return False

def main():
    sum = 11
    arr = [2,3,4,5]
    rslt = subset_sum(arr,sum)
    print(rslt)

if __name__ == "__main__":
    main()

