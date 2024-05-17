class Employee:
    def __init__(self,id,salary,experience,dob):
        self.id=id
        self.salary=salary
        self.experience=experience
        self.dob=dob
           
    def iseligible(self):
        if self.experience>5:
            print(f"{self.id} is eligible for bonus")
            self.salary=0.20*self.salary+self.salary
        else:
            print(f"{self.id} is not eligible for bonus")
            self.salary=0.05*self.salary+self.salary
                
    def increment(self):
        self.bonus=0.10*self.salary
        print(self.bonus)