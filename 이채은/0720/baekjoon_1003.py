t = int(input())
 
for _ in range(t):
    pe_0 = [1,0]
    pe_1 = [0,1]
    N = int(input())
    if N > 1:
        for i in range(N-1):
            pe_0.append(pe_1[-1])
            pe_1.append(pe_0[-2]+pe_1[-1]) 
 
    print(pe_0[N], pe_1[N])
