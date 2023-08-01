import sys

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Error")
    try:
        numbers = [int(arg) for arg in sys.argv[1::]]
    except ValueError:
        sys.exit("Error")

    bubble_sort(numbers)
    print(numbers)

