
# isoland
# give an arry with value 0 and 1 only, 0 represents sea and 1 represent land
# determin how many isolands in the given array

def helper(row,col,arr,visited):
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return
    if arr[row][col] == 0:
        return

    arr[row][col] = 0
    visited.append((row,col))

    helper(row-1,col,arr,visited)
    helper(row+1,col,arr,visited)
    helper(row,col-1,arr,visited)
    helper(row,col+1,arr,visited)

def isoland(arr):
    visited = []
    ans = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == 1:
                helper(row,col,arr,visited)
                ans += 1
    
    for idx in range(len(visited)):
        row,col = visited[idx]
        arr[row][col] = 1

    return ans

def main():
    arr = [
            [1,1,0,0],
            [1,0,0,1],
            [0,0,1,1],
            [1,0,1,1]
            ]
    rslt = isoland(arr)
    print(rslt)

if __name__ == "__main__":
    main()

