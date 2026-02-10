from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

set_appearance_mode("light")
topic = "light"

class MenuWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.geometry("250x350")

        self.main_topic = None

        self.sett_img = Image.open("assets/images/icon_sett.png")
        self.sett = CTkImage(light_image=self.sett_img, dark_image=self.sett_img, size=(15, 15))

        self.bg_gif = Image.open("assets/images/cat.gif")
        self.bg_frames = [ImageTk.PhotoImage(frame.copy().resize((250, 350)))
                            for frame in ImageSequence.Iterator(self.bg_gif)]
        self.bg_index = 0
        self.bg_label = CTkLabel(self, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.animate_bg()

        CTkButton(self, text="Play", height=50, width=150, command=self.change_them_main, corner_radius=0).place(x=50, y=225)
        CTkButton(self, text="", image=self.sett, height=15, width=15, command=self.change_them_menu, corner_radius=0).place(x=225, y=5)

    def change_them_menu(self):
        global topic
        if topic == "light":
            self._set_appearance_mode("dark")
            topic = "dark"
        else:
            self._set_appearance_mode("light")
            topic = "light"
        messagebox.showinfo("Topic", f"Now ur topic is {topic}!")
    
    def change_them_main(self):
        self.main_topic = self._get_appearance_mode()
        self.destroy()

    def animate_bg(self):
       self.bg_label.configure(image=self.bg_frames[self.bg_index])
       self.bg_index = (self.bg_index + 1) % len(self.bg_frames)
       self.after(60, self.animate_bg) 