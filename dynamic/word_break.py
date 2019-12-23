
# word break
# give a sentance and a dictionary, find out if the sentance can be split into several words which can all be found from dictionary

def word_break(sen,dct):
    dp = [ [False for x in range(len(sen))] for y in range(len(sen))]
    for length in range(1,len(sen)+1):
        for sIdx in range(0,len(sen)-length+1):
            eIdx = sIdx + length - 1
            tmp = sen[sIdx:eIdx+1]
            if tmp in dct:
                dp[sIdx][eIdx] = True
            else:
                for tail in range(sIdx,eIdx):
                    if dp[sIdx][tail] and dp[tail+1][eIdx]:
                        dp[sIdx][eIdx] = True
                        break
    return dp[0][-1]

def main():
    sen = 'iamverygood'
    dct = {'i':1, 'am':1, 'very': 1, 'good': 1}
    rslt = word_break(sen,dct)
    print(rslt)

if __name__ == "__main__":
    main()

