
# need to improve

import sys

def longest_consecutive_subsequence(arr):
    # Given an array of integers, find the length of the longest sub-sequence
    # such that elements in the subsequence are consecutive integers, the consecutive
    # numbers can be in any order.

    d = dict()
    _min, _max = sys.maxsize, -sys.maxsize
    for ele in arr:
        d[ele] = 1
        _max = max(_max,ele)
        _min = min(_min, ele)

    aux = dict()
    length,low,high = 0,None,None
    for ele in d.keys():
        _low,_high = ele,ele + 1
        cnt = 1
        while _high <= _max:
            if _high in aux:
                aux[_low] = cnt + aux[_high]
                if length < aux[_low]:
                    length = aux[_low]
                    low,high = _low, _low + aux[_low] - 1
                break
            elif _high in d:
                cnt += 1
                aux[_low] = cnt
                if length < aux[_low]:
                    length = aux[_low]
                    low,high = _low,_low + aux[_low] - 1
            else:
                break
            _high += 1

    return length,(low,high)

def main():
    length,rng = longest_consecutive_subsequence([1, 19, 3, 10, 4, 20, 2,21,23,22])
    print(length,rng)

if __name__ == '__main__':
    main()