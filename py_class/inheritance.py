class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}, ID: {self.id}") 

class Programmer(Employee):
    def __init__(self, name, id, language):
        self.name = name
        self.id = id
        self.language = language
        
    def showinfo(self):
        print(f"Name: {self.name}, ID: {self.id}, Language: {self.language}")
    

e = Employee("Prion", 123)
e.showDetails()
e1 = Programmer("Prion", 123, "Python")
e1.showinfo()  