def mergeSort(arr):
    steps = []

    def _mergeSort(arr, left, right):
        if left < right:
            mid = (left + right) // 2

            steps.append({
                'array': arr.copy(),
                'boundaries': [left, right]
            })

            _mergeSort(arr, left, mid)
            _mergeSort(arr, mid + 1, right)
            merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1

        # Merge Two Halves Into temp array In Sorted Order
        while i <= mid and j <= right:

            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1

                steps.append({
                    'array': arr.copy(),
                    'boundaries': [left, right],
                    'highlight': [i - 1],
                })
            else:
                temp.append(arr[j])
                j += 1

                steps.append({
                    'array': arr.copy(),
                    'boundaries': [left, right],
                    'highlight': [j - 1],
                })


        # Append Remaining Elements From Left Half
        while i <= mid:
            temp.append(arr[i])
            i += 1

            steps.append({
                'array': arr.copy(),
                'boundaries': [left, right],
                'highlight': [i - 1],
            })

        # Append Remaining Elements From Right Half
        while j <= right:
            temp.append(arr[j])
            j += 1

            steps.append({
                'array': arr.copy(),
                'boundaries': [left, right],
                'highlight': [j - 1],
            })

        # Copy Sorted Elements From Temp Back To Original Array
        for k in range(len(temp)):
            arr[left + k] = temp[k]

            if k == 0:
                steps.append({
                    'array': arr.copy(),
                    'boundaries': [left, right]
                })

            steps.append({
                'array': arr.copy(),
                'boundaries': [left, right],
                'currentPos': [left + k]
            })

    _mergeSort(arr, 0, len(arr) - 1)
    return steps
