
# rod cutting
# give a length of rod and prices at which different length of rod can sell
# determint how to cut to rod to get tme maxinum profit

def rod_cutting(length,pArr,lArr):
    dp = [ [x for x in range(length+1)] for y in range(len(pArr)+1)]
    for row in range(len(pArr)+1):
        for col in range(length+1):
            if row == 0 or col == 0:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row-1][col]
                if lArr[row-1] <= col:
                    diff = col - lArr[row-1]
                    dp[row][col] = max(dp[row][col], pArr[row-1]+dp[row][diff])
    return dp[-1][-1]

def main():
    rod = 11
    pArr = [1,3,3,4]
    lArr = [1,2,3,4]
    rslt = rod_cutting(rod,pArr,lArr)
    print(rslt)

if __name__ == "__main__":
    main()

    
