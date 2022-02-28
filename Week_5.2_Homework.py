# Calendar GUI That Can Select Date
# I was inspired by two Python projects, so I made both as one whole project!
# I made changes and added new code as I went along.
# https://towardsdatascience.com/develop-your-own-calendar-to-track-important-dates-with-python-c1af9e98ffc3#
# https://www.geeksforgeeks.org/python-gui-calendar-using-tkinter/


# Libraries that I downloaded and used for this project
from tkinter import *
from tkcalendar import Calendar


# This function shows the calendar of the given month, day, and year
# I added a 'def' function to define 'showCal' as the GUI calendar
def showCal():
    # This function creates the gui object pop-up
    tk = Tk()

    # Set the background colour of GUI window of the calendar
    # I changed the color of the background of the calendar
    tk.config(background="Pink")

    # set the name of tkinter GUI window of the calendar
    # I added a title to the calendar GUI window
    tk.title("Calendar")

    # This function sets the geometry of the calendar gui interface
    # I changed the sizing of the calendar
    tk.geometry("700x700")

    # These three functions get the year, day, and month text as string
    # I added these three functions to be able to make the year, day, and month as integers
    # These three functions also help me stay organized by adding them to the 'calendar = Calendar(tk, ...' down below
    fetch_year = int(year_field.get())

    fetch_day = int(day_field.get())

    fetch_month = int(month_field.get())

    # This function adds the calendar module
    # I changed the code to be able to get the date that the user inputs in the date submissions GUI window
    calendar = Calendar(tk, selectmode='day',
                        year=fetch_year, month=fetch_month,
                        day=fetch_day)

    calendar.pack(pady=20, fill="both", expand=True)

    # This function grabs the selected date in the calendar gui interface
    def grad_date():
        date.config(text="Selected Date is " + calendar.get_date())

    # The function below adds the buttons and labels
    Button(tk, text="Get Date",
           command=grad_date).pack(pady=20)

    date = Label(tk, text="")
    date.pack(pady=20)

    # Execute Tkinter
    tk.mainloop()


# Driver Code
if __name__ == "__main__":
    # This function creates the date submissions GUI window
    gui = Tk()

    # This function sets the background color of the date submissions GUI window
    # Changed the color because I like pink
    gui.config(background="pink")

    # This function sets the name of tkinter date submissions GUI window
    # I know that this is not needed since the date submissions GUI window is not big enough
    gui.title("Calendar")

    # This function sets the configuration of the date submissions GUI window
    # Changed the sizing of the date submissions GUI window
    gui.geometry("157x250")

    # This function is added so the date submissions GUI window can not be expanded
    # I added this function to not be able to resize the date submissions GUI window
    gui.resizable(0, 0)

    # This function is creates a calendar label with specified font and size
    # I changed the color and text to my liking
    cal = Label(gui, text="Calendar", bg="pink",
                font=("Times", 28, "bold"))

    # This function creates a 'Enter Year' label
    # I added this function to let the user know that they need to input the 'Year'
    year = Label(gui, text="Enter Year", bg="pink")

    # This function creates a text entry box for filling or typing the information
    # I added this function to be able to input the 'Year' to get the exact date
    year_field = Entry(gui)

    # This function creates a 'Enter Day' label
    # I added this function to let the user know that they need to input the 'Day'
    day = Label(gui, text="Enter Day", bg="pink")

    # This function creates a text entry box for filling or typing the information
    # I added this function to be able to input the 'Day' to get the exact date
    day_field = Entry(gui)

    # This function creates a 'Enter Month' label
    # I added this function to let the user know that they need to input the 'Month'
    month = Label(gui, text="Enter Month Number", background="pink")

    # This function creates a text entry box for filling or typing the information for the month, day, and year
    # I added this function to be able to input the 'Month' to get the exact date
    month_field = Entry(gui)

    # This function creates a 'Show Calendar' button and attached to showCal function (function to show the calendar)
    # I changed the command to 'showCal' since that is the function I used for the calendar
    Show = Button(gui, text="Show Calendar", fg="Black",
                  background="white", command=showCal)

    # This function creates a 'Exit Button' and attached to exit function in the date submissions GUI window
    # I changed the color of the buttons
    Exit = Button(gui, text="Exit", fg="Black", bg="white", command=exit)

    # The grid method function is used for placing the widgets at respective positions in table like structure
    # I added the day and month grids to make it mine! I wanted to be able to select the full date
    cal.grid(row=1, column=1)

    month.grid(row=2, column=1)

    month_field.grid(row=3, column=1)

    day.grid(row=4, column=1)

    day_field.grid(row=5, column=1)

    year.grid(row=6, column=1)

    year_field.grid(row=7, column=1)

    Show.grid(row=8, column=1)

    Exit.grid(row=9, column=1)

    # Executes the GUI
    gui.mainloop()
