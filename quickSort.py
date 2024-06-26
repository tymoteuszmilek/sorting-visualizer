def quickSort(arr):
    steps = []

    def _quickSort(arr, left, right):
        if left < right:
            partitionPos = partition(arr, left, right)
            _quickSort(arr, left, partitionPos - 1)
            _quickSort(arr, partitionPos + 1, right)

    def partition(arr, left, right):
        i = left
        j = right - 1
        pivot = arr[right] # Take Last Element Of Arr As 'Pivot'

        steps.append({
            'array': arr.copy(),
            'boundaries': [left, right],
        })

        # Swap Elements [i, j] if arr[i] > pivot and arr[j] < pivot and i < j
        while i <= j:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i < j:

                steps.append({
                    'array': arr.copy(),
                    'boundaries': [left, right],
                    'currentPos': [i],
                    'highlight': [j],
                })

                arr[i], arr[j] = arr[j], arr[i]

                steps.append({
                    'array': arr.copy(),
                    'boundaries': [left, right],
                    'swapPos': [i, j],
                })
                i += 1
                j -= 1

        # Place the pivot element in its correct position
        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]

            steps.append({
                'array': arr.copy(),
                'boundaries': [left, right],
                'currentPos': [i],  # Indicate the current position of the pivot
            })
        else:
            steps.append({
                'array': arr.copy(),
                'boundaries': [left],
                'currentPos': [right],
            })

        return i

    _quickSort(arr, 0, len(arr) - 1)
    return steps
