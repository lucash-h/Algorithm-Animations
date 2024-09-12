import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def create_array(lower_limit=0, upper_limit=10, val_num=10):
    array = np.random.randint(lower_limit, upper_limit, val_num)
    return array

#merge sort
#divide
#merge
#mergesort

def divide(array):
    if(len(array) > 2 or len(array) < 1):
        return array
    mid = len(array) // 2

    #check sytanx
    array1 = array[:mid]
    array2 = array[mid:len(array)]

    return array1, array2

#try list comprehensions maybes
def merge(array1, array2):
    merged_array = []
    i = 0

    #while one array is not exhausted
    while(array1 != null or array2 != null):
        if(array1[i] > array2[i]):
            merged_array.append(array2[i])
            
            #remove array2[i] from array2
        elif(array1[i] < array2[i]):
            merged_array.append(array1[i])
            #remove array1[i] from array1
        else:
            if len(array1) > len(array2):
                merged_array.append(array1[i])
            else:
                merged_array.append(array2[i])

    return merged_array

def merge_sort(array):
    if(len(array) < 2):
        return array

    a1, a2 = divide(array)
    merged = merge(a1,a2)

    return merged

def main():
    array = create_array()
    print(array)

    array_sorted = merge_sort(array)
    print(array_sorted)

if __name__ == "__main__": 
    main()

    
