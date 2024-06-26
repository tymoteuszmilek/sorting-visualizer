import streamlit as st
import numpy as np
import time

import quickSort
import mergeSort
import selectionSort
import insertionSort
import bubbleSort

sortingAlgorithms = {
    "Quick Sort": quickSort.quickSort,
    "Merge Sort": mergeSort.mergeSort,
    "Selection Sort": selectionSort.selectionSort,
    "Insertion Sort": insertionSort.insertionSort,
    "Bubble Sort": bubbleSort.bubbleSort,
}

# Plot The Array As A Bar Chart
def plotArray(arr_chart, arr):
    data = {'data': arr}
    arr_chart.bar_chart(data)

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
            plotArray(arr_chart, step['array'])
            time.sleep(delay) # Set The Delay ( By User )

if __name__ == '__main__':
    main()
