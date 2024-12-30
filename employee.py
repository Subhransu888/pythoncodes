employees={}
def add_employee(emp_dict):
    empid=input("enter employee id: ")
    if empid in emp_dict:
        print("employee id already exists")
    else:
        name=input("enter employee name: ")
        emp_dict[empid]=name
        print("employee added succesfully")
def delete_employee(emp_dict):
    empid=input("enter employee id of the employee you want to remove: ")
    if empid not in emp_dict:
        print("employee not found")
    else:
        del emp_dict[empid]
        print("employee deleted sucessfully")
def traverse(emp_dict):
    if not emp_dict:
        print("no employee in system")
    else:
        print("employee details: ")
        for empid, name in emp_dict.items():
            print(f"employee id: {empid}, name: {name}")
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Traverse Employees")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_employee(employees)
    elif choice == "2":
        delete_employee(employees)
    elif choice == "3":
        traverse(employees)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please select a valid option.")