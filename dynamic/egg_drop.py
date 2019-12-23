
# egg drop
# ginve some number of eggs and floor, find out the miniimum steps that needs to take to find out from which floor egg will break

import sys

def egg_drop(egg,floor):
    dp = [ [f for f in range(floor+1)] for e in range(egg+1)]
    for e in range(1, egg+1):
        for f in range(1, floor+1):
            if e == 1:
                dp[e][f] = f
            elif f == 1:
                dp[e][f] = 1
            else:
                dp[e][f] = sys.maxsize
                for k in range(1,f):
                    tmp = 1 + max(dp[e-1][k-1], dp[e][f-k])
                    dp[e][f] = min(tmp, dp[e][f])
    return dp[-1][-1]

def main():
    egg = 5
    floor = 10
    rslt = egg_drop(egg,floor)
    print(rslt)

if __name__ == "__main__":
    main()

