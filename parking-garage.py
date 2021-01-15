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

    

    def park(self):
       self.new_space = ticket.pop(0)
       self.space.append(new_space)
       self.occupied_space(new_space)

    def payForParking(self):
        paid_spaces = int(input("What number space are you in?"))
        print()
