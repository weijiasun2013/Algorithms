

def missing_numbers_in_given_range(arr,low,high):
    # find missing numbers of a range, the array elements are distinct, but not sorted

    d = dict()
    for ele in arr:
        d[ele] = 1

    rslt = []
    for x in range(low,high+1):
        if x not in d:
            rslt.append(x)
    return rslt

def main():
    rslt = missing_numbers_in_given_range([12,10,15,19,11],10,15)
    print(rslt)

if __name__ == '__main__':
    main()