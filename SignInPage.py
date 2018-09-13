from Tkinter import *
from LogInPage import *
import Message


class SignInPage(object):
    def __init__(self, parent, root, height, width, side, color, dbConnection):

        self.parent = parent
        self.root = root
        self.height = height
        self.width = width
        self.side = side
        self.color = color
        self.dbConnection = dbConnection
        self.font = ('Times', 14, 'roman')

        self.gui_init()

    def gui_init(self):

        self.topFrame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)
        self.topFrame.pack(side=self.side, expand=True, fill=BOTH)
        self.topFrame.grid_propagate(0)
        #self.bottomFrame = Frame(master)
        #self.bottomFrame.pack(side=BOTTOM, fill=X)

        #creating labels

        int_frame = Frame(
            self.topFrame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 4 / 5,
            width=self.width * 4 / 5)
        int_frame.grid_propagate(0)
        int_frame.pack(expand=True, fill=BOTH)
        int_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.userNameLabel = Label(
            int_frame, text="UserName", font=self.font, bg=self.color)
        self.userNameLabel.grid(row=1, column=0, sticky=W, padx=2, pady=2)

        self.firstNameLabel = Label(
            int_frame, text="FirstName", font=self.font, bg=self.color)
        self.firstNameLabel.grid(row=2, column=0, sticky=W, padx=2, pady=2)

        self.lastNameLabel = Label(
            int_frame, text="LastName", font=self.font, bg=self.color)
        self.lastNameLabel.grid(row=3, column=0, sticky=W, padx=2, pady=2)

        self.emailLabel = Label(
            int_frame, text="Email", font=self.font, bg=self.color)
        self.emailLabel.grid(row=4, column=0, sticky=W, padx=2, pady=2)

        self.passwordLabel = Label(
            int_frame, text="Password", font=self.font, bg=self.color)
        self.passwordLabel.grid(row=5, column=0, sticky=W, padx=2, pady=2)

        self.bankingCardLabel = Label(
            int_frame, text="Banking Card Nr", font=self.font, bg=self.color)
        self.bankingCardLabel.grid(row=6, column=0, sticky=W, padx=2, pady=2)

        #creating entries
        self.userNameEntry = Entry(int_frame, font=self.font)
        self.userNameEntry.grid(row=1, column=1, padx=2, pady=2)

        self.firstNameEntry = Entry(int_frame, font=self.font)
        self.firstNameEntry.grid(row=2, column=1, padx=2, pady=2)

        self.lastNameEntry = Entry(int_frame, font=self.font)
        self.lastNameEntry.grid(row=3, column=1, padx=2, pady=2)

        self.emailEntry = Entry(int_frame, font=self.font)
        self.emailEntry.grid(row=4, column=1, padx=2, pady=2)

        self.passwordEntry = Entry(int_frame, show="*", font=self.font)
        self.passwordEntry.grid(row=5, column=1, padx=2, pady=2)

        self.CreditCardNumberEntry = Entry(int_frame, show="*", font=self.font)
        self.CreditCardNumberEntry.grid(row=6, column=1, padx=2, pady=2)

        #creating register button
        self.registerButton = Button(
            int_frame, text="Register New User", font=32)
        self.registerButton.bind("<Button-1>", self.__registerAction)
        self.registerButton.grid(row=7, columnspan=2, padx=2, pady=2)

    def __registerAction(self, event):

        userName = self.userNameEntry.get()
        firstName = self.firstNameEntry.get()
        lastName = self.lastNameEntry.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        creditCard = self.CreditCardNumberEntry.get()
        self.__deleteText()
        args = (userName, None, None, None, None)
        cursor = self.dbConnection.cursor()
        result = cursor.callproc('log_in', args)

        if result[1] is not None:
            self.__message("Username exists")
        else:
            args = (userName, firstName, lastName, email, creditCard, password)
            result = cursor.callproc('add_new_user', args)
            self.dbConnection.commit()
            self.__message("Registerd successfully")
        cursor.close()



    def __message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window, self.color, message)
        new_window.wait_window()

    def __deleteText(self):

        self.userNameEntry.delete(0, 'end')
        self.firstNameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')
        self.CreditCardNumberEntry.delete(0, 'end')
