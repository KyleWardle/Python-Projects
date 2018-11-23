arr = [10,2,5,1,6,8,3,7,4,9,21,12,65,25]

length = len(arr)

for i in range(0, length - 1):
    for (key, val) in enumerate(arr):
        if (key != length - 1):
            if arr[key] > arr[key + 1]:
                store = arr[key]
                arr[key] = arr[key + 1]
                arr[key + 1] = store

for (key, val) in enumerate(arr):
    print(key, val)
