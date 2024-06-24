def flatlandSpaceStations(n, c):
    c.sort()
    maxDistance = c[0]
    
    for i in range(len(c)):
        dist = (c[i] - c[i-1])/2
        if(maxDistance < dist):
            maxDistance = dist
            
    lastStation = (n-1) - c[len(c)-1]
    
    if(lastStation < maxDistance):
        return int(maxDistance)
    else:
        return int(lastStation)