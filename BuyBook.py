from Tkinter import *
from LogInPage import *
import Message
import ttk


class BuyBook(object):
    def __init__(self, root, color, font, dbConnection, userInfo):

        self.root = root
        self.color = color
        self.font = font
        self.dbConnection = dbConnection
        self.userName = userInfo['userName']

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height * 3 / 4
        self.width = self.screen_width * 3 / 4

        self.gui_init()

    def gui_init(self):

        self.root.title("Buy new Book")
        self.root.resizable(width=False, height=FALSE)

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
            height=self.height * 1 / 10,
            width=self.width)

        topFrame.grid_propagate(0)
        topFrame.pack(side=TOP, expand=True, fill=BOTH)

        downFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width)

        downFrame.grid_propagate(0)
        downFrame.pack(side=TOP, expand=True, fill=BOTH)

        self.__printBooks(downFrame)
        self.__printTitle(topFrame)

    def __printTitle(self, frame):

        titleLable = Label(
            frame, text='Available Books', font=self.font, bg=self.color)
        titleLable.place(relx=0.5, rely=0.5, anchor='center')

    def __printBooks(self, frame):

        booksDisplay = ttk.Treeview(
            frame,
            columns=('#1', '#2', '#3', '#4', '#5', '#6'),
            height=20,
            show='headings',
            padding=(1, 1, 1, 1))

        booksDisplay.heading('#1', text='Title')
        booksDisplay.heading('#2', text='Author')
        booksDisplay.heading('#3', text='Genre')
        booksDisplay.heading('#4', text='Price')
        booksDisplay.heading('#5', text='Stock')
        booksDisplay.heading('#6', text='Score')

        booksDisplay.column('#1', stretch=True, width=self.width / 6)
        booksDisplay.column('#2', stretch=True, width=self.width / 6)
        booksDisplay.column('#3', stretch=True, width=self.width / 6)
        booksDisplay.column('#4', stretch=True, width=self.width / 6)
        booksDisplay.column('#5', stretch=True, width=self.width / 6)
        booksDisplay.column('#6', stretch=True, width=self.width / 6)

        booksDisplay.pack(side=TOP, fill=BOTH, expand=TRUE)

        booksDisplay.tag_configure(
            "tagBook",
            background="white",
            foreground="blue",
            font=self.font)

        booksDisplay.bind('<ButtonRelease-1>', self.__buyBook)

        self.__displayAllBooks(booksDisplay)

    def __buyBook(self, event):

        selectedItem = event.widget.focus()
        valueItem = event.widget.item(selectedItem)['values']
        print(valueItem)
        bookName = valueItem[0]

        args = (bookName, self.userName)
        cursor = self.dbConnection.cursor()

        result = cursor.callproc('buyBook', args)
        self.dbConnection.commit()
        cursor.close()
        self.__message("Buyed successfully")
        self.__displayAllBooks(event.widget)


    def __displayAllBooks(self, booksDisplay):

        for child in booksDisplay.get_children():
            booksDisplay.delete(child)

        cursor = self.dbConnection.cursor()
        cursor.callproc('getBooksUser')
        for result in cursor.stored_results():
            books = result.fetchall()
            for book in books:
                booksDisplay.insert(
                    '', 'end', values=book, tags='tagBook')
        cursor.close()

    def __message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window, self.color, message)
        new_window.wait_window()

