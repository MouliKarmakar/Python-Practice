class RailwayFrom :
    fromType = "RailwayFrom"

    def PrintData(self):
        print(f"name is {self.name}")
        print(f"train name{self.train}")

moulisapplication = RailwayFrom()
moulisapplication.name = "Mouli"
moulisapplication.train = "Rajdhani-Express"
moulisapplication.PrintData()

