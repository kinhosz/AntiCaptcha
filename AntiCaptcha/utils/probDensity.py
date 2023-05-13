def probDensityArr(position, size):
    arr = [0 for _ in range(size)]
    arr[position] = 1.0

    return arr