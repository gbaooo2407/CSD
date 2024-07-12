def rle_compression(text):
    if not text:
        return ""

    compressed_string = ""
    current_char = text[0]
    count = 1

    for char in text [1:]:
        if char == current_char:
            count += 1
        else:
            compressed_string += current_char + str(count)
            current_char = char
            count = 1
    compressed_string += current_char + str(count)

    return compressed_string

def rle_decompression(compressed_string):
    if not compressed_string:
        return ""

    decompressed_string = ""
    count = ""

    for char in compressed_string:
        if char.isdigit():
            count += char
        else:
            if count:
                decompressed_string += current_char * int(count)
            current_char = char
            count = ""
    if count:
        decompressed_string += current_char * int(count)
    return decompressed_string

if __name__ == '__main__':
    text = "AAAAABBBBBCCCCCCCDD"
    compressed = rle_compression(text)
    decompressed = rle_decompression(compressed)
    print('compressed: ', compressed)
    print('decompressed: ', decompressed)