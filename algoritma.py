def selection_sort(arr):
    """Algoritma Pengurutan 1: Selection Sort[cite: 16, 47]."""
    data = list(arr)
    n = len(data)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if data[j]["skor_akhir"] > data[max_idx]["skor_akhir"]: 
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
    return data

def merge_sort(arr):
    """Algoritma Pengurutan 2: Merge Sort[cite: 16, 47]."""
    if len(arr) <= 1: 
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["skor_akhir"] >= right[j]["skor_akhir"]: 
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result