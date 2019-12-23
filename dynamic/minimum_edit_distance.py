
# minimum edit distance
# give two strings, how to get the minimum steps to edit them to the same
# each operation on edition could be create, delete or change a letter

def minimum_edit_distance(s1,s2):
    dp = [ [x for x in range(len(s1)+1)] for y in range(len(s2)+1)]

    for row in range(len(s2)+1):
        for col in range(len(s1)+1):
            if row == 0 and col == 0:
                dp[row][col] = 0
            elif row == 0:
                dp[row][col] = col
            elif col == 0:
                dp[row][col] = row
            else:
                if s1[col-1] == s2[row-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = 1 + min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])
    return dp[-1][-1]

def main():
    s1 = 'abc'
    s2 = 'dc'
    rslt = minimum_edit_distance(s1,s2)
    print(rslt)

if __name__ == "__main__":
    main()

