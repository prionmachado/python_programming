class Employee:
    def __init__(self):
        self.__name = "Prion"   # private variable prefixed with __ 

a = Employee()
# print(a.__name) # cannot be accessed directly
print(a._Employee__name) # can be accessed indirectly