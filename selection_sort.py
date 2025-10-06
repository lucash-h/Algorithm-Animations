import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

def create_array():
    """Creates a random array for sorting visualization"""
    array = np.random.randint(1, 100, 30)  # Reduced size for better visualization
    return array

# Global variables for animation state
current_pass = 0
current_comparison = 0
min_index = 0
is_sorting = True
total_comparisons = 0

def selection_sort_step(array, bars):
    """Performs one step of selection sort for animation"""
    global current_pass, current_comparison, min_index, is_sorting, total_comparisons
    
    n = len(array)
    
    # Reset all colors
    for i, bar in enumerate(bars):
        if i < current_pass:
            bar.set_color('green')  # Sorted portion
        elif i == current_pass:
            bar.set_color('blue')   # Current position to fill
        else:
            bar.set_color('lightblue')  # Unsorted portion
    
    # Check if sorting is complete
    if current_pass >= n - 1:
        is_sorting = False
        # Color all bars green when sorting is complete
        for bar in bars:
            bar.set_color('green')
        return bars
    
    # Initialize min_index for new pass
    if current_comparison == 0:
        min_index = current_pass
        bars[min_index].set_color('orange')  # Current minimum candidate
    
    # Perform one comparison per frame
    if current_comparison < n - current_pass - 1:
        compare_index = current_pass + current_comparison + 1
        
        # Highlight the element being compared
        bars[compare_index].set_color('red')
        bars[min_index].set_color('orange')  # Keep minimum highlighted
        
        # Compare and update minimum if needed
        if array[compare_index] < array[min_index]:
            # Previous minimum goes back to normal color
            if min_index != current_pass:
                bars[min_index].set_color('lightblue')
            
            min_index = compare_index
            bars[min_index].set_color('orange')  # New minimum
        
        current_comparison += 1
        total_comparisons += 1
        
    else:
        # End of current pass - perform the swap
        if min_index != current_pass:
            # Swap elements
            array[current_pass], array[min_index] = array[min_index], array[current_pass]
            
            # Update bar heights
            bars[current_pass].set_height(array[current_pass])
            bars[min_index].set_height(array[min_index])
            
            # Highlight the swap
            bars[current_pass].set_color('yellow')
            bars[min_index].set_color('yellow')
        else:
            # No swap needed, just highlight the position
            bars[current_pass].set_color('yellow')
        
        # Move to next pass
        current_pass += 1
        current_comparison = 0
    
    return bars

def update_animation(frame, bars, array):
    """Update function for the animation"""
    global is_sorting, current_pass, total_comparisons
    
    if is_sorting:
        selection_sort_step(array, bars)
    
    return bars

def selection_animation():
    """Main function to run the selection sort animation"""
    global current_pass, current_comparison, min_index, is_sorting, total_comparisons
    
    # Reset global variables
    current_pass = 0
    current_comparison = 0
    min_index = 0
    is_sorting = True
    total_comparisons = 0
    
    array = create_array()
    print(f"Original array: {array.tolist()}")
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 8))
    bars = plt.bar(range(len(array)), array, color='lightblue')
    
    # Customize the plot
    ax.set_facecolor('black')
    ax.set_title('Selection Sort Animation', color='white', fontsize=16, pad=20)
    ax.set_xlabel('Array Index', color='white')
    ax.set_ylabel('Value', color='white')
    ax.tick_params(colors='white')
    
    # Add legend
    legend_elements = [
        plt.Rectangle((0,0),1,1, color='green', label='Sorted'),
        plt.Rectangle((0,0),1,1, color='blue', label='Current Position'),
        plt.Rectangle((0,0),1,1, color='orange', label='Current Minimum'),
        plt.Rectangle((0,0),1,1, color='red', label='Comparing'),
        plt.Rectangle((0,0),1,1, color='yellow', label='Swapping'),
        plt.Rectangle((0,0),1,1, color='lightblue', label='Unsorted')
    ]
    ax.legend(handles=legend_elements, loc='upper left', 
             facecolor='white', edgecolor='black')
    
    plt.grid(color='gray', linestyle='-', linewidth=0.3, alpha=0.5)
    
    # Calculate number of frames needed
    n = len(array)
    max_frames = n * (n + 1) // 2 + 50  # Enough frames for all comparisons plus buffer
    
    # Create animation
    ani = anim.FuncAnimation(fig, update_animation, 
                           fargs=(bars, array),
                           frames=max_frames,
                           interval=200,  # 200ms between frames
                           repeat=False, 
                           blit=False)
    
    plt.tight_layout()
    plt.show()
    
    print(f"Final sorted array: {array.tolist()}")
    print(f"Total comparisons made: {total_comparisons}")

if __name__ == "__main__":
    selection_animation()
