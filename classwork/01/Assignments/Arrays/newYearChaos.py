def minimumBribes(q):
    q_count = 0
    for i in range(len(q)-1,-1,-1):
        if(q[i] - (i+1) > 2) :
            print("Too chaotic")
            return
        
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                q_count += 1
                
    print(q_count)
    return

