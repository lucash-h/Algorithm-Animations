import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import time

def create_array():
    array = np.random.randint(1, 100, 32)  
    return array.tolist()

animation_steps = []
current_step = 0

class MergeSortAnimator:
    def __init__(self, array):
        self.original_array = array[:]
        self.array = array[:]
        self.steps = []
        self.colors = ['blue'] * len(array)
        
    def merge_sort_with_steps(self, arr, left, right, depth=0):
        """Merge sort that records steps for animation"""
        if left < right:
            mid = (left + right) // 2
            
            self.steps.append({
                'type': 'divide',
                'left': left,
                'right': right,
                'mid': mid,
                'array': arr[:],
                'depth': depth,
                'message': f"Dividing array[{left}:{right+1}] at index {mid}"
            })
            
            self.merge_sort_with_steps(arr, left, mid, depth + 1)
            self.merge_sort_with_steps(arr, mid + 1, right, depth + 1)
            
            self.merge_with_steps(arr, left, mid, right, depth)
    
    def merge_with_steps(self, arr, left, mid, right, depth):
        """Merge function that records steps for animation"""
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        self.steps.append({
            'type': 'merge_start',
            'left': left,
            'right': right,
            'mid': mid,
            'array': arr[:],
            'left_arr': left_arr[:],
            'right_arr': right_arr[:],
            'depth': depth,
            'message': f"Merging subarrays: {left_arr} and {right_arr}"
        })
        
        i = j = 0 
        k = left  
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                self.steps.append({
                    'type': 'merge_compare',
                    'array': arr[:],
                    'comparing': [left + i, mid + 1 + j],
                    'chosen': left + i,
                    'position': k,
                    'value': left_arr[i],
                    'message': f"Comparing {left_arr[i]} <= {right_arr[j]}, choosing {left_arr[i]}"
                })
                i += 1
            else:
                arr[k] = right_arr[j]
                self.steps.append({
                    'type': 'merge_compare',
                    'array': arr[:],
                    'comparing': [left + i, mid + 1 + j],
                    'chosen': mid + 1 + j,
                    'position': k,
                    'value': right_arr[j],
                    'message': f"Comparing {left_arr[i]} > {right_arr[j]}, choosing {right_arr[j]}"
                })
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            self.steps.append({
                'type': 'merge_remaining',
                'array': arr[:],
                'position': k,
                'value': left_arr[i],
                'message': f"Adding remaining element {left_arr[i]}"
            })
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            self.steps.append({
                'type': 'merge_remaining',
                'array': arr[:],
                'position': k,
                'value': right_arr[j],
                'message': f"Adding remaining element {right_arr[j]}"
            })
            j += 1
            k += 1
        
        self.steps.append({
            'type': 'merge_complete',
            'left': left,
            'right': right,
            'array': arr[:],
            'message': f"Completed merging array[{left}:{right+1}]"
        })

def update_animation(frame, bars, text_display):
    global animation_steps, current_step
    
    if current_step >= len(animation_steps):
        return bars
    
    step = animation_steps[current_step]
    
    for bar in bars:
        bar.set_color('lightblue')
    
    for i, bar in enumerate(bars):
        bar.set_height(step['array'][i])
    
    if step['type'] == 'divide':
        for i in range(step['left'], step['right'] + 1):
            bars[i].set_color('orange')
        if 'mid' in step:
            bars[step['mid']].set_color('red')
            bars[step['mid'] + 1].set_color('red')
            
    elif step['type'] == 'merge_start':
        for i in range(step['left'], step['mid'] + 1):
            bars[i].set_color('yellow')
        for i in range(step['mid'] + 1, step['right'] + 1):
            bars[i].set_color('cyan')
            
    elif step['type'] == 'merge_compare':
     
        for i in step['comparing']:
            if i < len(bars):
                bars[i].set_color('red')
  
        bars[step['position']].set_color('green')
        
    elif step['type'] == 'merge_complete':

        for i in range(step['left'], step['right'] + 1):
            bars[i].set_color('lightgreen')
    

    text_display.set_text(step.get('message', ''))
    
    current_step += 1
    return bars

def merge_sort_animation():
    global animation_steps, current_step
    

    current_step = 0
    animation_steps = []
    

    array = create_array()
    animator = MergeSortAnimator(array)
    
    print(f"Original array: {array}")

    animator.merge_sort_with_steps(animator.array, 0, len(animator.array) - 1)
    animation_steps = animator.steps
    
    print(f"Sorted array: {animator.array}")
    print(f"Total animation steps: {len(animation_steps)}")
    

    fig, ax = plt.subplots(figsize=(14, 8))
    bars = plt.bar(range(len(array)), array, color='lightblue')

    text_display = ax.text(0.02, 0.98, '', transform=ax.transAxes, 
                          fontsize=10, verticalalignment='top',
                          bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    

    ax.set_facecolor('black')
    ax.set_title('Merge Sort Animation', color='white', fontsize=16, pad=20)
    ax.set_xlabel('Array Index', color='white')
    ax.set_ylabel('Value', color='white')
    ax.tick_params(colors='white')
    

    legend_elements = [
        plt.Rectangle((0,0),1,1, color='lightblue', label='unsorted'),
        plt.Rectangle((0,0),1,1, color='orange', label='being divided'),
        plt.Rectangle((0,0),1,1, color='yellow', label='left subarray'),
        plt.Rectangle((0,0),1,1, color='cyan', label='right subarray'),
        plt.Rectangle((0,0),1,1, color='red', label='comparing'),
        plt.Rectangle((0,0),1,1, color='green', label='chosen element'),
        plt.Rectangle((0,0),1,1, color='lightgreen', label='merged section')
    ]
    ax.legend(handles=legend_elements, loc='upper right', 
             facecolor='white', edgecolor='black')
    
    plt.grid(color='gray', linestyle='-', linewidth=0.3, alpha=0.5)
    

    ani = anim.FuncAnimation(fig, update_animation, 
                           fargs=(bars, text_display),
                           frames=len(animation_steps) + 10,
                           interval=800,  
                           repeat=False, 
                           blit=False)
    
    plt.tight_layout()
    plt.show()

def main():
    merge_sort_animation()

if __name__ == "__main__": 
    main()