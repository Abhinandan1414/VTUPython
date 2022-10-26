''' 
7.b
Write a python program by creating a class called Employee to store the details of
Name, Employee_ID, Department and Salary, and implement a method to update salary
of employees belonging to a given department.
'''
class employee:
    def __init__(self):
        __id = 0
        __name = ""
        __gender = ""
        __city = ""
        __salary = 0

	
    def set_data(self, id=0, name=" ",gender = "", city = "", salary =0):
        self.__id=id
        self.__name = name
        self.__gender = gender
        self.__city = city
        self.__salary = salary
	
	
    def display_employee_data(self):
        print("--------------------------")
        print("Id\t:",self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)
        print("--------------------------")

def main_function():
    emp=employee()
    emp.set_data(1,'ramy','male','hyderabad',55000)
    emp.display_employee_data()
    emp.set_data(1,'ramy','male','hyderabad',70000)
    emp.display_employee_data()
    emp1 = employee()
    emp1.set_data(2,'reddy','male','hyderabad',66000)
    emp1.display_employee_data()
   

if __name__=='__main__':
    print(__doc__)
    main_function()
	