# list1=list(map(int,input("\nEnter the numbers : ").strip().split()))
list1=[55,7,3,9,0,22,1]
print(list1)
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    if list1[i]!=list1[min_index]:
        list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
