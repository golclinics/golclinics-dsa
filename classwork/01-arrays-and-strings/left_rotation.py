def solve(a, d):
    i = d % len(a)
    return(a[i:]+a[:i])