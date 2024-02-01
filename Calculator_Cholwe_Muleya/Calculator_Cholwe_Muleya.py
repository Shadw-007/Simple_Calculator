from tkinter import* #enables the GUI to appear

def btnClick(numbers): #function for numbers and operators
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay(): #function to clear screen display
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput(): #function to show results
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

cal = Tk()
cal.title("Calculator") #title on the GUI
operator = ""
text_Input = Variable()

txtDisplay = Entry(cal, font = ('arial', 20), textvariable = text_Input, bd = 12, insertwidth = 4,
                   bg = "white", justify = "right").grid(columnspan = 5) #this is for main display

btn7 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "7", bg = "silver", command= lambda:btnClick(7)).grid(row = 1, column = 0) #button number 7

btn8 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "8", bg = "silver", command= lambda:btnClick(8)).grid(row = 1, column = 1) #button number 8

btn9 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "9", bg = "silver", command= lambda:btnClick(9)).grid(row = 1, column = 2) #button number 9

Multiplicaiton = Button(cal, padx = 34.5, bd = 8, fg = "black", font = ('arial', 20),
              text = "*", bg = "silver", command= lambda:btnClick("*")).grid(row = 1, column = 3) #multiplication button

Division = Button(cal, padx = 32, bd = 8, fg = "black", font = ('arial', 20),
              text = "/", bg = "silver", command= lambda:btnClick("/")).grid(row = 1, column = 4) #division button

#==================================================================================
btn4 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "4", bg = "silver", command= lambda:btnClick(4)).grid(row = 2, column = 0) #button number 4

btn5 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "5", bg = "silver", command= lambda:btnClick(5)).grid(row = 2, column = 1) #button number 5

btn6 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "6", bg = "silver", command= lambda:btnClick(6)).grid(row = 2, column = 2) #button number 6

Addition = Button(cal, padx = 32, bd = 8, fg = "black", font = ('arial', 20),
              text = "+", bg = "silver", command= lambda:btnClick("+")).grid(row = 2, column = 3) #addition button

Subtaction = Button(cal, padx = 32, bd = 8, fg = "black", font = ('arial', 20),
              text = "-", bg = "silver", command= lambda:btnClick("-")).grid(row = 2, column = 4) #subtraction button

#==================================================================================
btn1 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "1", bg = "silver", command= lambda:btnClick(1)).grid(row = 3, column = 0) #button number 1

btn2 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "2", bg = "silver", command= lambda:btnClick(2)).grid(row = 3, column = 1) #button number 2

btn3 = Button(cal, padx = 8, bd = 8, fg = "black", font = ('arial', 20),
              text = "3", bg = "silver", command= lambda:btnClick(3)).grid(row = 3, column = 2) #button number 3

#==================================================================================
btn0 = Button(cal, padx = 32, bd = 8, fg = "black", font = ('arial', 20),
              text = "0", bg = "silver", command= lambda:btnClick(0)).grid(row = 3, column = 3) #button 0

btnEnter = Button(cal, padx = 4, bd = 8, fg = "black", font = ('arial', 20),
              text = "Enter", bg = "silver", command = btnEqualsInput).grid(row = 3, column = 4) #enter (=) button

btnClear = Button(cal, padx = 160, bd = 8, fg = "black", font = ('arial', 20, "bold"),
              text = "Clear", bg = "silver", command = btnClearDisplay).grid(row = 4, columnspan = 5) #clear (erase) button

cal.mainloop()
