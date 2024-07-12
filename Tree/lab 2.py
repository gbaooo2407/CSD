#Find index of all the occurances of a number from sorted list

#numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
#number_to_find = 15
#This should return 5,6,7 as indices containing number 15 in the array

def binary_search(array,target):
    left = 0
    right = len(array) -1
    index = 0
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if array[middle] < target:
            left = middle +1
        else:
            right = middle -1
    return -1

def indices(array,target):
    index = binary_search(array, target)
    position = []
    if index == -1:
        return []
    i = index
    while i >= 0 and array[i] == target:
        position.append(i)
        i -= 1
    i = index + 1
    while i < len(array) and array[i] == target:
        position.append(i)
        i += 1
    position.sort()
    return position

def main():
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    print(indices(numbers, number_to_find))
if __name__ == '__main__':
    main()