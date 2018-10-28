

def checkPair(arr,n):
    # given an array and a number n, check if there exits a pair of elements whose sum is equal to n
    # return the first pair meets requirement

    d = dict()
    for idx,ele in enumerate(arr):
        r = n - ele
        if r in d:
            return (r, ele)
        d[ele] = idx
    return None

def main():
    rslt = checkPair([1,2,3,4], 7)
    print(rslt)

if __name__ == '__main__':
    main()