def minimumBribes(q):
    
    bribe_count = 0
    n = len(q)
    
    for i in range(n-1, -1, -1):
         # break on encounter of bribes > 2
        if (q[i] - (i+1)) > 2:
            print("Too chaotic")
            return
        
        # check if within a range less than 1-q[n]-1 theres a number greater
        #  than q[n] and increment bribe count if the condition is satisfied 
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribe_count += 1
                
    print(bribe_count)

# driver code
minimumBribes([2,1,5,3,4])