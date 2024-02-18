class Employee:
    company="Google"

    def showdetails(self):
        print("This is an employee")

class Programmer(Employee):
    language="python"

    def getlanguage(self):
        print(f"the language is{self.language}")

    e=Employee()
    e.showdetails()
    