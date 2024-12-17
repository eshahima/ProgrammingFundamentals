
#create for loop to output odd integers less than or equal to 100
print("odd integers from 0-100")

for x in range(0,100):
    if x%2 != 0:
        print(x)

#create while loop to output even intefers less than or equal to 100
x = 100
print("even integers from 100-0")

while x<=100 and x>= 0:
    if x%2 == 0:
        print(x)
    x -= 1

#create a loop to continue to see values
print("Do you want to see the loop again?")
inp = input()

x=0 
if inp == "yes":
    while x<=10 and x>= 0:
        if x%2 == 0:
            print(x)
        x +=1

#input user's own starting and ending values
print("let's create a loop for you:")
print("Enter the starting value of your loop:")
start = input()
starto= int(start)

print("Enter ending value of your loop")
end = input()
endo = int(end)


for x in range(starto, endo):
    if x %2 == 0:
        print(x)
x +=1

