
import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            gender = gender_combobox.get()
            
            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("Gender:", gender)
            print("------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()               # create a window 
window.title("Applicaition Form")   # title of the window

frame = tkinter.Frame(window)       # creating a parent frame for the application 
frame.pack()                        #to show our application window and clear 

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="User Information") # create frame for user 
user_info_frame.grid(row= 0, column=0, padx=20, pady=10) #make the user info in a grid form 


first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)   # assign position to first name label
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)  # assign position to last name 

first_name_entry = tkinter.Entry(user_info_frame)  # enter my first name 
last_name_entry = tkinter.Entry(user_info_frame)   # enter my last name 
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")  # create a title lable
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."]) # use combobox to assigned title drop down 
title_label.grid(row=0, column=2) # assign position 
title_combobox.grid(row=1, column=2) # assign position 

age_label = tkinter.Label(user_info_frame, text="Age") # create an age label 
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110) # use spinbox to assigned number range from to
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality") # create a nationality label 
nationality_combobox = ttk.Combobox(user_info_frame, values=["Indian", "Pakistani", "Bangladeshi", "British", "American"]) # use combox to assigned country drop down 
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

gender_label = tkinter.Label(user_info_frame, text="Gender") # create gender title 
gender_combobox = ttk.Combobox(user_info_frame, values=["", "Male", "Female", "Other"]) # use combobox for drop down for sex 
gender_label.grid(row=2, column=2)
gender_combobox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children(): # use widget to create more space within the app titles 
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10) # sticky will allign to the left 

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text= "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop() # it will call all the tkinter window when u call it 