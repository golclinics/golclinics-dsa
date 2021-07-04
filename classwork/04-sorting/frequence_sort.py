def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """

    freq = {}
    res = ""

    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    sorted_freq = list(
        sorted(freq.items(), key=lambda x: x[1], reverse=True))

    for i, c in sorted_freq:
        res += i * c

    return res

print(frequencySort("tree"))