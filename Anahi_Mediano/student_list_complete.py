# Initial list of students
student= ["Pamela Gonzales", "Quebec Martinez", "Alheli Coss", "Rogelio Rodriguez", "Dania Garcia", "Manfred Salas", "Nicolas Parodi", "Sam Pastor", "Anahi Mediano", "Gael Martinez"]

def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    for names in student:
        print(names)
    print(f"_____________________________________") 
# Add a new student to the list
def add_student():
    student.append(input("Add a new student: "))
    print(f'{student}')
    display_students()
# Remove a student from the list by name
def remove_student():
    name= input ("Student to remove: ")
    if name in student:
        student.remove(remove_student)
    else:
        print("Name not found")
        
    display_students()
# remove a student from the end of the list
def pop_student():
    if student is not "":
        pop_name= student [-1]
        student.pop()
        print(f"student removed {pop_name}")
        display_students()
    else:
        print("Error this list is empty")
        display_students()
    display_students()

# Update a student's name in the list
def update_student():
    previous_name= input("Previous name of the student: ")
    new_name = input("What name do you want to update: ")
    find_name= student.index(previous_name)
    student[find_name] = new_name
    if not new_name:
        print("This name doesn´t exist")
    else:
        print("This name exist")
    display_students()

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            pop_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            exit()
            break
            
menu()