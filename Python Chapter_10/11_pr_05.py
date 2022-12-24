class Train:        
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats =seats

    def status(self):
        print(f"the name of this train is :{self.name}")
        print(f"the fare is : {self.fare}")

    def fareinfo(self):    
        print(f"the number of seats :{self.seats}")

    def bookticket(self):
        if self.seats>0:
            print(f"your ticket has been booked. your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("sorry, this train is full,\n kindly try in tatakal.")

    
intercity = Train( "Intercity_Express",100,340)
intercity.status()
intercity.fareinfo()
intercity.bookticket()

intercity.bookticket()
intercity.bookticket()




        