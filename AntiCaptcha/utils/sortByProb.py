def byProb(e):
    return e[1]

def sortByProb(arr):
    new_arr = [(i, arr[i]) for i in range(len(arr))]
    new_arr.sort(key=byProb, reverse=True)

    return new_arr