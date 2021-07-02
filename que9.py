class Employee:
    def __init__(self):
        pass
    def display(self):
        self.data={}

        self.count = int(input("Enter no.of employees working under manager: "))
        for i in range(0, self.count):
            print("Enter the details of Employee", i + 1, ":")
            self.name = input("Enter name: ")
            self.age = input("Enter age: ")
            self.experience = input("Enter experience: ")
            self.salary = input("Enter salary: ")
            self.data[i+1]={"Employee name":self.name,"age":self.age,"experience":self.experience,"salary":self.salary}

class Manager(Employee):
    def __init__(self):
        super().__init__()

    def manager(self,n,a,e,s):
        self.n=n
        self.a=a
        self.e=e
        self.s=s

    def display(self):
        super().display()
        print("Details of manager: ")
        print("NAME: ", self.n)
        print("AGE: ", self.a)
        print("EXPERIENCE:", self.e)
        print("SALARY: ", self.s)
        print("Details of employees working under manager ",self.n,"are: ")
        print(self.data)

manager=Manager()
manager.manager("Vijay","45","16years","150000")
manager.display()