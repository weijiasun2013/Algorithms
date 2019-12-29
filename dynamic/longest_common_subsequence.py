
# longest common subsequence
# give two strings, return the common subsequence

def longest_common_subsequence(s1,s2):
    dp = [ [0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]
    for row in range(len(s2)+1):
        for col in range(len(s1)+1):
            if row == 0 or col == 0:
                dp[row][col] = 0
            else:
                if s1[col-1] == s2[row-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    return dp[-1][-1]

def main():
    s1 = 'abcdef'
    s2 = 'agcbcf'
    rslt = longest_common_subsequence(s1,s2)
    print(rslt)

if __name__ == "__main__":
    main()

