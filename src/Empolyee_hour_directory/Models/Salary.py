

class Salary:
    def __init__(self, Analyst = 1000, Associate = 2000, SrAssociate = 3000, VP = 5000, MD = 10000, CEO = 20000):
        self.Analyst = Analyst
        self.Associate =  Associate
        self.SrAssociate = SrAssociate
        self.VP = VP
        self.MD = MD
        self.CEO = CEO 

    def serialize(self):
        return {"Analyst": self.Analyst, "Associate": self.Associate, "SrAssociate": self.SrAssociate, "VP": self.VP, "MD": self.MD, "CEO": self.CEO}

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
    
    def getSalary(self, position):
        if position == "Analyst":
            return self.Analyst
        elif position == "Associate":
            return self.Associate
        elif position == "SrAssociate":
            return self.SrAssociate
        elif position == "VP":
            return self.VP
        elif position == "MD":
            return self.MD
        elif position == "CEO":
            return self.CEO

