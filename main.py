from user_pwd import Username,Password,Path
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox
from instagrapi import Client
import threading

root =Tk()
root.title("Instagram Reel Downloader")
root.minsize(1058,500)
root.maxsize(1058,500)

HEIGHT = 500
WIDTH = 1058
FONT = font.Font(family ="Times New Roman", size ="19", weight ="bold")


def cmd():
    cd = threading.Timer(1, lambda:download_fn(entry.get()))
    cd.start()


def download_fn(link):
    try:
        button1.configure(state=DISABLED)
        if button1['state'] == DISABLED:
            FONT = font.Font(family ="Times New Roman", size ="12", weight ="bold")
            label5 = Label(frame, text = "In Progress. Please Wait! ", font = FONT, bd =5, fg= "#0d1137",bg="white")
            label5.place(relx = 0.615, rely = 0.5, relheight =0.1)
            root.after(12000, lambda: label5.destroy())
        else:
            pass
        cl = Client()
        cl.login(Username, Password)
        info = cl.media_pk_from_url(link)
        clip_url = cl.media_info(info).video_url
        cl.clip_download_by_url(clip_url, folder = Path)
        messagebox.showinfo('Successful!',rf'Download Successful! Check Your Folder. Path: {Path}')
        button1.configure(state= NORMAL )
    except:
        messagebox.showerror('Error','Please Enter Valid Link')
canvas = Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

frame=Frame(root,bg="white")
frame.place(relwidth=1,relheight=1)

background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Asus\Downloads\Insta_downloads\Logo.jpg"))
background_label = Label(frame, image = background_image)
background_label.place(relx=-0.03,relwidth = 0.62, relheight =1)


label1 = Label(frame, text = "Download Reels In One Click!", font =FONT, bd =5, fg= "#0d1137",bg="white")
label1.place(relx = 0.64, rely = 0.1, relheight =0.1)



FONT = font.Font(family ="Times New Roman", size ="12", weight ="bold")
label2 = Label(frame, text = "Enter link Address: ", font =FONT, bd =5, fg= "black",bg="white")
label2.place(relx = 0.615, rely = 0.25, relheight =0.1)

entry = Entry(frame, font = ("Times New Roman", 11), fg = "black", bg = '#48C9B0')
entry.place(relx = 0.615, rely = 0.35,relwidth=0.38, relheight = 0.07)
entry.insert(0, " Paste Your Link Here")

button1 = Button(root, text = "Download", font = FONT, bg = "#48C9B0", fg = "black", activeforeground = "black", activebackground = "#48C9B0", command=cmd)
button1.place(relx = 0.615,rely = 0.45,relwidth = 0.13, relheight = 0.07)

label2 = Label(frame, text = "Instructions: ", font = FONT, bd =5, fg= "#0d1137",bg="white")
label2.place(relx = 0.615, rely = 0.6, relheight =0.1)

FONT = font.Font(family ="Times New Roman", size ="11", weight ="normal")
label2 = Label(frame, text = "@Imransh1 Github ", font = FONT, bd =5, fg= "#0d1137",bg="white")
label2.place(relx = 0.87, rely = 0.90, relheight =0.1)


TEXT="1. Only public account reels can be downloaded.\n2. Enter the reel link from Instagram.\n3. This is only made for learning purpose.\n4. Any misuse is not advised."
label2 = Label(frame, text = TEXT, font =FONT, bd =5, fg= "#0d1137",justify=LEFT,bg="white")
label2.place(relx = 0.615, rely = 0.7, relheight =0.19)


root.mainloop()