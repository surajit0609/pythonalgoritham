a=[9,5,1,4,3]
for i in range(1,len(a)):
    temp=a[i]
    k=i
    while k>0 and temp<a[k-1]:
        a[k]=a[k-1]
        k=k-1
    a[k]=temp
print(a)