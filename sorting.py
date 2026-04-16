arr=[5,3,9,2,7,6,4,8,0,23,6,546,67,35,36,457]
#.     selection sorting
def selectionsort(arr):
   n= len(arr)
   for i in range(n-1):
      smallInx= i
      for j in range(i+1,n):
         if arr[j]<arr[smallInx]:
            smallInx= j
      arr[i],arr[smallInx]= arr[smallInx],arr[i]
   return arr
print(selectionsort(arr))

#.     bubble sorting 
def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print("Before bubble sort:", arr)
print("After bubble sort:", bubblesort(arr))

#.     insertion sorting
def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        min=arr[i]
        j=i-1
        while j>=0 and arr[j]>min:
            arr[j+1]=arr[j]
            j-=1
            arr[j]=min

#.      merge sorting.  (divide > sort > merge)
def merge():
 def mergesort(arr,s,e):
    if s==e:
        return
    mid=(s+e)//2
    mergesort(arr,s,mid)
    mergesort(arr,mid+1,e)
    merge(arr,s,mid,mid+1,e)
    return arr
 print(mergesort(arr))
 

