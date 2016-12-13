print("Bubble Sort In Python")
n = int(raw_input("How many numbers you want to enter"))
print(n)
l1 = []
for x in range(0 , n):
    no = input("Enter number:")
    l1.append(no)
print(l1)

for x in range(0,n):
    for y in range(0,n-1-x):
        if(l1[y] > l1[y+1]):
            temp=l1[y]
            l1[y]=l1[y+1]
            l1[y+1]=temp
print("The list of bubble sort")            
print(l1)




  