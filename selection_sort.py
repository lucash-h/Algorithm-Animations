import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#maybe create a main file that contains functions that overlap and another to handle running?


'''
This function creates a random array of 10 integers between 1 and 100
'''
def create_array():
    array = np.random.randint(1, 100, 100)
    return array

def selection_sort(bars, array, k):
    a_len = len(array)
    min = k
    for j in range(k+1,a_len):
        if array[j] < array[min]:
            min = j
    array[k], array[min] = array[min], array[k]

    for bar in bars:
        bar.set_color('white')

    bars[k].set_height(array[k]) 
    bars[min].set_height(array[min])
    bars[min].set_color('red')


def update(num, array, bars):
    if num < len(array):
        selection_sort(bars, array, num)



def selection_animation():
    array = create_array()
    fig, ax = plt.subplots()

    bars = plt.bar(range(len(array)), array, color='b')
    ani = anim.FuncAnimation(fig, update, fargs=(array, bars), frames=5000, repeat=False)
    
    ax.set_facecolor('black')
    plt.grid(color='white', linestyle='-', linewidth=0.5)   
    
    plt.show()  


if __name__ == "__main__":
    selection_animation()
