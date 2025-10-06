import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

def create_array():
    array = np.random.randint(1, 100, 50)
    return array

current_pass = 0
current_comparison = 0
is_sorting = True

def bubble_sort_step(array, bars):
    global current_pass, current_comparison, is_sorting
    
    n = len(array)
    
    for bar in bars:
        bar.set_color('blue')
    
    if current_pass >= n - 1:
        is_sorting = False
        for bar in bars:
            bar.set_color('green')
        return bars
    
    if current_comparison < n - 1 - current_pass:
        j = current_comparison
        
        bars[j].set_color('red')
        bars[j + 1].set_color('red')
        
        #Compare/Swap
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

            bars[j].set_height(array[j])
            bars[j + 1].set_height(array[j + 1])

            bars[j].set_color('yellow')
            bars[j + 1].set_color('yellow')
        
        current_comparison += 1
    else:
        bars[n - 1 - current_pass].set_color('green')
        current_pass += 1
        current_comparison = 0
    
    return bars

def update(frame, bars, array):
    global is_sorting
    
    if is_sorting:
        return bubble_sort_step(array, bars)
    else:
        return bars

def bubble_animation():
    global current_pass, current_comparison, is_sorting
    
    current_pass = 0
    current_comparison = 0
    is_sorting = True
    
    array = create_array()
    fig, ax = plt.subplots(figsize=(12, 6))

    bars = plt.bar(range(len(array)), array, color='blue')
    
    n = len(array)
    max_frames = n * n
    
    ani = anim.FuncAnimation(fig, update, fargs=(bars, array), 
                           frames=max_frames, interval=100, repeat=False, blit=False)

    ax.set_facecolor('black')
    ax.set_title('Bubble Sort Animation', color='white', fontsize=16)
    ax.set_xlabel('Array Index', color='white')
    ax.set_ylabel('Value', color='white')
    ax.tick_params(colors='white')
    plt.grid(color='gray', linestyle='-', linewidth=0.3, alpha=0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    bubble_animation()
