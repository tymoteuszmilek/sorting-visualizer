def countingSort(arr):
    steps = []
    maxValue = max(arr)
    countingArr = [0 for _ in range(maxValue + 1)]
    n = len(arr)
    count = 0

    for item in arr:
        countingArr[item] += 1

        steps.append({
            'array': arr.copy(),
            'highlight': [count]
        })
        count += 1

    index = 0
    for value, count in enumerate(countingArr):
        while count > 0:
            arr[index] = value
            steps.append({
                'array': arr.copy(),
                'currentPos': [index]
            })
            index += 1
            count -= 1

    return steps
