from Tkinter import *
import ttk
import NewBookPage
import Message


class AdminPage(object):
    def __init__(self, root, color, font, dbConnection):

        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.dbConnection = dbConnection
        self.color = color
        self.font = font
        self.screen_width = self.root.winfo_screenwidth() * 3 / 4
        self.screen_height = self.root.winfo_screenheight() * 3 / 4

        self.gui_init()

    def gui_init(self):

        self.up_frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.screen_height / 8,
            width=self.screen_width)
        self.up_frame.grid_propagate(0)
        self.up_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.down_frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.screen_height * 7 / 8,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.profileFrame = ProfileFrame(self.up_frame, self.screen_width / 2,
                                         self.screen_height / 8, self.color,
                                         self.font)

        self.logoutFrame = LogOutFrame(self.root, self.up_frame, self.screen_width / 2,
                                       self.screen_height / 8, self.color,
                                       self.font, self.dbConnection)

        self.booksInfoFrame = BookInformation(
            self.down_frame, self.screen_width, self.screen_height * 7 / 8,
            self.color, self.font, self.dbConnection)


class ProfileFrame(object):
    def __init__(self, root, width, height, color, font):

        self.root = root
        self.width = width
        self.height = height
        self.color = color
        self.font = font

        self.gui_init()

    def gui_init(self):

        self.frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            bd=5,
            relief=RAISED,
            width=self.width,
            height=self.height)
        self.frame.pack(expand=True, side=LEFT, fill=BOTH)
        self.frame.grid_propagate(0)

        profileInfo = self.__extract_profile()

        self.profileLabel = Label(
            self.frame, text=profileInfo, font=self.font, bg=self.color)
        self.profileLabel.place(relx=0.5, rely=0.5, anchor='center')

    def __extract_profile(self):

        profile_info = "ADMIN"
        return profile_info


class LogOutFrame(object):
    def __init__(self, parent, root, width, height, color, font, dbConnection):

        self.root = root
        self.parent = parent
        self.width = width
        self.height = height
        self.color = color
        self.font = font
        self.dbConnection = dbConnection
        self.gui_init()

    def gui_init(self):

        self.frame = Frame(
            self.root,
            cursor='hand1',
            bd=5,
            relief=RAISED,
            bg=self.color,
            width=self.width,
            height=self.height)
        self.frame.pack(side=LEFT, expand=True, fill=BOTH)
        self.frame.grid_propagate(0)

        self.logout_button = Button(
            self.frame, text="LogOut", font=self.font, borderwidth=5)
        self.logout_button.place(relx=0.5, rely=0.5, anchor='center')

        self.logout_button.bind("<Button-1>", self.__logOutAction)

    def __logOutAction(self, event):
        self.dbConnection.close()
        for child in self.parent.winfo_children():
            child.destroy()
        self.parent.destroy()


class BookInformation(object):
    def __init__(self, root, width, height, color, font, dbConnection):

        self.root = root
        self.width = width
        self.height = height
        self.color = color
        self.font = font
        self.dbConnection = dbConnection

        self.gui_init()

    def gui_init(self):

        frame_up = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            width=self.width,
            height=self.height * 1 / 12)
        frame_up.grid_propagate(0)
        frame_up.pack(side=TOP, expand=True, fill=BOTH)

        frame_middle = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            width=self.width,
            height=self.height * 10 / 12)
        frame_middle.grid_propagate(0)
        frame_middle.pack(side=TOP, expand=True, fill=BOTH)

        frame_down = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            width=self.width,
            height=self.height * 1 / 12)
        frame_down.grid_propagate(0)
        frame_down.pack(side=TOP, expand=True, fill=BOTH)

        self.uploadedFilesLabel = Label(
            frame_up, text="Available Books", font=self.font, bg=self.color)
        self.uploadedFilesLabel.place(relx=0.5, rely=0.5, anchor='center')

        self.booksDisplay = ttk.Treeview(
            frame_middle,
            columns=('#1', '#2', '#3', '#4', '#5'),
            height=20,
            show='headings',
            padding=(1, 1, 1, 1))

        self.booksDisplay.heading('#1', text='Title')
        self.booksDisplay.heading('#2', text='Author')
        self.booksDisplay.heading('#3', text='Genre')
        self.booksDisplay.heading('#4', text='Price')
        self.booksDisplay.heading('#5', text='Stock')
        self.booksDisplay.column('#1', stretch=True, width=self.width / 5)
        self.booksDisplay.column('#2', stretch=True, width=self.width / 5)
        self.booksDisplay.column('#3', stretch=True, width=self.width / 5)
        self.booksDisplay.column('#4', stretch=True, width=self.width / 5)
        self.booksDisplay.column('#5', stretch=True, width=self.width / 5)

        self.booksDisplay.grid(row=5, columnspan=5, sticky='nw')
        #self.booksDisplay.place(relx=0.5, rely=0.5, anchor='center')

        self.booksDisplayStyle = ttk.Style()
        self.booksDisplayStyle.configure(
            "Treeview", font=self.font, rowheight=50)
        self.booksDisplayStyle.configure("Treeview.Heading", font=self.font)

        self.booksDisplay.tag_configure(
            "tagBook", background="white", foreground="red", font=self.font)

        self.addNewBookButton = Button(
            frame_down, text="Add new book", font=self.font)
        self.addNewBookButton.place(relx=0.5, rely=0.5, anchor='center')

        self.addNewBookButton.bind("<Button-1>", self.__addNewBook)

        self.__displayBooks()

    def __addNewBook(self, event):

        new_window = Toplevel(self.root)
        NewBookPage.NewBook(new_window, self.color, self.dbConnection)
        new_window.wait_window()
        self.__displayBooks()

    def __displayBooks(self):

        for child in self.booksDisplay.get_children():
            self.booksDisplay.delete(child)

        cursor = self.dbConnection.cursor()
        cursor.callproc('getAllBooks')
        for result in cursor.stored_results():
            books = result.fetchall()
            for book in books:
                self.booksDisplay.insert(
                    '', 'end', values=book, tags='tagBook')
        cursor.close()
