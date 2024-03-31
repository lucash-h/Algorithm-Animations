import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

'''
This function creates a random array of 10 integers between 1 and 100
'''
def create_array(min_val, max_val, size):
    array = np.random.randint(min_val, max_val, size=size)
    return array

def insertion_sort(array, bars):

    for i in range(1, len(array)):
        val = array[i]

        #set the color of the bar being sorted to red
        bars[i].set_color('red')

        j = i - 1
        while j >= 0 and array[j] > val:
            #set the color of bar currently being evaluated to blue
            bars[j].set_color('blue')
            array[j + 1] = array[j]
            bars[j + 1].set_height(array[j])

            j -= 1
        #value has been found at j+1
        array[j + 1] = val

        bars[j + 1].set_color('purple')
        bars[j + 1].set_height(val)
        yield


'''
def track_traverse(array, bars, cur_idx):
    for i in range(len(array)):
        if i == cur_idx:
            bars[i].set_color('red')
        else:
            bars[i].set_color('blue')
    return bars
'''


def animation(array):
    fig, ax = plt.subplots()
    bars = plt.bar(range(len(array)), array, color='b')
    ani = anim.FuncAnimation(fig, func=insertion_sort, fargs=(array, bars), frames=len(array) - 1, repeat=True)
    plt.show()  

def main():
    min = 0
    max = 100
    size = 100
    rand_array = create_array(min, max, size)
    animation(rand_array)

    print(f"OG array: {rand_array}")

if __name__ == "__main__":
    main()