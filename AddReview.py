from Tkinter import *
from LogInPage import *


class AddReview(object):
    def __init__(self, root, color, font, dbConnection, userName, bookName):

        self.root = root
        self.color = color
        self.font = font
        self.dbConnection = dbConnection
        self.userName = userName
        self.bookName = bookName

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height / 3
        self.width = self.screen_width / 3

        self.gui_init()

    def gui_init(self):

        self.root.title("Add new review")
        self.root.resizable(width=False, height=False)

        self.frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)
        self.frame.pack(side=TOP, expand=True, fill=BOTH)
        self.frame.grid_propagate(0)

        topFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 8 / 10,
            width=self.width)

        topFrame.grid_propagate(0)
        topFrame.pack(expand=True, fill=BOTH, side=TOP)

        middleFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 1 / 10,
            width=self.width)

        middleFrame.grid_propagate(0)
        middleFrame.pack(expand=True, fill=BOTH, side=TOP)

        downFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 1 / 10,
            width=self.width)
        downFrame.grid_propagate(0)
        downFrame.pack(expand=True, fill=BOTH, side=TOP)

        self.reviewBox = Text(
            topFrame,
            cursor='hand1',
            bg='white',
            font=self.font,
            height=10,
            width=60)
        self.reviewBox.place(relx=0.5, rely=0.5, anchor='center')

        #creating entries

        self.ScoreLabel = Label(
            middleFrame, text="Insert Score", font=self.font, bg=self.color)
        self.ScoreLabel.grid(row=0, column=1, sticky=E, padx=100, pady=2)
        self.ScoreEntry = Entry(middleFrame, width=25, font=self.font)
        self.ScoreEntry.grid(row=0, column=2, sticky=W, padx=2, pady=2)

        #creating register button
        self.registerButton = Button(downFrame, text="Submit review", font=32)
        self.registerButton.bind("<Button-1>", self.__submitReview)
        self.registerButton.place(relx=0.5, rely=0.5, anchor='center')

    def __submitReview(self, event):

        userScore = self.ScoreEntry.get()
        userReview = self.reviewBox.get("1.0", 'end-1c')

        args = (self.userName, self.bookName, userScore, userReview)
        print(args)

        cursor = self.dbConnection.cursor()

        cursor.callproc('insertReview', args)
        self.dbConnection.commit()

        cursor.close()

        for child in self.root.winfo_children():
            child.destroy()

        self.root.destroy()
