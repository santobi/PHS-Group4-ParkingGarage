'''
Parking garage class with a few methods 
Garage class: 
attributes: 
- tickets list 
- parking space list 
- current ticket dict()
    -key: space number / value: paid/unpaid 

methods: 
- take ticket 
- pay for parking  
- leaving garage 

list for parking tickets 
- one list for used 
- one list for unused or available tickets 

list for parking spaces 
- available spaces 
- taken spaces 


Features for later: 
- garage is full 
- scan ticket 

'''

class ParkingGarage: 
    def __init__(self,available, occupied, paid_dict): 
        self.available = available #expect this to be a list of available parking spaces
        self.occupied = occupied #the list of occupied parking spaces
        self.paid_dict = paid_dict #a dictionary containing the space occupied and if the ticket is paid or unpaid
    
#when a person wants tp park, takes a ticket out of list, assignees that ticket number to a space, adds the space number to the dictionary with value of unpaid
    def park(self): 
        '''
   - This should decrease the amount of tickets available by 1
   - This should decrease the amount of parkingSpaces available by 1''' 
        parking_space = self.available.pop(0) #removes the first available space from the tickets list 
        print(f"You can now park at space {parking_space}. Please enjoy your parking! \n")
        #moves available space to list of occupied spaces
        self.occupied.append(parking_space)
        #creates dictionary entry for the space and marks the value as unpaid
        self.paid_dict[parking_space] = "Unpaid"

#when paying for parking, changes dictionary value for key (space)
    def payForParking(self):
        #finds the space the user wants to pay for
        print(f'The Following Spaces Are Occupied:\n{self.occupied}')
        while True:
            try:
                parking_space = int(input("What number space are you in?")) 
            except ValueError:
                print("Whoops! It looks like you didn't type a valid space. Please type a valid space number")
            else:
                if parking_space not in self.occupied:
                    print("That space is not currently occupied, please input a valid space number")
        #confirm the user wants to pay
        ##TODO - check if the space they want to pay is currently paid or unpaid, if paid, prompt them they dont need to pay twice
        pay = input("Please type 'Y' to pay")
        #toggles the value for the key in the paid dict from unpaid to paid
        if pay.lower() == "y":
    
            self.paid_dict[parking_space] = "paid"
        print(f'Your ticket for space "{parking_space}" has now been marked as "{self.paid_dict[parking_space]}". You have 15 minutes to leave your space.')
        ##TODO, bring them right to the leave function????

    def leaveGarage(self):
        print(f'The Following Spaces Are Full:\n{self.occupied}')
        while True:
            try:
                paid_space = int(input("What number space are you in?")) 
                break
            except ValueError:
                print("Whoops! It looks like you didn't type a valid space. Please type a valid space number")
            else:
                if parking_space not in self.occupied:
                print("That space is not currently occupied, please input a valid space number")
        #if ticket is paid, they person leaves ###TODO add in print statements to show they left
        if self.paid_dict[paid_space] == 'paid':
            self.occupied.remove(paid_space)
            self.available.append(paid_space)
            self.available.sort()
        else:
            command = input("Your parking has not yet been paid for, would you like to pay y/ n?: ")
            if command.lower() == "n":
                print("Goodbye")
                # break
            elif command.lower == "y":
                self.payForParking()
            ##TODO print statement to thank them for paying and havie a nice day
        ##TODO - delete corresponding dict entry for space


capitolParkingGarage = ParkingGarage([1,2,3,4,5,6,7,8,9,10],[],{})
def run():
    while True:
        action = input("Welcome to the parking garage! What would you like to do today \n Park/Pay/Leave/quit: ")
        if action.lower() == "quit":
            print("GoodBye")
            break
        elif action.lower() == "park":
            capitolParkingGarage.park()
        elif action.lower() == "pay":
            capitolParkingGarage.payForParking()
        elif action.lower() == "leave":
            capitolParkingGarage.leaveGarage()
        else:
            print("Not a valid entry try again: ")
run()
