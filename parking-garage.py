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
    def __init__(self,ticket, space, paid): 
        self.ticket = ticket
        self.space = space 
        self.paid = paid 
    
#when a person wants tp park, takes a ticket out of list, assignees that ticket number to a space, adds the space number to the dictionary with value of unpaid
    def park(self): 
        '''
   - This should decrease the amount of tickets available by 1
   - This should decrease the amount of parkingSpaces available by 1''' 
        new_space = self.ticket.pop(0) #removes one/index value from tickets list 
        print(f"You can now park at space {new_space}. Please enjoy your parking! \n")
        self.space.append(new_space)
        self.paid[new_space] = "Unpaid"

#when paying for parking, changes dictionary value for key (space)
    def payForParking(self):
        #finds the space the user wants to pay for
        parking_space = int(input("What number space are you in?"))
        print(self.space)
        #confirm the user wants to pay
        pay = input("Please type 'Y' to pay")
        #toggles the value for the key in the paid dict from unpaid to paid
        if pay.lower() == "y":
            self.paid[parking_space] = "paid"
        print("Thank you for paying! Your ticket has now been marked as paid.")
        print(self.paid.items(parking_space))

    def leaveGarage(self):
        self.paid = paid_space
        self.space.remove(paid_space)
        self.ticket.append(paid_space)
        self.ticket.sort()

capitolParkingGarage = ParkingGarage([1,2,3,4,5,6,7,8,9,10],[],{})
def run():
    while True:
        action = input("Welcome to the parking garage! What would you like to do today \n Park/Pay/Leave")
        if action.lower() == "park":
            capitolParkingGarage.park()
        elif action.lower() == "pay":
            capitolParkingGarage.payForParking()
        elif action.lower() == "leave":
            capitolParkingGarage.leaveGarage()
run()
