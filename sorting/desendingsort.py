list2=[55,76,9,0,4,3]
print(list2)
for i in range(len(list2)):
    max_val=max(list2[i:])
    max_ind=list2.index(max_val)
    if list2[i]!=list2[max_ind]:
        list2[i],list2[max_ind]=list2[max_ind],list2[i]
print(list2)
