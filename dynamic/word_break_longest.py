
# word break longest problem
# give a snetance and a dictionary, find out the longest sub-sentance which can be split into several words that can all be found from the dictionary

def word_break_longest(sen,dct):
    dp = [ [False for x in range(len(sen))] for y in range(len(sen))]
    _max, _sIdx = 0, -1

    for length in range(1,len(sen)+1):
        for sIdx in range(0,len(sen)-length+1):
            eIdx = sIdx + length - 1
            tmp = sen[sIdx:eIdx+1]
            if tmp in dct:
                dp[sIdx][eIdx] = True
                if _max < len(tmp):
                    _max = len(tmp)
                    _sIdx = sIdx
            else:
                for tail in range(sIdx,eIdx):
                    if dp[sIdx][tail] and dp[tail+1][eIdx]:
                        dp[sIdx][eIdx] = True
                        if _max < len(tmp):
                            _max = len(tmp)
                            _sIdx = sIdx
                        break
    return _max, _sIdx

def main():
    sen = 'abciamverywellbb'
    dct = {'i':1, 'am':1, 'very':1, 'good':1}
    _max,_sIdx = word_break_longest(sen,dct)
    print(sen)
    print(_max,_sIdx)

if __name__ == "__main__":
    main()

