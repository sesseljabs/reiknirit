import time
listi = [i for i in range(100000, 1, -1)]
start_time = time.time()
print("start")

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted(listi)


print(sorted(listi))


print("--- %s seconds ---" % (time.time() - start_time))