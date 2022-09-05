list=[55,6,3,8,1,9,6,9]
print(list)
for i in range(len(list)):
    min_index=i
    for j in range(i+1,len(list)):
        if list[j]<list[min_index]:
            min_index=j
    if list[i]!=list[min_index]:
        list[i],list[min_index]=list[min_index],list[i]
print(list)