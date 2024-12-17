#import datetime and timedelta classes from datetime module…. This helped me better store the dates and add the data
from datetime import datetime, timedelta

class User: #declaring user class
    def __init__(self, firstday, cyclelength):
#function _init_ basically taking in the parameters for the user and constructing it and assigning it new variables that can be used locally thoughout the class
        self.cyclelength = cyclelength #stores the cycle length input/parameter
        self.firstday = datetime.strptime(firstday, "%Y-%m-%d") #stores the first day input/parameter
        self.periods = [] #creating an array for periods
        self.ovulations = [] #creating an array for ovulations
        self.add_period(firstday)   #calling add_period() function in order to automatically add the dates into the arrays    

    def predictperiod(self): #this function predicts the period by adding cycle length to the first date and the user class is a parameter to this function
        return self.firstday + timedelta(days=int(self.cyclelength))
    #the cycle length is typecasted into an int and is a parameter to timedelta… helping it add to the first day to calculate the next period date
    def predictovul(self):
        return self.firstday + timedelta(days=(int(self.cyclelength) - 14))#cycle length selfcasted into int and subtracted by 14 and put into timedelta method and added to the first day
    #this function predicts the next ovulation date by adding the difference of cycle length and 14 to the first day of the period


    def add_period(self, firstday):#this function adds the period and ovulation date onto the periods and ovulation arrays
        date = datetime.strptime(firstday, "%Y-%m-%d")#stores the first date in the date format by putting it through the strptime method
        self.periods.append(date)#appends the firstday of period to the periods array
        self.ovulations.append(date + timedelta(days=(int(self.cyclelength)) - 14))#appends the date given to ovulations array

user = None #declares user = none to avoid error
while True: #helps create an infinite loop
    userinput = input("Do you want to start/continue? ") #takes in input when asked if wanted to continue
    if userinput.lower() == 'no': #breaks if no 
        break
    cyclelength = input("Enter your cycle length: ") #takes in input when asked about cycle length
    firstday = input("Enter the first date of your last period (YYYY-MM-DD): ") #takes in input when asked about first date of last period
    userin = input("Do you want to predict the first date of your next period or ovulation? ") #ask if wants to predict first date or ovulation
    if userin.lower()== 'first date':#if statement that evaluates if the user input says first date
        user = User(firstday, cyclelength)# calls the user class and puts in the stored inputs as parameters
        print("Your next period is on:", user.predictperiod().strftime("%Y-%m-%d")) #prints out the next period by calling the predictperiod function specifically for the user 
        print(user.periods)    #prints the periods array which is specifically for the user
    elif userin == 'ovulation': #evaluates if the user input was ovulation
        user = User(firstday, cyclelength) #calls the user class and puts in stored input as parameters
        print("Your ovulation is on:", user.predictovul().strftime("%Y-%m-%d")) #prints out the predicted ovulation date by calling the predictovul() function specifically for the user
        print(user.ovulations)#prints the ovulations array which is specifically for the user
