
# fraction addition
# given two fractions (numerator and denominator), count the sum of them
# the result should be the simplest result. (use common smallest multiple and common biggest divisor)

def primes(num):
    lst = [x for x in range(2,num) if all(x%y!=0 for y in range(2,x))]
    return lst

def factors(num,primeArr):
    dct = dict()
    n = num
    while n > 1:
        for idx in range(len(primeArr)):
            pri = primeArr[idx]
            if n%pri == 0:
                n = int(n/pri)
                if pri in dct:
                    dct[pri] += 1
                else:
                    dct[pri] = 1
                break
    return dct

def common_smallest_mul(dct1,dct2):
    ans = 1
    for k1,v1 in dct1.items():
        if k1 not in dct2:
            ans *= (k1**v1)
        else:
            _max = max(v1,dct2[k1])
            ans *= (k1**_max)
    
    for k2,v2 in dct2.items():
        if k2 not in dct1:
            ans *= (k2**v2)
    return ans

def common_biggest_div(dct1,dct2):
    ans = 1
    for k1,v1 in dct1.items():
        if k1 in dct2:
            _min = min(v1, dct2[k1])
            ans *= (k1**_min)
    return ans

def fraction_addition(frac1,frac2):
    n1,d1 = frac1
    n2,d2 = frac2

    pri = primes(max(d1,d2))
    fac_d1 = factors(d1,pri)
    fac_d2 = factors(d2,pri)
    d3 = common_smallest_mul(fac_d1,fac_d2)
    
    n3 = n1*int(d3/d1) +  n2*int(d3/d2)
    pri = primes(max(n3,d3))
    fac_n3 = factors(n3,pri)
    fac_d3 = factors(d3,pri)
    div = common_biggest_div(fac_n3,fac_d3)
    
    d3 = int(d3/div)
    n3 = int(n3/div)

    return (n3,d3)


def main():
    ans = fraction_addition((7,12),(4,8))
    print(ans)

if __name__ == "__main__":
    main()

