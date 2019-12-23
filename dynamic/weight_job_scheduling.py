
# weight job scheduling
# give a set of job time windows including beginning and ending time, and their weight
# find out how to pick up jobs to make maximum profit

def weight_job_scheduling(job,weight):
    e_s_p = []
    for idx in range(len(job)):
        e_s_p.append((job[idx][1], job[idx][0], weight[idx]))
    e_s_p.sort()
    
    _max = 0
    dp = [e_s_p[x][2] for x in range(len(e_s_p))]
    for idx in range(1,len(e_s_p)):
        curE,curS,curP = e_s_p[idx]
        for pIdx in range(idx):
            preE,preS,preP = e_s_p[pIdx]
            if preE <= curS and dp[pIdx] + curP > dp[idx]:
                dp[idx] = dp[pIdx] + curP
                if _max < dp[idx]:
                    _max = dp[idx]
    return _max


def main():
    job = [(2,3), (2,4), (3,5), (5,7)]
    weight = [1,2,2,1]
    rslt = weight_job_scheduling(job,weight)
    print(rslt)
    
if __name__ == "__main__":
    main()


