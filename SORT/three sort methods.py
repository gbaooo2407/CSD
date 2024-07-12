def selection_sort(array):
    size = len(array)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array [min_index] = array[min_index],array[i]

def insertion_sort(array):
    size = len(array)
    for i in range(1,size):
        number = array[i]
        j = i - 1
        while j >= 0 and number < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = number

def bubble_sort(array):
    size = len(array)
    for i in range(size - 1):
        is_swapped = False
        for j in range(size-1-i):
            if array[j] > array [j+1]:
                array[j], array[j+1] = array [j+1], array[j]
                is_swapped = True
                print(array)

        if not is_swapped:
            break



if __name__ == '__main__':
    array = [5,4,2,7,12,23,43,23,4,16,20]
    # selection_sort(array)
    insertion_sort(array)
    # array.sort()
    bubble_sort(array)
    print("sorted array",array)