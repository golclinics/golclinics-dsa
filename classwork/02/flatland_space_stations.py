def flatlandSpaceStations(n, c):
    c.sort()
    maximum_distance = max(c[0], n-1 - c[-1])
    import pdb
    pdb.set_trace()
    for i in range(len(c)-1):
        maximum_distance = max((c[i+1]-c[i])//2, maximum_distance)
    return maximum_distance