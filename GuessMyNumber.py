import random
print "Welcome to the game : Guess My Number"
range="1 to 10"
num = random.randint(1,10)
#print num
while True:
    
    userNum = int(input("Guess the number in "+range+": "))
    if userNum>num:
        print "Number is high"
    else:
        if userNum<num :
            print "Number is low"
        else:
            print "Number Guess is correct",num
            break;
            
        
        
    
    
    

