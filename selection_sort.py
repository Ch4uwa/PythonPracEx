from makearray import make_array
arr = make_array()


def selection_sort(arr):
    current_idx = 0
    while current_idx < len(arr) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(arr)):
            if arr[smallest_idx] > arr[i]:
                smallest_idx = i
        swap(current_idx, smallest_idx, arr)
        current_idx += 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    print(selection_sort(arr))
