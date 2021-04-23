# import sys
# sys.setrecursionlimit(100000)
#
#
# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
#
# def quickSort(arr, low, high):
#     if len(arr) == 1:
#         return arr
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# # arr = [i for i in range(N)]
# quickSort(arr, 0, N-1)
# for k in arr:
#     print(k)

# N = int(input())
# arr = [int(input()) for _ in range(N)]
# # arr = [-i for i in range(N)]
# minus = [0 for _ in range(1000001)]
# plus = [0 for _ in range(1000001)]
#
# for number in arr:
#     if number < 0:
#         minus[number + 1000000] = 1
#     else:
#         plus[number] = 1
#
# for m in range(1000001):
#     if minus[m] == 1:
#         print(m - 1000000)
# for p in range(1000001):
#     if plus[p] == 1:
#         print(p)

# N = int(input())
# arr = sorted([int(input()) for _ in range(N)])
# for n in arr:
#     print(n)

# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     # create temp arrays
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     # Copy data to temp arrays L[] and R[]
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#
#     # Merge the temp arrays back into arr[l..r]
#     i = 0  # Initial index of first subarray
#     j = 0  # Initial index of second subarray
#     k = l  # Initial index of merged subarray
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # Copy the remaining elements of L[], if there
#     # are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # Copy the remaining elements of R[], if there
#     # are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
#
#
# # l is for left index and r is right index of the
# # sub-array of arr to be sorted
# def mergeSort(arr, l, r):
#     if l < r:
#         # Same as (l+r)//2, but avoids overflow for
#         # large l and h
#         m = (l + (r - 1)) // 2
#
#         # Sort first and second halves
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# mergeSort(arr, 0, N-1)
# for k in arr:
#     print(k)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

N = int(input())
K = [int(input()) for _ in range(N)]
heapSort(K)
for k in K:
    print(k)