from tkinter import *

top = Tk()
songList = []



def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)
            
def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, Row = 1)
    B1Main = Button(text = week1, bg = "white", command = week1)
    B1Main.grid(column = 0, row = 1)
    B2Main = Button(text = week2, bg = "light orange", 
    B3Main

def week1():
    clearWindow()
    #This is a Label widget
    L1 = Label(top, text="ourTunes")
    L1.grid(column= 0, row= 1)
    
        def addTrack():
            songList.append(E1.get())
            E1.delete(0, END)

    #This is an Entry widget (for text entry)
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row = 2)

    #This is a Button widget
    B1 = Button(text = " + ", bg = "white", command= addTrack)
    B1.grid(column = 1, row = 2)

    B2 = Button(text = "Playlist", bg = "light blue", command = printList)
    B2.grid(column= 1, row = 1)

    B3 = Button(text = "Export", bg = "orange", command= exportList)
    B3.grid(column = 1, row = 3)


def week2 ():
    clearWindow()
    L1W2 = Label(top, text= "Dice Roller App")
    L1W2.grid(Column = 2, row = 1)
    
    L2W2 = Label(top, text= "# of sides")
    L2W2.grid(Column = 0, row = 2)
    
    E1W2 = Entry()
    E2W2 = Entry()
    B1W2 = Button()
    #dont forget grids
    
if _name_ == "_main_":
    mainMenu()
    top.mainloop()
