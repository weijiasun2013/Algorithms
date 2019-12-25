


def longest_consecutive_subsequence(lst):
    dct = dict()
    for ele in lst:
        dct[ele] = -1

    _max,_start = 0,0
    for k,v in dct.items():
        _next = k+1
        _length = 1
        while _next in dct:
            if dct[_next] == -1:
                _length += 1
                dct[_next] = 0
            elif dct[_next] == 0:
                break
            else:
                _length += dct[_next]
                break
            _next += 1
        dct[k] = _length

        if _max < _length:
            _max = _length
            _start = k
    return _max, _start

def main():
    lst = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    _max,_start = longest_consecutive_subsequence(lst)
    print(_max,_start)

if __name__ == '__main__':
    main()

