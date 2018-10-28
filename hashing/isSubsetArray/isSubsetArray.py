

def isSubsetArray(a1,a2):
    # check if a2 is a subset of a1
    # no duplicates in a1 or a2

    d1 = dict()
    for a in a1:
        d1[a] = 1

    for a in a2:
        if a not in d1:
            return False
    return True

def main():
    rslt1 = isSubsetArray([1,2,3,4,5], [1,3])
    print(rslt1)

    rslt2 = isSubsetArray([1,2,3,4,5], [1,6])
    print(rslt2)

if __name__ == '__main__':
    main()