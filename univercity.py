import tkinter as tk
from tkinter import messagebox

courses = [
    ("Math", "mr.ahmadi"),
    ("Physics", "mr. ramini"),
    ("Chemistry", "mr. kamaly"),
    ("Biology", "mr. vafaii"),
    ("Computer Science", "mr. rahimi"),
    ("History", "mr. lemiy"),
    ("Philosophy", "mr. hamidi"),
    ("Literature", "mr. mosavi"),
    ("Art", "mr. karimi"),
    ("Economics", "mr. moradi")
]

selected_courses = []

def open_selection_page():
    def add_course():
        selected_courses.clear()
        for var, course in zip(course_vars, courses):
            if var.get():
                selected_courses.append(course[0])

        if len(selected_courses) > 4:
            messagebox.showerror("Error", "You can select up to 4 courses only.")
            selected_courses.clear()
        else:
            open_info_page()

    root = tk.Tk()
    root.title("Course Selection")

    tk.Label(root, text="Select up to 4 courses:").pack()

    course_vars = []
    for course, professor in courses:
        var = tk.IntVar()
        tk.Radiobutton(root, text=f"{course} - {professor}", variable=var, value=1).pack(anchor="w")
        course_vars.append(var)

    tk.Button(root, text="Next", command=add_course).pack()

    root.mainloop()

def open_info_page():
    def submit_info():
        national_code = national_code_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        residence = residence_entry.get()

        if not national_code.isdigit() or len(national_code) != 10:
            messagebox.showerror("Error", "National code must be exactly 10 digits.")
            return

        if not first_name.isalpha():
            messagebox.showerror("Error", "First name must contain only letters.")
            return

        if not last_name.isalpha():
            messagebox.showerror("Error", "Last name must contain only letters.")
            return

        messagebox.showinfo("Success", f"Course selection completed!\n\nSelected Courses: {', '.join(selected_courses)}\nName: {first_name} {last_name}\nNational Code: {national_code}\nResidence: {residence}")
        root.destroy()

    root = tk.Tk()
    root.title("User Information")

    tk.Label(root, text="Enter your information:").pack()

    tk.Label(root, text="National Code:").pack()
    national_code_entry = tk.Entry(root)
    national_code_entry.pack()

    tk.Label(root, text="First Name:").pack()
    first_name_entry = tk.Entry(root)
    first_name_entry.pack()

    tk.Label(root, text="Last Name:").pack()
    last_name_entry = tk.Entry(root)
    last_name_entry.pack()

    tk.Label(root, text="Place of Residence:").pack()
    residence_entry = tk.Entry(root)
    residence_entry.pack()

    tk.Button(root, text="Submit", command=submit_info).pack()

    root.mainloop()

open_selection_page()