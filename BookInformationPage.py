from Tkinter import *
import ttk
import AddReview
import Message


class BookInformation(object):
    def __init__(self, root, color, dbConnection, bookName, userInfo):

        self.root = root
        self.color = color
        self.bookName = bookName
        self.dbConnection = dbConnection
        self.userName = userInfo['userName']
        self.font = ('Times', 12, 'roman')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height / 3
        self.width = self.screen_width / 3
        self.gui_init()

    def gui_init(self):

        self.root.title(self.bookName)
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

        upFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width)

        upFrame.grid_propagate(0)
        upFrame.pack(side=TOP, expand=True, fill=BOTH)

        upLeftFrame = Frame(
            upFrame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width / 3,
            relief=RAISED,
            bd=5)
        upLeftFrame.grid_propagate(0)
        upLeftFrame.pack(side=LEFT, expand=True, fill=BOTH)

        upRightFrame = Frame(
            upFrame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width * 2 / 3,
            relief=RAISED,
            bd=5)
        upRightFrame.grid_propagate(0)
        upRightFrame.pack(side=LEFT, expand=True, fill=BOTH)

        downFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height / 10,
            width=self.width)
        downFrame.grid_propagate(0)
        downFrame.pack(side=TOP, expand=True, fill=BOTH)

        self.__initBookInfo(upLeftFrame)
        self.__initReviews(upRightFrame)
        self.__initAddReviewButton(downFrame)

    def __initBookInfo(self, frame):

        book_information = self._getBookInformation()

        bookProfileLabel = Label(
            frame,
            text=book_information,
            font=self.font,
            bg=self.color,
            fg='red')
        bookProfileLabel.place(relx=0.5, rely=0.5, anchor='center')

    def __initReviews(self, frame):

        self.reviewsDisplay = ttk.Treeview(
            frame, columns=('#1', '#2'), height=10, show='headings')

        self.reviewsDisplay.heading('#1', text='Reviewer')
        self.reviewsDisplay.heading('#2', text='Score')
        self.reviewsDisplay.column('#1', stretch=True, width=self.width / 4)
        self.reviewsDisplay.column('#2', stretch=True, width=self.width / 4)

        self.reviewsDisplay.grid_propagate(0)
        self.reviewsDisplay.pack(side=TOP, expand=True, fill=BOTH)

        #reviewsDisplayStyle = ttk.Style()

        #reviewsDisplayStyle.configure("Treeview", font=self.font, rowheight=50)
        #reviewsDisplayStyle.configure("Treeview.Heading", font=self.font)

        #reviewsDisplay.grid(row=5,columnspan=5, sticky='')

        self.reviewsDisplay.tag_configure(
            "tagReview",
            background="white",
            foreground="green",
            font=self.font)

        self.reviewsDisplay.bind("<ButtonRelease-1>", self.__showReview)

        self.__displayAvailableReviews()

    def __initAddReviewButton(self, frame):
        addReviewButton = Button(
            frame, text="Add review", font=self.font, borderwidth=5)
        addReviewButton.place(relx=0.5, rely=0.5, anchor='center')

        addReviewButton.bind("<Button-1>", self.__addReview)

    def _getBookInformation(self):

        args = (self.bookName, )
        cursor = self.dbConnection.cursor()
        cursor.callproc('getBookInfo', args)
        for result in cursor.stored_results():
            book = result.fetchall()
            book_info = map(str, book[0])
            book_info = "\n".join(book_info)

        cursor.close()
        return book_info

    def __addReview(self, event):

        new_window = Toplevel(self.root)
        AddReview.AddReview(new_window, self.color, self.font,
                                        self.dbConnection, self.userName,
                                        self.bookName)
        new_window.wait_window()
        self.__displayAvailableReviews()

    def __showReview(self, event):

        selectedItem = event.widget.focus()
        itemValue = event.widget.item(selectedItem)

        print(itemValue['values'][0], itemValue['values'][1])

    def __displayAvailableReviews(self):

        for child in self.reviewsDisplay.get_children():
            self.reviewsDisplay.delete(child)

        args = (self.bookName, )
        cursor = self.dbConnection.cursor()
        cursor.callproc('getBookReviews', args)
        for result in cursor.stored_results():
            reviews = result.fetchall()
            for review in reviews:
                self.reviewsDisplay.insert(
                    '', 'end', values=review, tags='tagReview')
        cursor.close()
