'''// Iterative Bubble Sort
bubbleSort(arr[], n)
{
  for (i = 0; i < n-1; i++)

     // Last i elements are already in place
     for (j = 0; j  arr[j+1])
         swap(arr[j], arr[j+1]);
}

def stafrof(st):
    if len(st)==1:
        return st
    st = list(st)
    max = (0,0)
    for i in range(0,len(st)):
        if st[i] > max[0]:
            max = (st[i],i)
    st.insert(max[1],max[0])


    st = str(st)
    return stafrof(st[1:])
print(stafrof("eabc"))'''



def partition(arr,low,high):
    i = (low - 1)
    pivot = arr[ high ]

    for j in range(low,high):

        if arr[j] < pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)


def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi - 1)
        quickSort(arr,pi + 1,high)
arr = ["q","a"]
print(quickSort(arr, 0, len(arr)-1))
print(arr)


