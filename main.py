from tkinter import *
from pytube import YouTube, exceptions
from tkinter import filedialog
import os


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

        self.play = Button(self.frame2, bg="red", text="▶", fg="white", bd=0, width=3, height=2, padx=5,
                           command=lambda: self.download(self.link.get()))
        self.play.pack(side=LEFT, anchor=CENTER)

        self.frame3 = Frame(self.window)
        self.frame3.pack()

        self.value_radio_button = IntVar(value=2)

        self.radio1 = Radiobutton(self.frame3, text="Audio", variable=self.value_radio_button, value=0)
        self.radio1.pack(side=LEFT)

        self.radio2 = Radiobutton(self.frame3, text="Video", variable=self.value_radio_button, value=1)
        self.radio2.pack(side=LEFT)

        self.radio3 = Radiobutton(self.frame3, text="Audio e Video", variable=self.value_radio_button, value=2)
        self.radio3.pack(side=LEFT)

        self.window.mainloop()

    def download(self, link):
        try:
            if self.value_radio_button.get() < 3:
                folder = filedialog.askdirectory()
                if not folder or folder.strip() == "" or not os.path.exists(folder):
                    raise TypeError("Invalid folder path.")
                yt = YouTube(link)
                if self.value_radio_button.get() == 0:
                    yt.streams.filter(only_audio=True).first().download(folder)
                elif self.value_radio_button.get() == 1:
                    yt.streams.filter(only_video=True).first().download(folder)
                elif self.value_radio_button.get() == 2:
                    yt.streams.filter(progressive=True, file_extension='mp4').first().download(folder)
                self.send_message("Success!", "Download concluded at\r\n" + folder)

        except exceptions.RegexMatchError:
            self.send_message("ERROR", "Invalid Link provided.")

        except TypeError:
            self.send_message("ERROR", "Invalid destination folder provided.")

    @staticmethod
    def send_message(message_type, message_text):
        window = Toplevel()
        window.title(message_type)
        window.resizable(FALSE, FALSE)
        window.geometry("300x200+300+200")

        Label(window, text=message_text, pady=30, font="Comic 12").pack()

        Button(window, text="OK", command=window.destroy)


YTDownloader()
