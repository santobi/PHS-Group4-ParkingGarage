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

list for parking ticekts 
- one list for used 
- one list for unused or avaiable tickets 

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
    
#when a person wants tp park, takes a ticket out of list, assignes that ticket number to a space, adds the space number to the dictionary with value of unpaid
    def park(self): 
        '''
   - This should decrease the amount of tickets available by 1
   - This should decrease the amount of parkingSpaces available by 1'''
        new_space = self.ticket.pop(0) #removes one/index value from tickets list 
        self.space.append(new_space)
        self.paid[new_space] = "Unpaid"

#when paying for parking, changes dictionary value for key (space)
    def payForParking(self):
        paid_space = int(input("What number space are you in?"))
        print(spaces)
        space.remove(paid_space)
        ticket.append(paid_space)
        ticket.sort()



garageSession = ParkingGarage([10],[],{})
run()
    if quit
        quit
    if Parking
        do ticket_num
    if paying
        do the paying method
    if leaving
        do the leaving method


    
