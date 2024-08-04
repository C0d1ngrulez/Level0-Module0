from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer = simpledialog.askstring(title='Greeter', prompt='What is 10 times 10?')
    #      // 3.  Use an if statement to check if their answer is correct
    if answer == "100":
        #      // 4.  if the user's answer was correct, add one to their score
        simpledialog.askstring(title='Greeter', prompt='Correct!')
        score += 10
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    #      // Option: Subtract a point from their score for a wrong answer
    else:
        simpledialog.askstring(title='Greeter', prompt='Incorrect!')

    answer = simpledialog.askstring(title='Greeter', prompt='What is 100+20-10=?')
    if answer == "110":
        simpledialog.askstring(title='Greeter', prompt='Correct!')
        score += 10
    else:
        simpledialog.askstring(title='Greeter', prompt='Incorrect!')

    answer = simpledialog.askstring(title='Greeter', prompt='Who is the best marvel super hero?')
    if answer == "Wolverine":
        simpledialog.askstring(title='Greeter', prompt='Nice')
        score += 10
    else:
        simpledialog.askstring(title='Greeter', prompt='Fair enough')

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function
    messagebox.showinfo(message=score)
    # Run the window's .mainloop() method
    window.mainloop()
