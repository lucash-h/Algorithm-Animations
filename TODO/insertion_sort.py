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
    array[0] = 1
    return array

def insertion_sort(bars, array, k):
    key = array[k]
    j = k - 1
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        bars[j + 1].set_height(array[j])  

        j -= 1
    array[j + 1] = key


    bars[k].set_height(array[k]) 
    bars[j+1].set_height(array[j])
    bars[k].set_color('red')
    #bars[j+1].set_color('red')
    bars[j].set_color('red')

def update(num, array, bars):
    if num < len(array):
        insertion_sort(bars, array, num+1)
    
def insertion_animation():
    array = create_array()
    fig, ax = plt.subplots()

    bars = plt.bar(range(len(array)), array, color='b')
    ani = anim.FuncAnimation(fig, update, fargs=(array, bars), frames=len(array), repeat=False, interval = 100)
    
    ax.set_facecolor('black')
    plt.grid(color='white', linestyle='-', linewidth=0.5)   
    
    plt.show()  


if __name__ == "__main__":
    insertion_animation()