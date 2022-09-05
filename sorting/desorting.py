list=[55,7,0,7,55,3,3,9,0,22,1]
print(list)
for i in range(len(list)):
    max_index=i
    for j in range(i+1,len(list)):
        if(list[j]>list[max_index]):
            max_index=j
    if list[i]!=list[max_index]:
        list[i],list[max_index]=list[max_index],list[i]
print(list)