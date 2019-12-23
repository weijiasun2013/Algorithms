
# shortest path
# give an mxn 2d-array, each element represent a cost, find out the minimum cost from top-left to bottom-right

def shortest_path(arr):
    dp = [0 for x in range(len(arr[0]))]

    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if row == 0 and col == 0:
                dp[col] = arr[row][col]
            elif row == 0:
                dp[col] = dp[col-1] + arr[row][col]
            elif col == 0:
                dp[col] = dp[col] + arr[row][col]
            else:
                dp[col] = min(dp[col], dp[col-1]) + arr[row][col]
    return dp[-1]

def main():
    arr = [[1, 2, 1, 2, 11],
           [1, 4, 1, 4, 12],
           [1, 5, 1, 6, 15],
           [11,12,2, 4,  1]
           ]
    rslt = shortest_path(arr)
    print(rslt)

if __name__ == "__main__":
    main()

