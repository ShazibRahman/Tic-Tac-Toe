from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('Tic-Tac-Toe')
bclick = True
flag = 0


def clearstatus():
    for lis in b:
        for button in lis:
            button["text"] = " "
            button.configure(bg='grey')



def changecolor(*lis):
    for i in lis :
        i.configure(bg='blue')
        i.configure(fg='black')




def activate():
    for lis in b:
        for button in lis:
            button.configure(state=NORMAL)


def checkForWin(a):

    won=False

    for i in range(4):
        if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==b[i][3]["text"]==a ):
            changecolor(b[i][0],b[i][1],b[i][2],b[i][3])
            won=True


        if  b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==b[3][i]['text']==a:
            changecolor(b[0][i],b[1][i],b[2][i],b[3][i])
            won=True

    if b[0][0]['text']==b[1][1]['text']==b[2][2]['text']==b[3][3]['text']==a :
        changecolor(b[0][0],b[1][1],b[2][2],b[3][3])
        won=True
    if b[3][0]['text']==b[2][1]['text']==b[1][2]['text']==b[0][3]['text']==a:
        changecolor(b[3][0],b[2][1],b[1][2],b[0][3])
        won=True
    if won:



        tkinter.messagebox.showinfo("Game-over", f"Player {a} wins!!")


        reset()
    if (flag == 16):
        tkinter.messagebox.showinfo("Game-over", "It's a tie.")

        reset()



def btnClick(button):
    global bclick, flag
    if button["text"] == " " and bclick == True:
        button.configure(fg='red')
        button["text"] = "X"
        bclick = False

        checkForWin("X")
        lab['text']="O's turn"
        flag += 1
    elif button["text"] == " " and bclick == False:
        button["text"] = "O"
        button.configure(fg='blue')
        bclick = True


        checkForWin("O")
        lab['text']="x's turn"
        flag += 1
    elif button["text"] != " ":
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

# This function is used to reset the current state of the board.


def reset():
    global bclick, flag
    flag, bclick = 0, True
    clearstatus()
    activate()


# these are the settings buttons
button_reset = Button(tk, text="Reset", font='Times 20 bold',
                      bg='red', fg='white', height=1, width=6, command=lambda: reset())
button_reset.grid(row=0, column=1, columnspan=2)

# these are the game buttons
button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=1, column=0)
button2 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=1, column=1)
button3 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=1, column=2)
button4 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=1, column=3)
button5 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=2, column=0)
button6 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=2, column=1)
button7 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=2, column=2)
button8 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=2, column=3)
button9 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=3, column=0)
button10 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button10))
button10.grid(row=3, column=1)
button11= Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button11))
button11.grid(row=3, column=2)
button12 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button12))
button12.grid(row=3, column=3)
button13 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button13))
button13.grid(row=4, column=0)
button14 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button14))
button14.grid(row=4, column=1)
button15 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button15))
button15.grid(row=4, column=2)
button16 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
                 fg='red', height=4, width=8, command=lambda: btnClick(button16))
button16.grid(row=4, column=3)
b = [
           [button1, button2, button3, button4],
           [button5, button6, button7, button8],
           [ button9,button10,button11,button12],
           [button13, button14, button15, button16]
    ]
lab=Label(tk, text="X's Turn", font='Times 20 bold',
                      bg='red', fg='white', height=1, width=8)
lab.grid(row=5, column=1, columnspan=2)

tk.mainloop()
