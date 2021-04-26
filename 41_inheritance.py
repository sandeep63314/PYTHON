from functools import reduce
class project:
    grade = 'A'
    def __init__(self,name,empcount,revenue):
        self.projectname = name
        self.employeecount = empcount
        self.revenue = revenue
    def project_performance(self):
        if self.revenue >= 100000:
            grade = 'A'
        elif 80000 <= self.revenue < 100000:
            grade = 'B'
        elif 50000 <= self.revenue < 80000:
            grade = 'C'
        elif 30000 <= self.revenue < 50000:
            grade = 'D'
        else:
            grade = 'E'
        return grade
class tcs(project):    
    def __init__(self,name,empcount,revenue,year):
        project.__init__(self,name,empcount,revenue)
        self.currentyear = year
    def calculate_total_revenue(*args):
        totalrevenue = reduce(lambda acc,x : acc + x,args)
        return totalrevenue
    def calculate_total_employee(*args):
        totalemployee = reduce(lambda acc,x : acc + x,args)
        return totalemployee
    def performance_evaluation(*args):
        for prjs in args:
            if prjs.project_performance() == 'A':
                print(f'{prjs.projectname} is performing more than expected. Keep it up!!!')
            elif prjs.project_performance() == 'B':
                print(f'{prjs.projectname} is performing as expected. Thank you')
            elif prjs.project_performance() == 'C':
                print(f'{prjs.projectname} is performing average.')
            elif prjs.project_performance() == 'D':
                print(f'{prjs.projectname} is performing less than average. Need to improve it\'s performance')
            elif prjs.project_performance() == 'E':
                print(f'{prjs.projectname} has failed to meet it\'s expectations. Need immediate attention')    

year = input('Enter the current year:')    
cibc = tcs('CIBC',11111,100000,year)
generalmotors = tcs('GENERAL ELECTRONICS',22222,80000,year)
print(f'Total revenue of TCS in year:{year} is ${tcs.calculate_total_revenue(cibc.revenue,generalmotors.revenue)}')
print(f'Total number of employees of TCS in year:{year} is {tcs.calculate_total_employee(cibc.employeecount,generalmotors.employeecount)}')
tcs.performance_evaluation(cibc,generalmotors)
