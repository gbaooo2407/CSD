def brute_force_matching(text,pattern):
    n = len(text)
    m = len(pattern)
    pos = []
    j = 0
    for i in range(n-m+1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
            if j == m:
                pos.append(i)
                i += 1
    return pos

if __name__ == '__main__':
    text = 'this is a long text with pattern inside pattern'
    pattern = ['pattern','text']

    result = brute_force_matching(text,pattern)

    if result != -1:
        print("Pattern found at index: {}".format(result))
    else:
        print("Pattern not found in text")