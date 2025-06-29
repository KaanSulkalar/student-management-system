from datetime import datetime
import json

class Student:
    def __init__(self, student_num, first_name, last_name, date_of_birth, sex, country):
        self.__student_num = student_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__sex = sex
        self.__country = country
        
    ## Getter methods
    
    def get_student_num(self):
        return self.__student_num
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_date_of_birth(self):
        return self.__date_of_birth
    
    def get_sex(self):
        return self.__sex
    
    def get_country(self):
        return self.__country
    
    #additional info no need 
    def get_age(self):
        birth_year = int(self.__date_of_birth.split('/')[0])
        current_year = datetime.now().year
        return current_year - birth_year
    
    ## Setter methods
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth
    
    def set_sex(self, sex):
        self.__sex = sex
    
    def set_country(self, country):
        self.__country = country
    
    def to_dictionary(self):
        return {
            "Student_Number": self.__student_num,
            "First_Name": self.__first_name,
            "Last_Name": self.__last_name,
            "Date_of_Birth": self.__date_of_birth,
            "Sex": self.__sex,
            "Country": self.__country
        }   
        
    @staticmethod
    def from_dictionary(data):
        return Student(
            data["Student_Number"], data["First_Name"], data["Last_Name"],
            data["Date_of_Birth"], data["Sex"], data["Country"]
        )
        
    def __str__(self):
        return(f"Student Number: {self.__student_num}, Student Name and Surname: {self.__first_name} {self.__last_name}, "
               f"Date of Birth: {self.__date_of_birth}, Sex: {self.__sex}, Country: {self.__country}" )
        
##-----------------------------------------------------------------------------------------------------------------------------##

class StudentManager:
    def __init__(self):
        self.allStudents = []
        
    def add_student(self, student):
        if len(self.allStudents) < 100:
            self.allStudents.append(student)
        else:
            print("Maximum student capacity reached you can not add more students.")
            
    def find_student(self, student_number):
        for student in self.allStudents:
            if student.get_student_num() == student_number:
                return student
        return None
        
    def show_all_students(self):
        for student in self.allStudents:
            print(student)
            
    def show_students_by_year(self, year):
        found = False
        for student in self.allStudents:
            if student.get_date_of_birth().startswith(str(year)):
                print(student)
                found = True
        if not found:
            print(f"No students have found bor in that year. ({year})")
            
    def modify_student(self, student_number):
        student = self.find_student(student_number)
        if student:
            print("Chose a option to modify.")
            print("1) First Name\n2) Last Name\n3) Date of Birth\n4) Sex\n5) Country")
            entered_choice = input("Please enter a choise: ")
            new_value = input("Enter a new value: ")
            
            if entered_choice == "1":
                student.set_first_name(new_value)
            elif entered_choice == "2":
                student.set_last_name(new_value)
            elif entered_choice == "3":
                student.set_date_of_birth(new_value)
            elif entered_choice == "4": 
                student.set_sex(new_value)
            elif entered_choice == "5":
                student.set_country(new_value)
            else:
                print("Wrong option is chosen.")
        else:
            print("Student not found, exiting program.")
            exit(0)
        
    def delete_student(self, student_number):
        for i, student in enumerate(self.allStudents):
            if student.get_student_num() == student_number:
                del self.allStudents[i]
                print("Student deleted.") 
                return 
        print("Student not found.")
            
    def save_to_file(self, fileName="students.json"):
        with open(fileName, "w") as file:
            json.dump([student.to_dictionary() for student in self.allStudents], file)
        print("Data is saved...")
    
    def load_from_file(self, fileName="students.json"):
        try:
            with open(fileName, "r") as file:
                data = json.load(file)
                self.allStudents = [Student.from_dictionary(d) for d in data]
            print("Data loaded from the file")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error ocured while reading file.")

##-----------------------------------------------------------------------------------------------------------------------------##

def main():
    manager = StudentManager()
    
    while True:
        print("\n Student Management System DEMO")
        print("1) Add a new student")
        print("2) Find a student by student number")
        print("3) Show all students")
        print("4) Show all students born in a given year")
        print("5) Modify a student info")
        print("6) Delete a student by student number")
        print("7) Save student file")
        print("8) Load student from file")
        print("9) Quit program")
        
        entered_choice = input("Enter your option: ")
        
        if entered_choice == "1": 
            student_num = input("Enter student number: ")
            first_name = input("Enter student name: ")
            last_name = input("Enter student surname: ")
            date_of_birth = input("Enter date of birth: ")
            sex = input("Enter sex: ")
            country = input("Enter country: ")
            
            student = Student(student_num, first_name, last_name, date_of_birth, sex, country)
            manager.add_student(student)
            
        elif entered_choice == "2":
            student_num = input("Enter student number: ")
            student = manager.find_student(student_num)
            if student:
                print(student)
            else:
                print("Student not found.")
                
        elif entered_choice == "3":
            manager.show_all_students()
            
        elif entered_choice == "4":
            year = input("Enter year: ")
            manager.show_students_by_year(year)
            
        elif entered_choice == "5":
            student_num = input("Enter student number: ")
            manager.modify_student(student_num)
            
        elif entered_choice == "6":
            student_num = input("Enter student number you want to delete: ")
            manager.delete_student(student_num)
            
        elif entered_choice == "7":
            manager.save_to_file()
            
        elif entered_choice == "8":
            manager.load_from_file()
            
        elif entered_choice == "9":
            print("Exiting program...")
            break
        
        else: 
            print("Invalid option please enter a valid option to proceed.")
                
if __name__ == "__main__":
    main()
