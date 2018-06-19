from Tkinter import *
import glob
# from text_parser import find
# from text_parser import parse_text

#key down function
def click():
    entered_text = textentry.get() #this will collect text from text entry box
    entered_text2 = textentry2.get()
    response = parse_text(entered_text, entered_text2)
    output.delete(0.0, END)
    output.insert(response, END)

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

#text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=8, column=0, columnspan=2, sticky="W")


#run main loop
window.mainloop()
