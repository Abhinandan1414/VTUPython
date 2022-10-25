# employee class code in Python
# class definition
class employee:
    def __init__(self):
        __id = 0
        __name = ""
        __gender = ""
        __city = ""
        __salary = 0

	
	# function to set data 
    def set_data(self, id=0, name=" ",gender = "", city = "", salary =0):
        self.__id=id
        self.__name = name
        self.__gender = gender
        self.__city = city
        self.__salary = salary
	
	# function to get/print data
    def display_employee_data(self):
        print("--------------------------")
        print("Id\t:",self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)
        print("--------------------------")

# main function definition
def main_function():
    #Employee Object
    emp=employee()
    emp.set_data(1,'ramy','male','hyderabad',55000)
    emp.display_employee_data()
    emp1 = employee()
    emp1.set_data(2,'reddy','male','hyderabad',66000)
    emp1.display_employee_data()

main_function()
	