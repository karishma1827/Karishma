class Student:
    def __init__(self,n,i,ag,g):
        self.name=n
        self.id_number=i
        self.age=ag
        self.gpa=g
    
    def ishonour(self):
        if self.gpa>9:
            print(f"{self.name} is a honour student")
        else:
            print(f"{self.name } is not a honour student")
        

