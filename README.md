# Sorting Algorithm Visualizer

## Overview
This project is a visual representation of various sorting algorithms. It provides an interactive way to understand how different sorting algorithms work by visualizing the steps taken by the algorithm to sort an array. The project is built using Python and Streamlit for the user interface.

## Features
- **Interactive UI:** Choose from a variety of sorting algorithms.
- **Adjustable Parameters:** Change the array size and animation speed.
- **Real-Time Visualization:** Watch how the array gets sorted step-by-step.
- **Highlighting:** Different colors for boundaries, current position, and swaps for better understanding (green is the current element, red is element that is being compared with current element, yellow are elements that got swapped.

## Sorting Algorithms Implemented
- Quick Sort
- Merge Sort
- Selection Sort
- Insertion Sort
- Counting Sort
- Bubble Sort

## Live Deployment

The project is live and accessible via Streamlit Sharing. You can view it [here](https://sorting-visualizer-haxdhnrqm6cvfm3cblvr24.streamlit.app).

## How to Use
1. **Setup:**
    - Ensure you have Python and pip installed on your machine.
    - Clone the repository:
      ```bash
      git clone https://github.com/tymoteuszmilek/sorting-visualizer.git
      cd sorting-algorithm-visualizer
      ```
    - Install the required dependencies:
      ```bash
      pip install -r requirements.txt
      ```

2. **Run the Application:**
    - Start the Streamlit app:
      ```bash
      streamlit run visualizer.py
      ```
    - Open the web browser and go to the provided local URL.

3. **Interact with the App:**
    - Select a sorting algorithm from the dropdown menu.
    - Adjust the array size and animation delay using the provided sliders and input fields.
    - Click the "Sort" button to see the algorithm in action.
