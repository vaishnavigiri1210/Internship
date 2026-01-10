''' 
main file for EduTrack application 
(Frontend i.e. handles GUI using tkinter for adding student and viewing analytics dashboard)
'''

import tkinter as tk
from tkinter import messagebox
import logic

students = logic.load_students()

def add_student():
    """
    Add student after validating input.
    """
    try:
        name = name_entry.get()     # entry.get() used for user input
        marks = {
            "Maths": int(maths_entry.get()),
            "Science": int(science_entry.get()),
            "English": int(english_entry.get())
        }

        if any(m < 0 or m > 100 for m in marks.values()):       
            raise ValueError

        logic.save_student(name, marks)
        messagebox.showinfo("Success", "Student added successfully")
    except ValueError:
        messagebox.showerror("Error", "Invalid marks entered")


def show_dashboard():
    """
    Display analytics dashboard.
    """
    students = logic.load_students()
    if not students:
        messagebox.showwarning("Warning", "No student data available")
        return

    avg = logic.class_average(students)
    top = logic.topper(students)

    messagebox.showinfo(
        "Dashboard",
        f"Total Students: {len(students)}\n"       # f means “put value inside the string”
        f"Class Average: {avg:.2f}%\n"              # :.2f means 2 decimal places
        f"Topper: {top.name} ({top.average():.2f}%)"        # {} used to insert variables
    )


def show_weak():
    """
    Show students scoring below 40%.
    """
    students = logic.load_students()
    weak = logic.weak_students(students)    # weak is a list of names
    messagebox.showinfo("Weak Students", "\n".join(weak) if weak else "No weak students") 
    # .join() joins list elements with newline


# GUI Window
root = tk.Tk()
root.title("EduTrack - Student Analytics")
root.geometry("400x400")

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)     # Entry widget for user input
name_entry.pack()               # Pack method to add widget to window

tk.Label(root, text="Maths Marks").pack()
maths_entry = tk.Entry(root)
maths_entry.pack()

tk.Label(root, text="Science Marks").pack()
science_entry = tk.Entry(root)
science_entry.pack()

tk.Label(root, text="English Marks").pack()
english_entry = tk.Entry(root)
english_entry.pack()

''' add_student button using command to link function to button and
.pack used to add button to window also pady for padding i.e space '''

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Dashboard", command=show_dashboard).pack(pady=5)
tk.Button(root, text="Below 40%", command=show_weak).pack(pady=5)

root.mainloop()
