x = 2
#describe: uses the criteria to control flow of program; picks a path or excutes a part of code based on crietria
#basic conditional el-if:

if x == 1:
    print("true")
else:
    print("false")

#multiway branching conditional

if x == 3:
    print("false")
elif x == 2:
    print("true")
else:
    print("false")

while True: 
    userinput = input("do you want to play a game?")
    
    if userinput.lower() == 'no':
        break

    elif userinput.lower() == 'yes':
        print("enter a number")
        x = input()
``

        print("enter another number")
        y = input()

        sum = int(x) + int(y)
 
        if sum > 0:
            print("The sum of the numbers is positive.")
        
        elif sum < 0:
            print("The sum of the numbers is negative.")
        
        else:
            print("The sum of the numbers is zero.") 
    
