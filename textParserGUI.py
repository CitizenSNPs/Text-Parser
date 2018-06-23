from Tkinter import *
from text_parser import *

#key down function
def click():
    entered_text = textentry.get() #this will collect text from text entry box
    entered_text2 = textentry2.get()
    response = parse_text(entered_text, entered_text2)

#main:
window = Tk()
window.title("My program")
window.configure(background="black")


#create label
Label(window, text="Please enter folder path.", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky="W")

#create text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky="W")

#create another label
Label(window, text="Enter substring", bg="black", fg="white", font="none 12 bold").grid(row=3, column=0, sticky="W")

#another text box
textentry2 = Entry(window, width=20, bg="white")
textentry2.grid(row=4, column=0, sticky="W")

#add submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=6, column=0, sticky="W")
#width is 6 because 6 letters in SUBMIT



#run main loop
window.mainloop()

if __name__ == "__main__":
    import glob
