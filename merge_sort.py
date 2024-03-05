import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import math

def create_array():
    array = np.random.randint(1, 100, 100)
    array[0] = 1
    return array
'''
def merge_sort(S):
    S1 = []
    S2 = []
    if (len(S) < 2): 
        return S
    divide(S1,S2,S)
    S1 = merge_sort(S1)
    S2 = merge_sort(S2)
    merge(S1,S2,S)
    return S

def divide(S1,S2,S):
    for i in range (math.ceil(len(S)/2)):
        S1[i] = S[i]
    i = math.ceil(len(S)/2 + 1) 
    for i in range(len(S)):
        S2[i - math.math.ceil(len(S)/2)] = S[i]

def merge(S1,S2,S):
    i = 1
    j = 1
    while (i < len(S1) and j < len(S2)):
        if (S1[i] < S2[j]):
            S[i+j-1] = S1[i]
            i += 1
        else:
            S[i+j-1] = S2[j]
            j += 1

    while (i < len(S1)):
        s[i+j-1] = S1[i]
        i += 1

    while (j < len(S2)):
        S[i+j-1] = S2[j]
        j += 1
'''

'''
Merge Sort
Takes a list
divides the list into 2
sorts both lists
combines the lists

so to animate I need to get first list
show that it is split
    give each half a different color
then neeed to show both sides getting sorted recursively
    can just change bar colors and heights
    recursively sorts by breaking down until the list length < 2 then merge them together
    sooo each frame can have one of those iterations of breaking down the list or merging
    so I could show each section breaking into halfs
    then one by one each "half" gets merged back together once the length < 2
    
'''
#divide
def divide(S):
    if (len(S) < 2): 
        return S
    S1 = S[:len(S)//2]
    S2 = S[len(S)//2:]
    return S1, S2

def conquer_helper(val,S, index):
    if(val < S[index]):        
        S.insert(index,val)
    else:
        conquer_helper(val,S,index+1)

#conquer
def conquer(S):
    #sort list
    if(len(S) < 2):
        return S
    for i in range(len(S)):
        conquer_helper(S[i],S,0)

#combine
def combine(S1,S2, bars):
    S = []
    i = 0
    j = 0
    while (i < len(S1) and j < len(S2)):
        if (S1[i] < S2[j]):
            S.append(S1[i])
            bars[i].set_height(S1[i])
            i += 1
        else:
            S.append(S2[j])
            bars[j].set_height(S1[j])

            j += 1
    while (i < len(S1)):
        S.append(S1[i])
        bars[i].set_height(S1[i])
        i += 1
    while (j < len(S2)):
        S.append(S2[j])
        bars[i].set_height(S1[i])
        j += 1
    return S

def update(frame, array, bars):
    #divide
    #conquer
    #combine
    
    
def mergesort_animation():
    array = create_array()
    fig, ax = plt.subplots()

    bars = plt.bar(range(len(array)), array, color='b')
    ani = anim.FuncAnimation(fig, update, fargs=(array, bars), frames=len(array), repeat=False, interval = 100)
    
    ax.set_facecolor('black')
    plt.grid(color='white', linestyle='-', linewidth=0.5)   
    
    plt.show()  


if __name__ == "__main__":
    mergesort_animation()