class Student:
    def __init__(self,nm,roll):
        self.name=nm
        self.rollno=roll
    def __init__(self,nm,roll,mk):
         self.name=nm
         self.rollno=roll
         self.marks=mk
    def __init__(self,nm):
         self.name=nm
    def display(self):
        print(f'{self.name}') 
s=Student('smita')
s.display()
    
    

 

        
        




