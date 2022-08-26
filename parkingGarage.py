


class Garage():
    def __init__(self, tickets_available, space_available, currentTickets, cost= 3):
        self.tickets_available = tickets_available
        self.space_available = space_available
        self.cost = cost
        self.currentTickets = currentTickets


    def enter(self):
        if self.tickets_available == 0:
            print('Sorry we are out of space! better luck next time loser!')
            return False
       
        else:
            print('Here is your ticket!')
            garage.tickets_available -= 1 
            garage.space_available -= 1 
            

    
    
    def leave(self):
        print(f'Your total is {self.cost}')
        payed = int(input('Please pay here!: '))
        
        if int(payed) == self.cost:
            print('I hope you found a great parking spot! come again!')
            garage.tickets_available += 1
            garage.space_available += 1
            garage.currentTickets['ticket'] = False
        else:
            print('Stop being broke, and get a job! its literally $3')


        

    
garage = Garage(3, 3,{'ticket': False})






class run():
    while True:
        
        answer = input('Welcome to our Parking Garage! Would you like to enter or leave?: ')

        if answer == 'leave':
            garage.leave()


        elif answer == 'enter':
            garage.enter()
      






