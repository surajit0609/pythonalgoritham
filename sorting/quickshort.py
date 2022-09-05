def quickshort(a,low,high):
    if low<high:
        partitation_point=partitation(a,low,high)
        quickshort(a,low,partitation_point-1)
        quickshort(a,partitation_point+1,high)
    
def partitation(a,low,high):
    pivot=a[low]
    left=low+1
    right=high
    done=False
    while not done:
        while left<=right and a[left]<=pivot:
            left=left+1
        while left<=right and a[right]>=pivot:
            right=right-1
        if left>right:
            done=True
        else:
            a[left],a[right]=a[right],a[left]
    a[low],a[right]=a[right],a[low]
    return right



a=[50,25,92,16,76,30,43,54,19]
quickshort(a,0,len(a)-1)
print(a)