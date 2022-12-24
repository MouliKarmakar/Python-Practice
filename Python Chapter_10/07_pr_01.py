class Programer :
    company = "microsoft"

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language

    def get_Dtailas(self):
        print(f"the name of the programer is {self.name}")
        print(f"the salary is {self.salary}")
        print(f"the coding language he uses is {self.language}")

sumit = Programer("sumit",120,"C++")
sujoy = Programer("sujoy",130,"Python0")
ashim = Programer("ashim",145,"java")
subir = Programer("subir",150,"java script")

sumit.get_Dtailas()
sujoy.get_Dtailas()
ashim.get_Dtailas()
subir.get_Dtailas()

