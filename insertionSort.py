def insertionSort(arr):
    steps = []
    n = len(arr)

    for i in range(1, n):
        currentValue = arr[i]
        j = i - 1

        # Search The Correct Index to Insert currentValue
        while j >= 0 and currentValue < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        steps.append({
            'array': arr.copy(),
            'currentPos': [i],
            'highlight': [j + 1]
        })

        arr[j + 1] = currentValue

        steps.append({
            'array': arr.copy(),
            'swapPos': [j + 1, i]
        })

    return steps
