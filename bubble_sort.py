import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

def create_array():
    array = np.random.randint(1, 100, 1000)
    return array

def bubble_sort(bars, array, i):
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
    
    bars[i].set_height(array[i]) 
    bars[j].set_height(array[j])
    bars[j+1].set_height(array[j+1]) 
    bars[j+1].set_color('white')

    return bars

def update(i, bars, array):
    if i < len(array):
        bars = bubble_sort(bars, array, i)
    return bars

def bubble_animation():
    array = create_array()
    fig, ax = plt.subplots()

    bars = plt.bar(range(len(array)), array, color='b')
    ani = anim.FuncAnimation(fig, update, fargs=(bars, array), frames=1000, repeat=False)

    ax.set_facecolor('black')
    plt.grid(color='white', linestyle='-', linewidth=0.5)

    plt.show()

bubble_animation()
