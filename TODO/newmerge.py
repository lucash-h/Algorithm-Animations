import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import math

def create_array():
    array = np.random.randint(1, 100, 100)
    array[0] = 1
    return array

#for merge sort
#divide the array into 2
#sort each half by dividing until there are only two elements?
def merge_sort(a, bars, stat, middle, end):
    if (len(a) < 2):
        return a

    half = len(a) // 2
    return merge(merge_sort(a[:half]), bars, 0, half, len(a))

def merge(a, bars, start, middle, end):
    merged = []
    l = 0
    r = 0

    #iterates through each array and appends the smaller value to the merged array
    while l < middle and r < end:
        if a[l] < a[r]:
            merged.append(a[l])
            l += 1
        else:
            merged.append(a[r])
            r += 1
    #the loop runs out when either a or b has been iterated through
    #so we append the rest of the other array to the merged array
    while l < middle:
        merged.append(a[l])
        l += 1
    while r < end:
        merged.append(a[r])
        r += 1

    for i in range(len(merged)):
        a[start + i] = merged[i]
        bars[start + i].set_height(merged[i])

    return merged

def update(frame, array, bars):
        start = 0
        width = len(array)
        middle = min(start + width, len(array))
        end = min(start + 2 * width, len(array))
        merge_sort(array, bars, start, middle, end)
    #frame set to log2(len(array))) + 1 which is # of steps in merge sort operation to properly show animation

def merge_sort_animation(a):
    array = create_array()
 
    fig, ax = plt.subplots()

    bars = plt.bar(range(len(array)), array, color='b')
    
    ani = anim.FuncAnimation(fig, update, fargs=(array,bars), frames=int(np.log2(len(array))) + 1, repeat=True, interval = 100)
    
    ax.set_facecolor('black')
    plt.grid(color='white', linestyle='-', linewidth=0.5)   
    
    plt.show()  

    

def main():
    array = create_array()
    merge_sort_animation(array)

if __name__ == "__main__": main()