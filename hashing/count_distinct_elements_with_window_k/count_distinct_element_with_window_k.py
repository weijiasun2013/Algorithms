

def count_distinct_element_with_window_k(arr,k):
    # Count distinct elements in every window of size k
    d = dict()
    rslt = []
    for idx in range(len(arr)-k+1):
        if idx == 0:
            for i in range(idx,idx+k):
                if arr[i] not in d:
                    d[arr[i]] = 1
                else:
                    d[arr[i]] += 1

        else:
            _remove, _add = arr[idx-1], arr[idx+k-1]
            if _remove != _add:
                if d[_remove] == 1:
                    del d[_remove]
                else:
                    d[_remove] -= 1
                if _add not in d:
                    d[_add] = 1
                else:
                    d[_add] += 1
        rslt.append(len(d))
    return rslt

def main():
    rslt = count_distinct_element_with_window_k([1,1,2,2,2,3,4,5],4)
    print(rslt)

if __name__ == '__main__':
    main()