
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from select import select

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import NW, Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class NewBookWindow:
    def __init__(self):    
        self.newbookwindow= Tk()

        self.newbookwindow.title("Add a New Book")
        self.newbookwindow.geometry("1300x700")
        self.newbookwindow.configure(bg = "#2C0A59")

    def back_to_home(self):
        from interface.screens.HomeWindow import HomeWindow
        self.newbookwindow.destroy()
        self.novaHome = HomeWindow()
        self.novaHome.generate_home_window()

    def submit(self):
        from controller.database import 
        from controller.request import request 
        from datetime import date
        isbn = self.entry_isbn.get()
        datas = request(isbn)
        datas['status'] = self.status 
        if self.status == "read":
            datas['start_of_reading'] = "NULL"
            datas['end_of_reading'] = "NULL"
        elif self.status == "reading":
            datas['start_of_reading'] = str(date.today())
            datas['end_of_reading'] = "NULL"
        elif self.status == "IWTR":
            datas['start_of_reading'] = self.IWTR_window.date
            datas['end_of_reading'] = "NULL"

        print(datas)
        
        del datas
    def select_status(self, status):
        self.status = status
        print(status)
        

    def clicked_button_read(self, event):
        self.status = 'read'
        self.button_read.config(image=self.newbookwindow.btn_activeRead)
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_activeRead))
        
        self.button_reading.config(image=self.newbookwindow.btn_inactiveReading)
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_inactiveReading))

        self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR)
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR))

    def clicked_button_reading(self, event):
        self.status = 'reading'
        self.button_reading.config(image=self.newbookwindow.btn_activeReading)
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_activeReading))
        
        self.button_read.config(image=self.newbookwindow.btn_inactiveRead)
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_inactiveRead))

        self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR)
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR))

    def clicked_button_IWTR(self, event):
        self.status = "IWTR"
        self.button_IWTR.config(image=self.newbookwindow.btn_activeIWTR)
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_activeIWTR))
        
        self.button_reading.config(image=self.newbookwindow.btn_inactiveReading)
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_inactiveReading))

        self.button_read.config(image=self.newbookwindow.btn_inactiveRead)
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_inactiveRead))

    def go_to_IWTR_window(self):
        from interface.screens.IWantToReadWindow import IWantToReadWindow
        self.IWTR_window = IWantToReadWindow()
        self.IWTR_window.generate_IWTR_window()

    def generate_new_book_window(self):
        canvas = Canvas(
            self.newbookwindow,
            bg = "#2C0A59",
            height = 700,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)

        image_image_readStatus = PhotoImage(
            file=relative_to_assets("image_readStatus.png"))
        image_readStatus = canvas.create_image(
            718.0,
            347.0,
            image=image_image_readStatus
        )

        image_image_ISB = PhotoImage(
            file=relative_to_assets("image_ISBN.png"))
        image_2 = canvas.create_image(
            683.0,
            180.0,
            image=image_image_ISB
        )

        image_image_AddNewBook = PhotoImage(
            file=relative_to_assets("image_AddNewBook.png"))
        image_AddNewBook = canvas.create_image(
            321.0,
            58.0,
            image=image_image_AddNewBook
        )

        entry_image_isbn = PhotoImage(
            file=relative_to_assets("entry_isbn.png"))

        entry_bg_1 = canvas.create_image(
            670.5,
            253.0,
            image=entry_image_isbn
        )

        self.entry_isbn = Entry(
            bd=0,
            bg="#93679A",
            highlightthickness=0,
            justify="center",
            font=('Georgia 20')      
        )
        self.entry_isbn.place(
            x=375.0,
            y=235.0,
            width=600.0,
            height=30.75,
        )

        self.newbookwindow.btn_inactiveRead = PhotoImage(file=relative_to_assets("button_read.png"))
        self.newbookwindow.btn_activeRead = PhotoImage(file=relative_to_assets("button_ReadActive.png"))

        self.button_image_read = PhotoImage(
            file=relative_to_assets("button_read.png"))
        self.button_read = Button(
            image=self.button_image_read,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            cursor="hand2",
        )
        self.button_read.place(
            x=537.0,
            y=380.0,

        )

        self.button_read.bind("<Enter>", lambda e: self.button_read.config(image=self.newbookwindow.btn_activeRead))
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_inactiveRead))
        self.button_read.bind("<Button-1>", self.clicked_button_read)

        self.newbookwindow.btn_inactiveReading = PhotoImage(file=relative_to_assets("button_reading.png"))
        self.newbookwindow.btn_activeReading = PhotoImage(file=relative_to_assets("button_ReadingActive.png"))

        button_image_reading = PhotoImage(
            file=relative_to_assets("button_reading.png"))
        self.button_reading = Button(
            image=button_image_reading,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            cursor="hand2",
        )
        self.button_reading.place(
            x=537.0,
            y=480.0,
        )

        self.button_reading.bind("<Enter>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_activeReading))
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_inactiveReading))
        self.button_reading.bind("<Button-1>", self.clicked_button_reading)

        self.newbookwindow.btn_inactiveIWTR = PhotoImage(file=relative_to_assets("button_IWTR.png"))
        self.newbookwindow.btn_activeIWTR = PhotoImage(file=relative_to_assets("button_IWTRActive.png"))

        button_image_IWTR = PhotoImage(
            file=relative_to_assets("button_IWTR.png"))
        self.button_IWTR = Button(
            image=button_image_IWTR,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            command=self.go_to_IWTR_window,
            cursor="hand2",
        )
        self.button_IWTR.place(
            x=537.0,
            y=580.0,
        )
        self.button_IWTR.bind("<Enter>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_activeIWTR))
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR))
        self.button_IWTR.bind("<Button-1>",self.clicked_button_IWTR)

        button_image_plus = PhotoImage(
            file=relative_to_assets("button_plus.png"))
        button_plus = Button(
            image=button_image_plus,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A60",
            command=self.submit,
            cursor="hand2",
        )
        button_plus.place(
            x=1087.2080078125,
            y=227.0,
        )

        button_image_icon = PhotoImage(
            file=relative_to_assets("icon.png"))
        button_icon = Button(
            image=button_image_icon,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A60",
            command=self.back_to_home,
            cursor="hand2",
        )
        button_icon.place(
            x=1197.0,
            y=19.0,
        )
        self.newbookwindow.resizable(False, False)
        self.newbookwindow.mainloop()
