'''
  given a set, try to separate the set into two whose difference is minimum
'''


def subest_minimum_diff(lst):
    sum = 0
    for ele in lst:
        sum += ele

    dp = [ [None for x in range(1+sum)] for y in range(1+len(lst))]
    for row in range(1+len(lst)):
        for col in range(1+sum):
            if row == 0 and col == 0:
                dp[row][col] = True
            elif row == 0:
                dp[row][col] = False
            elif col == 0:
                dp[row][col] = True
            else:
                dp[row][col] = dp[row-1][col]
                if col >= lst[row-1]:
                    diff = col - lst[row-1]
                    dp[row][col] |= dp[row][diff]

    idx = int((sum+1)/2)
    while idx >= 0:
        if dp[-1][idx] == True:
            break
        idx -= 1

    rslt = abs(idx-(sum-idx))
    return rslt

def main():
    lst = [1,2,3,4,5]
    rslt = subest_minimum_diff(lst)
    print(rslt)

if __name__ == '__main__':
    main()

