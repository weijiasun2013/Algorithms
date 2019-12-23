
# generate parentheses
# give a number, produce all reasonable parentheses pairs

def helper(left,right,path,rslt):
    if right == 0:
        rslt.append(path)
        return
    if left > 0:
        helper(left-1,right,path+'(',rslt)
    if right > left:
        helper(left,right-1,path+')',rslt)

def generate_parentheses(num):
    rslt = []
    helper(num,num,'',rslt)
    return rslt

def main():
    num = 3
    rslt = generate_parentheses(num)
    for idx in range(len(rslt)):
        print(rslt[idx])

if __name__ == "__main__":
    main()

