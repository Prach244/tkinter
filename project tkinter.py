import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="udemy_courses"
)
mycursor = mydb.cursor()

# Function to add a new course to the database
def add_course():
    course_name = course_name_entry.get()
    instructor = instructor_entry.get()
    price = price_entry.get()

    sql = "INSERT INTO courses (course_name, instructor, price) VALUES (%s, %s, %s)"
    val = (course_name, instructor, price)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Course added successfully!")

# Function to view all courses
def view_courses():
    mycursor.execute("SELECT * FROM courses")
    courses = mycursor.fetchall()
    for course in courses:
        print(course)

# Function to add a new student
def add_student():
    student_name = student_name_entry.get()
    email = email_entry.get()

    sql = "INSERT INTO students (student_name, email) VALUES (%s, %s)"
    val = (student_name, email)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Student added successfully!")

# Function to enroll a student in a course
def enroll_student():
    student_id = int(student_id_entry.get())
    course_id = int(course_id_entry.get())

    sql = "INSERT INTO student_courses (student_id, course_id) VALUES (%s, %s)"
    val = (student_id, course_id)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Student enrolled in course!")

# Create GUI
root = tk.Tk()
root.title("Udemy Course and Student Management")

# Labels and Entry fields for courses
tk.Label(root, text="Course Name:").grid(row=0, column=0)
tk.Label(root, text="Instructor:").grid(row=1, column=0)
tk.Label(root, text="Price:").grid(row=2, column=0)
course_name_entry = tk.Entry(root)
course_name_entry.grid(row=0, column=1)
instructor_entry = tk.Entry(root)
instructor_entry.grid(row=1, column=1)
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1)

# Labels and Entry fields for students
tk.Label(root, text="Student Name:").grid(row=3, column=0)
tk.Label(root, text="Email:").grid(row=4, column=0)
student_name_entry = tk.Entry(root)
student_name_entry.grid(row=3, column=1)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1)

# Labels and Entry fields for enrolling students
tk.Label(root, text="Student ID:").grid(row=5, column=0)
tk.Label(root, text="Course ID:").grid(row=5, column=2)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=5, column=1)
course_id_entry = tk.Entry(root)
course_id_entry.grid(row=5, column=3)

# Buttons for course management
add_course_button = tk.Button(root, text="Add Course", command=add_course)
add_course_button.grid(row=6, column=0, pady=10)
view_courses_button = tk.Button(root, text="View Courses", command=view_courses)
view_courses_button.grid(row=6, column=1, pady=10)

# Buttons for student management
add_student_button = tk.Button(root, text="Add Student", command=add_student)
add_student_button.grid(row=7, column=0, pady=10)
enroll_student_button = tk.Button(root, text="Enroll Student", command=enroll_student)
enroll_student_button.grid(row=7, column=1, pady=10)

root.mainloop()
