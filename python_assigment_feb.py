#1. Create an empty list and ask the user to enter only int and float elements.
numbers = []
for i in range(5):  
    value = input(f"Enter a number ({i+1}/5): ")
    
    try:
        value = float(value)  
    except ValueError:
        print("Invalid input! Please enter only integers or floats.")

print("Final List:", numbers)


#2. Create an empty dictionary d1 and ask the user to enter values using a loop.
d1 = {}
n = int(input("Enter how many key-value pairs you want to add: "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value {i+1}: ")
    d1[key] = value 

print("Final Dictionary:", d1)


#3. Create an empty dictionary d1 and ask the user to enter values using dictionary comprehension.
n = int(input("Enter how many key-value pairs you want to add: "))
d1 = {input(f"Enter key {i+1}: "): input(f"Enter value {i+1}: ") for i in range(n)}

print("Final Dictionary:", d1)


#4. Function that accepts two int or float parameters and returns a tuple of 4 arithmetic operations.
def arithmetic_operations(a, b):
    """Performs addition, subtraction, multiplication, and division on two numbers."""
    if (isinstance(a, (int, float))) and (isinstance(b, (int, float))):
        add = a + b
        sub = a - b
        mul = a * b
        div = a / b if b != 0 else "Cannot divide by zero"
        return (add, sub, mul, div)
    else:
        return "Error: Please enter only numbers!"
# Example 
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print(arithmetic_operations(x, y))


#5. Modify the above function to divide the multiplication result by 2.
def modified_multiplication(a, b):
    """Returns arithmetic operations but divides the multiplication result by 2."""
    if (isinstance(a, (int, float))) and (isinstance(b, (int, float))):
        add = a + b
        sub = a - b
        mul = (a * b) / 2  
        div = a / b if b != 0 else "Cannot divide by zero"
        return (add, sub, mul, div)
    else:
        return "Error: Please enter only numbers!"
# Example 
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print(modified_multiplication(x, y))


#6. Function to add only string elements to a list.
def add_strings():
    """Takes user input and adds only string elements to the list."""
    string_list = []
    
    for i in range(5): 
        value = input(f"Enter a string ({i+1}/5): ")
        
        if value.isdigit() or value.replace(".", "").isdigit():
            print("Invalid input! Please enter only strings.")
        else:
            string_list.append(value)
    
    return string_list
# Example 
final_list = add_strings()
print("Final String List:", final_list)


#7. Function to read a file and return a dictionary of total lines and total words
def file_stats(file_path):
    """Reads a file and returns a dictionary with total lines and total words."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            total_lines = len(lines)
            total_words = sum(len(line.split()) for line in lines)
            
        return {"Total Lines": total_lines, "Total Words": total_words}
    
    except FileNotFoundError:
        return "Error: File not found!"
    except Exception as e:
        return f"Error: {str(e)}"

# Example
file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\PYTHON_ASSIGN\small_size\VAISHNAVIII ASSIGNMENT PYTHONNNNNN.txt"
print(file_stats(file_path))


#8. Function to display dictionary keys and values on separate lines
def display_dict(d):
    """Displays dictionary keys and values on separate lines."""
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")
# Example 
sample_dict = {"Name": "John", "Age": 25, "City": "Pune"}
display_dict(sample_dict)


#9. Lambda function to display dictionary keys and values on separate lines
display_lambda = lambda d: [print(f"Key: {k}, Value: {v}") for k, v in d.items()]
# Example
sample_dict = {"Name": "John", "Age": 25, "City": "Pune"}
display_lambda(sample_dict)


#10. Function to validate a password
import re

def validate_password(password):
    """Checks if password contains at least one lowercase, one uppercase, one number, and one special character (except comma and quotes)."""
    if (re.search(r"[a-z]", password) and  
        re.search(r"[A-Z]", password) and  
        re.search(r"[0-9]", password) and  
        re.search(r"[!@#$%^&*()_+]", password) 
        not re.search(r"[,'\"]", password)):  
        return "Valid Password"
    else:
        return "Invalid Password! Follow the rules."
# Example 
password = input("Enter password: ")
print(validate_password(password))


#11. Decorator to accept only natural numbers (for factorial function)
def natural_number_check(func):
    """Decorator to allow only natural numbers (1 and above) for factorial calculation."""
    def wrapper(n):
        if isinstance(n, int) and n > 0:
            return func(n)
        else:
            return "Error: Only natural numbers are allowed!"
    return wrapper

@natural_number_check
def factorial(n):
    """Calculates factorial recursively."""
    return 1 if n == 1 else n * factorial(n - 1)

# Example 
num = int(input("Enter a natural number: "))
print(factorial(num))


#12. Decorator to check if current time is between 7 AM and 7 PM
from datetime import datetime

def time_restrict(func):
    """Decorator to allow function execution only between 7 AM and 7 PM."""
    def wrapper(*args, **kwargs):
        current_hour = datetime.now().hour
        if 7 <= current_hour < 19:
            return func(*args, **kwargs)
        else:
            return "Error: Garden is open only from 7 AM to 7 PM!"
    return wrapper

# a. Function payment_check()
@time_restrict
def payment_check():
    """Checks user transactions in the given month."""
    return "Payment details are being processed."

# b. Function entry()
@time_restrict
def entry():
    """Performs user entry transaction."""
    return "Entry transaction completed."

# c. Function exit()
@time_restrict
def exit():
    """Updates out-time of the user if entry exists."""
    return "Exit time updated successfully."

# Example-
print(payment_check())
print(entry())
print(exit())


#13. Lambda function for sorting a string
sort_string = lambda s: "".join(sorted(s))

# Example
string = input("Enter a string to sort: ")
print(sort_string(string))

#14. Generator to generate unique values like ABC0001, ABC0002, etc.
def unique_code_generator():
    """Generates runtime unique values in the format ABC0001, ABC0002, etc."""
    num = 1
    while True:
        yield f"ABC{num:04d}"
        num += 1

# Example 
gen = unique_code_generator()
for _ in range(5):  
    print(next(gen))

#15. Decorator to check if input is alphanumeric and validate PAN details
import re

def validate_pan(func):
    """Decorator to check if input values are alphanumeric and PAN format is correct."""
    def wrapper(*args, **kwargs):
        for arg in args:
            if not arg.isalnum():
                return "Error: Input should be alphanumeric!"
            
        pan_pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
        if re.match(pan_pattern, args[0]):
            return func(*args, **kwargs)
        else:
            return "Error: Invalid PAN format!"
    return wrapper

@validate_pan
def check_pan_details(pan):
    """Returns valid PAN message if PAN format is correct."""
    return f"PAN {pan} is valid."

# Example
pan_number = input("Enter PAN number: ")
print(check_pan_details(pan_number))

#16. Function to perform all arithmetic operations
def arithmetic_operations(a, b):
    """Performs addition, subtraction, multiplication, division, and modulus."""
    try:
        a, b = float(a), float(b)
        return a + b, a - b, a * b, a / b if b != 0 else "Cannot divide by zero", a % b if b != 0 else "Cannot find modulus by zero"
    except ValueError:
        return "Error: Only numeric inputs are allowed!"

# Example 
x, y = input("Enter two numbers separated by space: ").split()
print(arithmetic_operations(x, y))


#17. Validate user inputs and store in a text file
import re

def validate_name(name):
    """Validates name to ensure it contains only letters and spaces."""
    if re.match(r"^[A-Za-z\s]+$", name):
        return True
    return False

def validate_marks(marks):
    """Validates marks to be a number between 0 and 100."""
    try:
        marks = float(marks)
        return 0 <= marks <= 100
    except ValueError:
        return False

def validate_mobile(mobile):
    """Validates mobile number to be exactly 10 digits."""
    return bool(re.match(r"^\d{10}$", mobile))

def save_to_file(data):
    """Saves dictionary to a text file."""
    with open("user_data.txt", "a") as file:
        file.write(str(data) + "\n")

def main():
    """Main function to take inputs and validate them."""
    user_data = {}

    name = input("Enter your name: ")
    if not validate_name(name):
        print("Error: Invalid name format. Special characters not allowed.")
        return
    user_data["Name"] = name

    marks = input("Enter your marks: ")
    if not validate_marks(marks):
        print("Error: Invalid marks format.")
        return
    user_data["Marks"] = marks

    mobile = input("Enter your mobile number: ")
    if not validate_mobile(mobile):
        print("Error: Invalid mobile number.")
        return
    user_data["Mobile"] = mobile

    save_to_file(user_data)
    print("User data saved successfully.")

# Run the program
main()


#18. Segregate files into small, medium, and large folders based on size
import os

def categorize_files(folder_path):
    """Categorizes files in the given folder based on their extensions."""
    try:
        if not os.path.exists(folder_path):
            return "Error: Folder not found!"
        
        files = os.listdir(folder_path)
        file_categories = {}

        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[-1].lower()
                if ext not in file_categories:
                    file_categories[ext] = []
                file_categories[ext].append(file)

        return file_categories

    except Exception as e:
        return f"Error: {str(e)}"

# Example 
folder_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\PYTHON_ASSIGN"
print(categorize_files(folder_path))


#19. In the hotel user is entering the details of menu, quantity and printing the bill. number of menu may varies with customer's order. generate a file having grocery bill as per the below formatNote: User may enter n entities and total will be calculated adding the GST of 10% separately.
import datetime

def generate_bill():
    items = []
    total = 0

    while True:
        menu = input("Enter item name (or 'done' to finish): ")
        if menu.lower() == "done":
            break
        try:
            qty = int(input("Enter quantity: "))
            price = int(input("Enter price per item: "))
            items.append((menu, qty, price))
            total += qty * price
        except ValueError:
            print("Please enter valid numbers for quantity and price.")

    gst = round(total * 0.10)
    grand_total = total + gst

    with open("hotel_bill.txt", "w") as file:
        file.write(f"Welcome Hotel Name\nDate: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
        file.write("--------------------------------------------------\n")
        file.write("Menu\tQty\tPrice\n")
        for menu, qty, price in items:
            file.write(f"{menu}\t{qty}\t{price * qty}\n")
        file.write("--------------------------------------------------\n")
        file.write(f"Total: {total}\nGST 10%: {gst}\nGrand Total: {grand_total}\n")

    print("Bill generated successfully!")

generate_bill()

#20. Check which word has the most repetition in a file
def most_repeated_word(file_path):
    """Finds the most repeated word in the given file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().split()
        
        word_count = {}
        for word in words:
            word = word.lower().strip(".,!?()[]{}\"'") 
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        
        most_common = max(word_count, key=word_count.get) 
        return most_common, word_count[most_common]

    except FileNotFoundError:
        return "Error: File not found!"
    except Exception as e:
        return f"Error: {str(e)}"

# Example -
file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\PYTHON_ASSIGN\small_size\VAISHNAVIII ASSIGNMENT PYTHONNNNNN.txt"
print(most_repeated_word(file_path))


#21. Function to count occurrences of a word in a file
def word_occurrences(word, file_path):
    """Returns a dictionary with the word and its occurrences in the file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().lower()
        
        count = text.split().count(word.lower())  
        return {word: count}

    except FileNotFoundError:
        return "Error: File not found!"
    except Exception as e:
        return f"Error: {str(e)}"
#EXAMPLE -
file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\PYTHON_ASSIGN\small_size\VAISHNAVIII ASSIGNMENT PYTHONNNNNN.txt"
word = "python"
print(word_occurrences(word, file_path))


#22. Function to return all word occurrences
def all_word_occurrences(file_path):
    """Returns a dictionary of all words and their occurrences in the file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().split()
        
        word_count = {}
        for word in words:
            word = word.lower().strip(".,!?()[]{}\"'") 
            if word:
                word_count[word] = word_count.get(word, 0) + 1

        return word_count

    except FileNotFoundError:
        return "Error: File not found!"
    except Exception as e:
        return f"Error: {str(e)}"

# Example 
file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\PYTHON_ASSIGN\small_size\VAISHNAVIII ASSIGNMENT PYTHONNNNNN.txt"
print(all_word_occurrences(file_path))


#23. Class based on Question 8 logic
class WordCounter:
    def __init__(self, filepath):
        self.filepath = filepath

    def count_words(self):
        try:
            with open(self.filepath, "r") as file:
                words = file.read().split()
                word_count = {}
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
                return word_count
        except FileNotFoundError:
            return {"Error": "File not found"}

filepath = input("Enter file path: ")
counter = WordCounter(filepath)
print(counter.count_words())

#24. Find most repetitive word in all text files in a folder
import os

def most_repeated_word_in_folder(folder_path):
    """Finds the most repeated word across all text files in a folder."""
    word_count = {}

    try:
        if not os.path.exists(folder_path):
            return "Error: Folder not found!"

        for file in os.listdir(folder_path):
            if file.endswith(".txt"):  
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    words = f.read().split()

                for word in words:
                    word = word.lower().strip(".,!?()[]{}\"'")
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
        
        most_common = max(word_count, key=word_count.get)
        return most_common, word_count[most_common]

    except Exception as e:
        return f"Error: {str(e)}"

# Example
folder_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\PYTHON_ASSIGN"
print(most_repeated_word_in_folder(folder_path))

#25. Class for file reading
class FileReader:
    """Class to handle file reading and word processing."""

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Reads the file content and returns as a string."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return "Error: File not found!"
        except Exception as e:
            return f"Error: {str(e)}"

    def word_count(self):
        """Returns a dictionary with word occurrences."""
        try:
            text = self.read_file()
            if "Error" in text:
                return text  # Return error if file reading fails

            words = text.split()
            word_count = {}

            for word in words:
                word = word.lower().strip(".,!?()[]{}\"'")  # Clean punctuation
                if word:
                    word_count[word] = word_count.get(word, 0) + 1

            return word_count
        except Exception as e:
            return f"Error: {str(e)}"

# Example-
file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\PYTHON_ASSIGN\small_size\VAISHNAVIII ASSIGNMENT PYTHONNNNNN.txt"
reader = FileReader(file_path)
print(reader.word_count())


#26. Function to return keys with integer/float values
def filter_numeric_keys(data):
    return {key: value for key, value in data.items() if isinstance(value, (int, float))}

data = {"name": "John", "age": 25, "height": 5.9, "city": "Pune"}
print(filter_numeric_keys(data))

#27. Decorator for error handling
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Custom Error: {e}"
    return wrapper

@error_handler
def validate_name(name):
    if not name.isalpha():
        raise ValueError("Invalid name format!")
    return f"Valid name: {name}"

name = input("Enter your name: ")
print(validate_name(name))

#28. User class that checks keys in a dictionary
class User:
    def __init__(self, data):
        required_keys = ["name", "age", "email"]
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Missing key: {key}")
        self.name = data["name"]
        self.age = data["age"]
        self.email = data["email"]

    def display(self):
        return f"User: {self.name}, Age: {self.age}, Email: {self.email}"

user_data = {"name": "Alice", "age": 22, "email": "alice@example.com"}
try:
    user = User(user_data)
    print(user.display())
except KeyError as e:
    print(e)

#29. Class Pharma for medicine entry and billing
class Pharma:
    def __init__(self):
        self.medicines = {}

    def add_medicine(self, name, price):
        self.medicines[name] = price

    def generate_bill(self, items):
        total = sum(self.medicines[item] * qty for item, qty in items.items() if item in self.medicines)
        return f"Total Bill: {total} (Including GST 10%: {total * 0.10})"

# User A - Adding medicines
pharma_store = Pharma()
pharma_store.add_medicine("Paracetamol", 50)
pharma_store.add_medicine("Ibuprofen", 80)

# User B - Generating bill
customer_cart = {"Paracetamol": 2, "Ibuprofen": 1}
print(pharma_store.generate_bill(customer_cart))

#30. Read file and return dictionary with number positions
def extract_numbers_from_file(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read().split()
            number_dict = {index: int(value) for index, value in enumerate(content) if value.isdigit()}
            return number_dict
    except FileNotFoundError:
        return {"Error": "File not found"}

filepath = input("Enter file path: ")
print(extract_numbers_from_file(filepath))

#31. Class for file reading and storing numbers in user-specific dictionary
class FileProcessor:
    def __init__(self, user):
        self.user = user
        self.data = {}

    def read_numbers(self, filepath):
        try:
            with open(filepath, "r") as file:
                content = file.read().split()
                self.data[self.user] = {index: int(value) for index, value in enumerate(content) if value.isdigit()}
        except FileNotFoundError:
            self.data[self.user] = {"Error": "File not found"}

    def get_data(self):
        return self.data

# Example 
user1 = FileProcessor("UserA")
user1.read_numbers("sample.txt")
print(user1.get_data())

#32. Hotel Booking Portal
import random

class HotelBooking:
    def __init__(self):
        self.bookings = {}

    def book_room(self, name, pan, mobile):
        confirmation_no = random.randint(1000, 9999)
        self.bookings[confirmation_no] = {"Name": name, "PAN": pan, "Mobile": mobile}
        return f"Booking Confirmed! Your confirmation number is {confirmation_no}"

hotel = HotelBooking()
name = input("Enter Name: ")
pan = input("Enter PAN Card Number: ")
mobile = input("Enter Mobile Number: ")
print(hotel.book_room(name, pan, mobile))

#33. User Superclass with Student, Professor & Admin
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        return f"{self.username} registered successfully!"

    def sign_in(self):
        return f"{self.username} signed in!"

    def sign_out(self):
        return f"{self.username} signed out!"

class Student(User):
    def view_marks(self, result_date, marks):
        return marks if result_date else "Results not available yet."

class Professor(User):
    def enter_marks(self, student_marks):
        return student_marks

class Admin(User):
    def view_marks(self, marks):
        return marks

# Example 
prof = Professor("ProfJohn", "pass123")
print(prof.enter_marks({"Student1": 85, "Student2": 90}))

student = Student("StudentA", "stud123")
print(student.view_marks(False, {"Math": 80}))  # Results not available yet

#34. Resume Exchange Portal
class ResumePortal:
    def __init__(self):
        self.resumes = {}

    def upload_resume(self, employee, file_path):
        """Uploads the resume for an employee."""
        self.resumes[employee] = file_path
        return f"Resume uploaded for {employee}."

    def view_resumes(self):
        """Returns all uploaded resumes."""
        return self.resumes if self.resumes else "No resumes available."

# Example
portal = ResumePortal()
resume_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\Resumes\resume_john.pdf"
print(portal.upload_resume("John Doe", resume_path))
print(portal.view_resumes())



#35. Employee Database Management
import pyodbc 
class EmployeeDB:
    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=VAISHNAVI;"
            "DATABASE=EmployeeDB;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            "IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='employees' AND xtype='U') "
            "CREATE TABLE employees ("
            "id INT IDENTITY(1,1) PRIMARY KEY, "
            "name NVARCHAR(100), "
            "mobile NVARCHAR(15), "
            "address NVARCHAR(255))"
        )

        self.cursor.execute(
            "IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='leave_requests' AND xtype='U') "
            "CREATE TABLE leave_requests ("
            "id INT IDENTITY(1,1) PRIMARY KEY, "
            "name NVARCHAR(100), "
            "leave_days INT, "
            "status NVARCHAR(20))"
        )

        self.conn.commit()

    def add_employee(self, name, mobile, address):
        self.cursor.execute("INSERT INTO employees (name, mobile, address) VALUES (?, ?, ?)", (name, mobile, address))
        self.conn.commit()
        return "Employee added successfully!"

    def apply_leave(self, name, days):
        self.cursor.execute("INSERT INTO leave_requests (name, leave_days, status) VALUES (?, ?, 'Pending')", (name, days))
        self.conn.commit()
        return "Leave applied!"

    def approve_leave(self, name):
        self.cursor.execute("UPDATE leave_requests SET status = 'Approved' WHERE name = ?", (name,))
        self.conn.commit()
        return "Leave Approved!"

db = EmployeeDB()
print(db.add_employee("Alice", "9876543210", "New York"))
print(db.apply_leave("Alice", 5))
print(db.approve_leave("Alice"))
