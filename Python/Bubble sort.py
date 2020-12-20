
def sort(List):
    for i in range(len(List)):
        for j in range(len(List)-1):
            if List[j]>List[j+1]:
                temp=List[j]
                List[j]=List[j+1]
                List[j+1]=temp

List=[5,6,7,1,4,8,3,2,9]
sort(List)
print(List)