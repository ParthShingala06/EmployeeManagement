class Salary:
    def __init__(self, Analyst = 1000, Associate = 2000, SrAssociate = 3000, VP = 5000, MD = 10000, CEO = 20000):
        self.Analyst = Analyst
        self.Associate =  Associate
        self.SrAssociate = SrAssociate
        self.VP = VP
        self.MD = MD
        self.CEO = CEO 

    def SalaryUpdate(self, position, salary):
        if position == "Analyst":
            self.Analyst = int(salary)
        elif position == "Associate":
            self.Associate = int(salary)
        elif position == "SrAssociate":
            self.SrAssociate = int(salary)
        elif position == "VP":
            self.VP = int(salary)
        elif position == "MD":
            self.MD = int(salary)
        elif position == "CEO":
            self.CEO = int(salary)
