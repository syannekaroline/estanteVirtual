
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


IWTRwindow = Tk()
IWTRwindow.title("I Want to Read")
IWTRwindow.geometry("870x200")
IWTRwindow.configure(bg = "#2C0A59")
IWTRwindow.maxsize(width=988, height=700)#configura as dmensoes maximas da tela
IWTRwindow.minsize(width=400, height=170)


canvas = Canvas(
    IWTRwindow,
    bg = "#2C0A59",
    height = 270,
    width = 870,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

IWTRwindow.btn_2022inactive = PhotoImage(file=relative_to_assets("button_2022.png"))
IWTRwindow.btn_2022active = PhotoImage(file=relative_to_assets("button_2022Active.png"))

button_image_2022 = PhotoImage(
    file=relative_to_assets("button_2022.png"))

button_2022 = Button(
    image=button_image_2022,
    borderwidth=0,
    highlightthickness=0,
    bg="#2C0A59",
    bd=0,
    relief="sunken",
    cursor="hand2",
    activebackground="#2C0A59",
    command=lambda: print("button_2022 clicked"),
    
)
button_2022.place(
    x=22.76129150390624,
    y=111.438201904296,
)

button_2022.bind("<Enter>", lambda e: button_2022.config(image=IWTRwindow.btn_2022active))
button_2022.bind("<Leave>", lambda e: button_2022.config(image=IWTRwindow.btn_2022inactive))


IWTRwindow.btn_2023inactive = PhotoImage(file=relative_to_assets("button_2023.png"))
IWTRwindow.btn_2023active = PhotoImage(file=relative_to_assets("button_2023Active.png"))

button_image_2023 = PhotoImage(
    file=relative_to_assets("button_2023.png"))

button_2023 = Button(
    image=button_image_2023,
    borderwidth=0,
    highlightthickness=0,
    bg="#2C0A59",
    bd=0,
    relief="sunken",
    cursor="hand2",
    activebackground="#2C0A59",
    command=lambda: print("button_2023 clicked"),
    
)

button_2023.place(
    x=173.8081817626953,
    y=112.17134094238281,

)
button_2023.bind("<Enter>", lambda e: button_2023.config(image=IWTRwindow.btn_2023active))
button_2023.bind("<Leave>", lambda e: button_2023.config(image=IWTRwindow.btn_2023inactive))


IWTRwindow.btn_2024inactive = PhotoImage(file=relative_to_assets("button_2024.png"))
IWTRwindow.btn_2024active = PhotoImage(file=relative_to_assets("button_2024Active.png"))

button_image_2024 = PhotoImage(
    file=relative_to_assets("button_2024.png"))

button_2024 = Button(
    image=button_image_2024,
    borderwidth=0,
    highlightthickness=0,
    bg="#2C0A59",
    bd=0,
    relief="sunken",
    cursor="hand2",
    activebackground="#2C0A59",
    command=lambda: print("button_2024 clicked"),
    
)
button_2024.place(
    x=323.07843017578125,
    y=112.90451049804688,

)

button_2024.bind("<Enter>", lambda e: button_2024.config(image=IWTRwindow.btn_2024active))
button_2024.bind("<Leave>", lambda e: button_2024.config(image=IWTRwindow.btn_2024inactive))


IWTRwindow.btn_2025inactive = PhotoImage(file=relative_to_assets("button_2025.png"))
IWTRwindow.btn_2025active = PhotoImage(file=relative_to_assets("button_2025Active.png"))

button_image_2025 = PhotoImage(
    file=relative_to_assets("button_2025.png"))

button_2025 = Button(
    image=button_image_2025,
    borderwidth=0,
    highlightthickness=0,
    bg="#2C0A59",
    bd=0,
    relief="sunken",
    cursor="hand2",
    activebackground="#2C0A59",
    command=lambda: print("button_2025 clicked"),
    
)
button_2025.place(
    x=480.5277099609375,
    y=112.90451049804688,
)

button_2025.bind("<Enter>", lambda e: button_2025.config(image=IWTRwindow.btn_2025active))
button_2025.bind("<Leave>", lambda e: button_2025.config(image=IWTRwindow.btn_2025inactive))

IWTRwindow.btn_IDKinactive = PhotoImage(file=relative_to_assets("button_IDK.png"))
IWTRwindow.btn_IDKactive = PhotoImage(file=relative_to_assets("button_IDKActive.png"))

button_image_IDK = PhotoImage(
    file=relative_to_assets("button_IDK.png"))

button_IDK = Button(
    image=button_image_IDK,
    borderwidth=0,
    highlightthickness=0,
    bg="#2C0A59",
    bd=0,
    activebackground="#2C0A59",
    command=lambda: print("button_IDK clicked"),
    relief="sunken",
    cursor="hand2",
)
button_IDK.place(
    x=651.0565795898438,
    y=111.85713958740234,

)

button_IDK.bind("<Enter>", lambda e: button_IDK.config(image=IWTRwindow.btn_IDKactive))
button_IDK.bind("<Leave>", lambda e: button_IDK.config(image=IWTRwindow.btn_IDKinactive))



image_image_WTR= PhotoImage(
    file=relative_to_assets("WTR.png"))
image_1 = canvas.create_image(
    179.0,
    47.0,
    image=image_image_WTR
)
IWTRwindow.resizable(True, True)
IWTRwindow.mainloop()