
# longest common substring
# give two strings, find out the longest common substring

def longest_common_substring(s1,s2):
    _max,_eIdx = -1,-1
    dp = [ [0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]
    for row in range(len(s2)+1):
        for col in range(len(s1)+1):
            if row == 0 or col == 0:
                dp[row][col] = 0
            else:
                if s2[row-1] == s1[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                    if dp[row][col] > _max:
                        _max = dp[row][col]
                        _eIdx = col - 1
                else:
                    dp[row][col] = 0
    if _max > 0:
        return s1[_eIdx-_max+1:_eIdx+1]
    return 0

def main():
    s1 = 'abcdef'
    s2 = 'acbcabc'
    rslt = longest_common_substring(s1,s2)
    print(rslt)

if __name__ == "__main__":
    main()

