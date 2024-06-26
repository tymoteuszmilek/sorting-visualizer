def selectionSort(arr):
    steps = []
    n = len(arr)

    for i in range(n-1):
        minValueIndex = i
        # Select Min Value
        for j in range(i+1, n):
            currValue = arr[j]

            if currValue < arr[minValueIndex]:
                minValueIndex = j

        # Swap Current Element With Min Element
        arr[i], arr[minValueIndex] = arr[minValueIndex], arr[i]

        steps.append({
            'array': arr.copy(),
        })

    return steps