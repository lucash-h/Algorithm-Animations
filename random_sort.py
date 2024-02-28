import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#maybe create a main file that contains functions that overlap and another to handle running?

lower_limit = 1
upper_limit = 100
number = 100

'''
This function creates a random array of 10 integers between 1 and 100
'''
def create_array():
    array = np.random.randint(lower_limit, upper_limit, number)
    return array
"""
def random_sort(bars, array, i):
    i = np.random.randint(0, len(array))
    j = np.random.randint(0, len(array))
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

    bars[i].set_color('red')
    bars[j].set_color('red')
"""
def random_sort(array, i, j):
    """i = np.random.randint(0, len(array))
    j = np.random.randint(0, len(array))"""

    if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]


def update(frame, bars, array):
    if validate(array):
        return

    random_number = np.random.randint(0, len(array)-1)

    random_sort(array, random_number, random_number + 1)
    for i in range(len(array)):
        bars[i].set_height(array[i])
        bars[i].set_color('b')

    bars[random_number].set_color('white')
    bars[random_number + 1].set_color('red')

def validate(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def random_animation():
    array = create_array()
    array = create_array()
    fig, ax = plt.subplots()
    bars = plt.bar(range(len(array)), array, color='b')
    
    animation = anim.FuncAnimation(fig, update, fargs=(bars, array), frames=10, repeat=True)
    
    ax.set_facecolor('black')
    plt.grid(color='white', linestyle='-', linewidth=0.5)

    plt.show()  
if __name__ == "__main__":
    random_animation()