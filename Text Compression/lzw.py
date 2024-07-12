def lzw_compression(text):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    string = ""
    result = []

    for c in text:
        merged = string + c
        if merged in dictionary:
            string = merged
        else:
            result.append(dictionary[string])
            dictionary[merged] = dict_size
            dict_size += 1
            string = c

    if string:
        result.append(dictionary[string])
    return result

def lzw_decompression(compressed):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    compressed = iter(compressed)

    string = chr(next(compressed))
    result = [string]

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = string + string[0]

        result.append(entry)

        dictionary[dict_size] = string + entry[0]
        dict_size += 1
        string = entry
    return ''.join(result)


if __name__ == '__main__':
    text = "TOBENOTTOBEISNOTTOBE"
    compressed = lzw_compression(text)
    print("compressed: ",compressed )
    decompressed = lzw_decompression(compressed)
    print("decompessed: ",decompressed)