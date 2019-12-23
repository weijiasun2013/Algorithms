
# longest palindrome subsequence
# give a string, find out the longest palindrome subsequence

def longest_palindrome_subsequence(s):
    dp = [ [x for x in range(len(s))] for y in range(len(s))]
    for length in range(1,len(s)+1):
        for sIdx in range(0, len(s)-length+1):
            eIdx = sIdx + length - 1
            
            if length == 1:
                dp[sIdx][eIdx] = 1
            elif length == 2:
                if s[sIdx] == s[eIdx]:
                    dp[sIdx][eIdx] = 2
                else:
                    dp[sIdx][eIdx] = 1
            else:
                if s[sIdx] == s[eIdx]:
                    dp[sIdx][eIdx] = 2 + dp[sIdx+1][eIdx-1]
                else:
                    dp[sIdx][eIdx] = max(dp[sIdx+1][eIdx], dp[sIdx][eIdx-1])
    return dp[0][-1]

def main():
    s = 'abcdbfa'
    rslt = longest_palindrome_subsequence(s)
    print(rslt)

if __name__ == "__main__":
    main()

