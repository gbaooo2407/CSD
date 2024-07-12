def swap(a, b, array):
    array[a], array[b] = array[b], array[a]

def partition(array, start, end):
    pivot = array[start]  # Chọn pivot là phần tử đầu tiên của mảng con
    left = start + 1
    right = end

    while True:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            swap(left, right, array)

    swap(start, right, array)
    return right


def quick_sort(array, start, end):
    if start < end:
        partition_index = partition(array, start, end)
        quick_sort(array, start, partition_index - 1)
        quick_sort(array, partition_index + 1, end)


if __name__ == '__main__':
    array = [10, 8, 12,35, 27, 2, 6, 40]
    quick_sort(array, 0, len(array) - 1)
    print(array)
