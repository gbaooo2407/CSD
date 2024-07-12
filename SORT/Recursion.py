def walk (steps):
    for step in range(1,steps +1):
        print(step)

def recursion_walk(steps):
    if steps == 0:
        return
    recursion_walk(steps-1)
    print(steps)

def factorial(number):
    result = 1
    for i in range(1,number+1):
        result = result * i
    return result

def recursion_factorial(number):
    if number == 0:
        return 1
    return number * recursion_factorial(number-1)

def linear_search(array,target):
    for index,element in enumerate(array):
        if element == target:
            return index
    return -1

def binary_search(array,target):
    left = 0
    right = len(array) -1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if array[middle] < target:
            left = middle +1
        else:
            right = middle -1
    return -1

def recursive_binary_search(array,target,left,right):
    middle = (left+right) // 2
    if right < left:
        return -1
    if array[middle] == target:
        return middle
    if array[middle] < target:
        left = middle + 1
    else:
        right = middle - 1
    return recursive_binary_search(array,target,left,right)

def recursive_linear_search(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_linear_search(arr, target, index + 1)


if __name__ == '__main__':
    array =[1,2,4,5,7,8,9]
    print(recursive_binary_search(array,7,0,len(array)-1))
    print(recursive_linear_search(array,8))