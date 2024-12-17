#array is a variable that stores items; index starts at 0

array = [["Esha", "Himagirish", "17", "4'11"], ["Algebra", "Math", "12"], ["es", "sa", "rt"]]
user_input = input("Input your name and age seperated with commas and inside [];  type done, once done")
x = len(array)
while user_input.lower() != 'done':
    array.insert(x+1, user_input)
    user_input =  input("Input your name: and type done once done")
    
number = input("input row number to print out information")
row = int(number) - 1

print(array[row])
#rownumber = input("input ")
