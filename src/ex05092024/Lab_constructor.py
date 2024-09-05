class Employee:
    #Attribute
    id=None
    name=None
    Age=None
    Address=None
    Phone=None
    eid=None


    #Behaviours
    # def sleep2(self, name):
      #  print("I am a Method!")
       # return None

    def __init__(self,name):
        print("Called, Object is created")
        self.name = name

employee1=Employee("Vidya")
print(employee1.name)

employee2=Employee("Vids")
print(employee2.name)
