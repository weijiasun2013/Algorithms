

import sys

def longest_consecutive_subsequence(arr):
    dct = dict()
    _low,_high = sys.maxsize,-sys.maxsize
    for ele in arr:
        dct[ele] = -1
        _low = min(ele, _low)
        _high = max(ele,_high)

    _max,_small = 0,0
    for k,v in dct.items():
        if v == -1:
            dct[k] = 0
            _length = 1

            cur = k + 1
            while cur in dct and cur <= _high:
                _length += 1
                dct[cur] = 0
                cur += 1

            cur = k - 1
            while cur in dct and cur >= _low:
                _length += 1
                dct[cur] = 0
                cur -= 1

            if _length > _max:
                _max = _length
                _small = cur + 1

    return _max, _small

def main():
    _max,_small = longest_consecutive_subsequence([2, 9, 3, 10, 4, 20, 1])
    print('length:', _max, "start num: ", _small)

if __name__ == "__main__":
    main()

