import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

import quickSort
import mergeSort
import selectionSort
import insertionSort
import countingSort
import bubbleSort

sortingAlgorithms = {
    "Quick Sort": quickSort.quickSort,
    "Merge Sort": mergeSort.mergeSort,
    "Selection Sort": selectionSort.selectionSort,
    "Insertion Sort": insertionSort.insertionSort,
    "Counting Sort": countingSort.countingSort,
    "Bubble Sort": bubbleSort.bubbleSort,
}

# Plot The Array As A Bar Chart
def plotArray(arr_chart, arr, bar_colors=None):
    if bar_colors is None:
        bar_colors = ['#162780'] * len(arr) # Default Color

    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color=bar_colors)

    # Display The Plot In The Streamlit App
    arr_chart.pyplot(fig)
    plt.close(fig)

# Main Function To Run The Streamlit App
def main():
    minLen = 2
    maxLen = 50
    defaultLen = 30
    maxValue = 100

    st.title('Sorting Algorithm Visualization')
    algorithm = st.selectbox('Choose Sorting Algorithm', list(sortingAlgorithms.keys()))
    arraySize = st.slider('Array Size', min_value=minLen, max_value=maxLen, value=defaultLen, step=1)
    delay = st.number_input('Animation Delay', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    array = np.random.randint(1, maxValue + 1, arraySize)
    arr_chart = st.empty()

    plotArray(arr_chart, array)

    if st.button('Sort'):
        sorted_array = array.copy()
        steps = sortingAlgorithms[algorithm](sorted_array)
        for step in steps:
            bar_colors = ['#162780'] * len(step['array']) # Default Bar Color
            # Define Color Of Specified Type Of  Bars
            if step.get('boundaries'): # Orange
                for index in step['boundaries']:
                    if 0 <= index < len(step['array']):
                        bar_colors[index] = '#FFA500'
            if step.get('highlight'): # Red
                for index in step['highlight']:
                    if 0 <= index < len(step['array']):
                        bar_colors[index] = '#F00F0F'
            if step.get('currentPos'): # Green
                for index in step['currentPos']:
                    if 0 <= index < len(step['array']):
                        bar_colors[index] = '#00FF00'
            if step.get('swapPos'): # Yellow
                for index in step['swapPos']:
                    if 0 <= index < len(step['array']):
                        bar_colors[index] = '#FFFF00'

            # Plot The Array With Updated Colors
            plotArray(arr_chart, step['array'], bar_colors)
            time.sleep(delay) # Set The Delay ( By User )


if __name__ == '__main__':
    main()
