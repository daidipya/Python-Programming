#Bubble Sort by Rohan

n = input("Please Enter How much numbers:")
l1=[]
for i in range(0,n):
    no = input("Enter Number:")
    l1.append(no)
    
print "Input list is:"
print l1

for x in range(0,n):
    for y in range(0, n-x-1):
        if(l1[y]>l1[y+1]):
            temp = l1[y]
            l1[y]=l1[y+1]
            l1[y+1]=temp
            
print "Sorted list is:"
print l1