def selectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array

array = [9,5,0,4,3,1]
print("Following is the selection Sort of given Array:")
print(selectionSort(array))