
# longest palindrome substring
# give a string, find out the longest palindrome substring of it

def longest_palindrome_substring(s):
    dp = [ [x for x in range(len(s))] for y in range(len(s))]
    _max,_sIdx = 0, -1

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
                    if dp[sIdx+1][eIdx-1] == (eIdx-1) - (sIdx+1) + 1:
                        dp[sIdx][eIdx] = 2 + dp[sIdx+1][eIdx-1]
                    else:
                        dp[sIdx][eIdx] = 1
                else:
                    dp[sIdx][eIdx] = 1
            if dp[sIdx][eIdx] >_max:
                _max = dp[sIdx][eIdx]
                _sIdx = sIdx
    return _max, _sIdx

def main():
    s = 'abcbcbf'
    _max,_sIdx = longest_palindrome_substring(s)
    print(s)
    print(_max,_sIdx)

if __name__ == "__main__":
    main()

