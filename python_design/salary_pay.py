
class Wages():
    def __init__(self,name,hours,salary_hours):
        self.name=name
        self.hours=hours
        self.salary=salary_hours
        self._week_salary=0
    def payForWeek(self):
        if self.hours>40:
            self._week_salary=40*self.salary+1.5*(self.hours-40)*self.salary
        else:
            self._week_salary=self.hours*self.salary
    def __str__(self):
        return "Pay for %s:$%f"%(self.name,self._week_salary)

def main():
    name=raw_input("Enter person's name:")
    hours=int(raw_input("Enter number of hours worked:"))
    salary_hours=int(raw_input("Enter hourly wage:"))
    wage=Wages(name,hours,salary_hours)
    wage.payForWeek()
    print wage
main()