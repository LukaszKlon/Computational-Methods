import numpy as np

def normal_sum(table):
    sum = np.float32(0)
    for i in table:
        sum += i

    return sum

def recu_sum(table,l,r):
    if l == r:
        return np.float32(table[l])
    mid = (l + r)//2 
    return recu_sum(table,l,mid) + recu_sum(table,mid+1,r)

def kahan_sum(table):
    sum = np.float32(0)
    err = np.float32(0)
    y = np.float32(0)
    temp = np.float32(0)
    for i in table:
        y = i+err
        temp = sum+y
        if temp == np.nan:
            print(temp)
            break
        err = (temp-sum)+y
        sum = temp
    
    return sum

x = np.float32(0.53125)
N = 10**7
table = [x for _ in range(N)]
print(normal_sum(table))
print(recu_sum(table,0,N-1))
print(kahan_sum(table))