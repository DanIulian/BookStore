from Tkinter import *
import Message


class NewBook(object):
    def __init__(self, root, color, dbConnection):

        self.root = root
        self.color = color
        self.dbConnection = dbConnection
        self.font = ('Times', 14, 'roman')

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height / 3
        self.width = self.screen_width / 3

        self.gui_init()

    def gui_init(self):

        self.root.title("Add new book page")
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

        self.topFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 4 / 5,
            width=self.width * 4 / 5,
        )

        self.topFrame.grid_propagate(0)
        self.topFrame.pack(expand=True, fill=BOTH)
        self.topFrame.place(relx=0.5, rely=0.5, anchor='center')

        self.bookNameLable = Label(
            self.topFrame, text="BookName", font=self.font, bg=self.color)
        self.bookNameLable.grid(row=1, column=0, sticky=W, padx=2, pady=2)

        self.bookAuthorLabel = Label(
            self.topFrame, text="Author", font=self.font, bg=self.color)
        self.bookAuthorLabel.grid(row=2, column=0, sticky=W, padx=2, pady=2)

        self.bookGenreLabel = Label(
            self.topFrame, text="Genre", font=self.font, bg=self.color)
        self.bookGenreLabel.grid(row=3, column=0, sticky=W, padx=2, pady=2)

        self.bookYearLabel = Label(
            self.topFrame,
            text="Published Year",
            font=self.font,
            bg=self.color)
        self.bookYearLabel.grid(row=4, column=0, sticky=W, padx=2, pady=2)

        self.bookStockLabel = Label(
            self.topFrame, text="Stock", font=self.font, bg=self.color)
        self.bookStockLabel.grid(row=5, column=0, sticky=W, padx=2, pady=2)

        self.bookPriceLabel = Label(
            self.topFrame, text="Price", font=self.font, bg=self.color)
        self.bookPriceLabel.grid(row=6, column=0, sticky=W, padx=2, pady=2)

        #creating entries
        self.bookNameEntry = Entry(self.topFrame, font=self.font)
        self.bookNameEntry.grid(row=1, column=1, padx=2, pady=2)

        self.bookAuthorEntry = Entry(self.topFrame, font=self.font)
        self.bookAuthorEntry.grid(row=2, column=1, padx=2, pady=2)

        self.bookGenreEntry = Entry(self.topFrame, font=self.font)
        self.bookGenreEntry.grid(row=3, column=1, padx=2, pady=2)

        self.bookYearEntry = Entry(self.topFrame, font=self.font)
        self.bookYearEntry.grid(row=4, column=1, padx=2, pady=2)

        self.bookStockEntry = Entry(self.topFrame, font=self.font)
        self.bookStockEntry.grid(row=5, column=1, padx=2, pady=2)

        self.bookPriceEntry = Entry(self.topFrame, font=self.font)
        self.bookPriceEntry.grid(row=6, column=1, padx=2, pady=2)

        #creating register button
        self.registerButton = Button(
            self.topFrame, text="Register new Book", font=32)
        self.registerButton.bind("<Button-1>", self.__registerBook)
        self.registerButton.grid(row=7, column=1, columnspan=2, padx=1, pady=1)

    def __registerBook(self, event):

        bookName = self.bookNameEntry.get()
        bookAuthor = self.bookAuthorEntry.get()
        bookGenre = self.bookGenreEntry.get()
        bookYear  =self.bookYearEntry.get()
        bookCost = float(self.bookPriceEntry.get())
        bookStock = int(self.bookStockEntry.get())

        #check if the book exists
        cursor = self.dbConnection.cursor()
        args = (bookName, None)
        result = cursor.callproc('isBook', args)
        if result[1] != 0:
            self.__message("Book already exists")
        else:

            args = (bookName, bookGenre, bookAuthor, bookYear, bookStock, bookCost)
            result = cursor.callproc('insertBook', args)
            self.dbConnection.commit()
            self.__message("Book added successfully")
        cursor.close()






        for child in self.root.winfo_children():
            child.destroy()

        self.root.destroy()


    def __message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window, self.color, message)
        new_window.wait_window()
