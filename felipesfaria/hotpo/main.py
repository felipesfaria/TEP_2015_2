__author__ = 'felipesfaria'
import time
print ("Hello Half or Three Plus One!")
memo = {}
memoCounter = [0]

def hotpo(n):
    if(n%2==0):
        return n/2
    return 3*n+1

def hotpoCountMemo(n):
    if(n in memo and n<memoCap):
        return memo[n]
    if n==1:
        result = 1;
    else:
        result = hotpoCountMemo(hotpo(n))+1
    if(n<memoCap):
        memoCounter[0] = memoCounter[0]+ 1
        memo[n]=result
    return result

def hotpoCount(n):
    if n==1:
        result = 1;
    else:
        result = hotpoCount(hotpo(n))+1;
    return result

def hotpoMaxMemo(min,max):
    maxCount = 0;
    maxN=0
    memo={}
    for i in range(min,max+1):
        t=hotpoCountMemo(i)
        if(t>maxCount):
            maxCount=t
            maxN=i
    return [maxN,maxCount]

def hotpoMax(min,max):
    maxCount = 0;
    maxN=0
    for i in range(min,max+1):
        t=hotpoCount(i)
        if(t>maxCount):
            maxCount=t
            maxN=i
    return [maxN,maxCount]

def printHotpoMax(min,max,memo):
    start = time.time()
    if(memo):
        r=hotpoMaxMemo(min,max)
    else:
        r=hotpoMax(min,max)
    end=time.time()
    elapsed = end-start
    print("MemoCap={:,}\tMemoCounter={:,}".format(memoCap,memoCounter[0]))
    print("hotpoMax({:,},{:,})=n:{:,},max:{:,}\telapsed={}\tmemo={}".format(min,max,r[0],r[1],end-start,memo))

memoCap = 12000000
printHotpoMax(1000000,10000000,True)