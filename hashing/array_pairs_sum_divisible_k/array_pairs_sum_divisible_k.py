

def array_pairs_sum_divisible_k(arr,k):
    # Check if an array can be divided into pairs whose sum is divisible by k

    if len(arr)%2 == 1:
        return False,None

    d = dict()
    rslt = []
    for ele in arr:
        r = ele%k
        other = (k - r)%k
        if other not in d:
            if r not in d:
                d[r] = [ele]
            else:
                d[r].append(ele)
        else:
            rslt.append((d[other][-1],ele))
            if len(d[other]) == 1:
                del d[other]
            else:
                del d[other][-1]

    if len(d) == 0:
        return True,rslt
    return False,None

def main():
    ans1,solution1 = array_pairs_sum_divisible_k([9,7,5,3],6)
    print(ans1,solution1)

    ans2, solution2 = array_pairs_sum_divisible_k([9, 17, 5, 3], 6)
    print(ans2, solution2)

if __name__ == '__main__':
    main()