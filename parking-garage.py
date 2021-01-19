class ParkingGarage: 
    def __init__(self,available, occupied, paid_dict): 
        self.available = available
        self.occupied = occupied 
        self.paid_dict = paid_dict
    
#when a person wants tp park, takes a ticket out of list, assignees that ticket number to a space, adds the space number to the dictionary with value of unpaid
    def park(self):
        if len(self.available) == 0: 
            print('Sorry. Our parking garage is full! \n')
        else: 
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
                parking_space = int(input("What number space are you in? "))
                if parking_space not in self.occupied:
                    print("That space is not currently occupied, please input a valid space number")
                else:
                    break
            except ValueError:
                print("Whoops! It looks like you didn't type a valid space. Please type a valid space number")
                
        #confirm the user wants to pay

        if self.paid_dict[parking_space] == "paid": 
            print('This ticket has already been paid')
        else:
            print('This ticket requires payment')
            pay = input("Please type 'Y' to pay ")
            #toggles the value for the key in the paid dict from unpaid to paid
            if pay.lower() == "y":
                self.paid_dict[parking_space] = "paid"
            print(f'Your ticket for space "{parking_space}" has now been marked as "{self.paid_dict[parking_space]}". You have 15 minutes to leave your space.')


    def leaveGarage(self):
        print(f'The Following Spaces Are Full:\n{self.occupied}')
        while True:
            try:
                paid_space = int(input("Please enter the parking space number of your pre-paid ticket? ")) 
                if paid_space not in self.occupied:
                    print("That space is not currently occupied, please input a valid space number: ")
                else:
                    break
            except ValueError:
                print("Whoops! It looks like you didn't type a valid space. Please type a valid space number")
                
        #if ticket is paid, they person leaves 
        if self.paid_dict[paid_space] == 'paid':
            self.occupied.remove(paid_space)
            self.available.append(paid_space)
            self.available.sort()
            del self.paid_dict[paid_space]
            print("Thank you safe travels :) \n")
        else:
            command = input("Your parking has not yet been paid for, would you like to pay y/ n?: ")
            if command.lower() == "n":
                print("Goodbye \n")
                # break
            elif command.lower() == "y":
                self.payForParking()

    def showBook(self):
        print("Here's the list of current occupied spaces and their pad status ")
        print(self.paid_dict)
        print("\n")

capitolParkingGarage = ParkingGarage([1,2,3,4,5,6,7,8,9,10],[],{})
def run():
    while True:
        action = input("Welcome to the parking garage! What would you like to do today \n Park/Pay/Leave/Show/Quit: ")
        if action.lower() == "quit":
            print("GoodBye")
            break
        elif action.lower() == "park":
            capitolParkingGarage.park()
        elif action.lower() == "pay":
            capitolParkingGarage.payForParking()
        elif action.lower() == "leave":
            capitolParkingGarage.leaveGarage()
        elif action.lower() == "show":
            capitolParkingGarage.showBook()
        else:
<<<<<<< HEAD
            print("Not a valid entry try again: ")
run()
=======
            print("Not a valid entry, please try again: ")
run()
>>>>>>> e110ff3a56da415562a3e9019ba76afe4eb25caa
