from tkinter import *


class YTDownloader:

    def __init__(self):

        self.window = Tk()
        self.window.title("Youtube Downloader")
        self.window.resizable(TRUE, TRUE)
        self.window.geometry("1280x720+25+30")

        self.img_logo = PhotoImage(file="assets/logo.png")

        self.frame = Frame(self.window, background="#3b3b3b", pady=80)
        self.frame.pack(fill="x")

        self.label_logo = Label(self.frame, image=self.img_logo, bg="#3b3b3b")
        self.label_logo.pack()

        self.frame2 = Frame(self.window, pady=20)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text="Insert link:", padx=5, font="Comic 20")
        self.label_insert.pack(side=LEFT)

        self.link = Entry(self.frame2, width=50, font="Comic 12")
        self.link.pack(side=LEFT)

        Label(self.frame2, text=" ", padx=5).pack(side=LEFT)

        self.play = Button(self.frame2, bg="red", text="▶", fg="white", bd=0, command=NONE, width=3, height=2, padx=5)
        self.play.pack(side=LEFT, anchor=CENTER)

        self.window.mainloop()


YTDownloader()
