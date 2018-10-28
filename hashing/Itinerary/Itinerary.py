

def Itinerary(dct):
    # given a dictionary of a travel, find the path from beginning to ending
    
    fSet,tSet = set(),set()
    for k,v in dct.items():
        fSet.add(k)
        tSet.add(v)
    s = list(fSet - tSet)[0]

    rslt = []
    c = s
    rslt.append(s)
    while c in dct:
        rslt.append(dct[c])
        c = dct[c]
    return rslt

def show(lst):
    for idx in range(len(lst)-1):
        print(lst[idx],'-->', lst[idx+1])

def main():
    dct = {'city1':'city2','city2':'city3','city3':'target','start':'city1'}
    rslt = Itinerary(dct)
    show(rslt)

if __name__ == '__main__':
    main()