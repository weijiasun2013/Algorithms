

def symmetric_pairs(arr):
    # Given an array of pairs, find all symmetric pairs in it

    d = dict()
    rslt = []
    for ele in arr:
        s,t = ele[0],ele[1]
        if t in d and d[t] == s:
            rslt.append(((s,t),(t,s)))
            del d[t]
        else:
            d[s] = t
    return rslt

def main():
    rslt = symmetric_pairs([(10,20), (1,2), (3,4), (4,3), (20,10)])
    print(rslt)

if __name__ == '__main__':
    main()