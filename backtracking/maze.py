
# maze problem
# give a 2d array, each element's value represents the pace size by which it can reach in four directions
# determin if there is a path from the top-left to the central point, if so display it

import copy

def helper(arr,visited,row,col,path,rslt):
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return

    cenX,cenY = int(len(arr)/2),  int(len(arr[0])/2)
    if row == cenX and col == cenY:
        path2 = copy.deepcopy(path)
        path2.append((cenX,cenY))
        rslt.append(path2)
        return
    if visited[row][col] == 1:
        return

    visited[row][col] = 1
    path2 = copy.deepcopy(path)
    path2.append((row,col))
    pace = arr[row][col]
    helper(arr,visited,row-pace,col,path2,rslt)
    helper(arr,visited,row+pace,col,path2,rslt)
    helper(arr,visited,row,col-pace,path2,rslt)
    helper(arr,visited,row,col+pace,path2,rslt)

def maze(arr):
    rslt = []
    visited = [ [0 for x in range(len(arr[0]))] for y in range(len(arr))]
    helper(arr,visited,0,0,[],rslt)
    return rslt

def main():
    arr = [
            [1,2,3],
            [3,0,3],
            [2,1,4]
            ]
    rslt = maze(arr)
    for idx in range(len(rslt)):
        print(rslt[idx])

if __name__ == "__main__":
    main()


