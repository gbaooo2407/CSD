def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left,right)
def merge_two_sorted_list(a, b):
    merged_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1
    while i < len_a:
        merged_list.append(a[i])
        i += 1
    while j < len_b:
        merged_list.append(b[j])
        j += 1
    return merged_list


if __name__ == '__main__':
    arr = [24,36,12,4,25,63,22,29,10,5]
    print(merge_sort(arr))