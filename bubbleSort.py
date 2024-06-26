def bubbleSort(arr):
    steps = []
    n = len(arr)
    swapped = True

    # If Any Element From arr Will Get Swapped Keep The Loop
    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                steps.append({
                    'array': arr.copy(),
                    'currentPos': [i],
                    'highlight': [i + 1]
                })
                # Swap Elements [i, j] if arr[i] > arr[j]
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

                steps.append({
                    'array': arr.copy(),
                    'swapPos': [i, i + 1]
                })
            else:
                steps.append({
                    'array': arr.copy(),
                    'currentPos': [i],
                    'highlight': [i + 1],
                })
        n -= 1

    steps.append({
        'array': arr.copy(),
    })

    return steps
