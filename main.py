class student:
    grade=11
    def display(self):
        print("My grade is",self.grade)

ob=student()
ob.display()

class studentA:
    grade=10
    name="Refilwe"
    def intro(self):
        print("Hi I'm a student at this school")
    def printout(self):
        print("My name is",self.name,"My grade is",self.grade)
obj=studentA()
obj.intro()
obj.printout()