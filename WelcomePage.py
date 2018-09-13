from Tkinter import *
from mysql.connector import MySQLConnection
from LogInPage import *
from SignInPage import *

USER = 'user'
PASSWORD = '****'
HOST = 'localhost'
DATABASE = 'bookStoreDB'


class WelcomePage(object):
    '''
    This is the initial class instantiated when the application starts.
    It is responsible for rendering the WelcomePage of the application and
    for establishing connection to the database.
    It contains the LogIn Frame where an existing user or the administrator
    authenticate and the Register frame for registering a new user.
    '''
    def __init__(self, root):

        self.root = root
        self.screen_width = root.winfo_screenwidth() / 2
        self.screen_height = root.winfo_screenheight() / 2
        self.color = 'light sky blue'
        self.dbConnection = MySQLConnection(
            user=USER, password=PASSWORD, host=HOST, database=DATABASE)
        self.adminCredentials = ('admin', 'root')

        self.gui_init()

    def gui_init(self):

        self.up_frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.screen_height / 4,
            width=self.screen_width)
        self.up_frame.grid_propagate(0)
        self.up_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.down_frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.screen_height * 3 / 4,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.welcomeText = Label(
            self.up_frame,
            text="BookStore\nby Dan Muntean",
            font=('Verdana', 16, 'roman italic'),
            bg=self.color)
        self.welcomeText.place(relx=.5, rely=.5, anchor='center')

        self.login_frame = LoginFrame(self.root, self.down_frame,
                                      self.screen_height * 3 / 4,
                                      self.screen_width / 2, LEFT, self.color,
                                      self.dbConnection, self.adminCredentials)

        self.register_frame = SignInPage(
            self.root, self.down_frame, self.screen_height * 3 / 4,
            self.screen_width / 2, LEFT, self.color, self.dbConnection)


root = Tk()
root.title("BookStore")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.minsize(width=screen_width / 2, height=screen_height / 2)
root.maxsize(width=screen_width, height=screen_height)
root.resizable(width=True, height=True)

logupFrame = WelcomePage(root)
root.mainloop()
