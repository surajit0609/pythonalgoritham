def bobblesort(a):
    for passnumber in range(len(a)-1,0,-1):
        for i in range(passnumber):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    print(a)
a=[10,4,43,5,57,91,45,9,7]
bobblesort(a)