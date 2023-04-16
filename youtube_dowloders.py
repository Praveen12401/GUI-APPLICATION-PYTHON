from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

tab=Tk()
# tab.withdraw()


# ask the user to select a dictionary
#
# def path():
#     dictionary_path = filedialog.askdirectory()



# only single video downlode now
def download():
    # link="https://youtu.be/s7Kh-hV2vOU"
    url= url_value.get()
    print(url)
    messagebox.showinfo("url",url)
    youtube_1 = YouTube(url)
    # print(youtube_1.title)
    # print(youtube_1.thumbnail_url)

    dictionary_path = filedialog.askdirectory()

    videos = youtube_1.streams.get_highest_resolution()
    videos.download("dictionary_path")







tab.geometry("600x600")
tab.minsize(500, 500)
tab['bg'] = "pink"
l=Label(tab,text=" SELECT  PATH  FOR  VIDEO : ",fg="red",bg="yellow").place(x=50,y=110)
# path display code
entry_2 = Button(tab,text="select path", fg="red", bg="yellow", relief=SUNKEN,command=filedialog.askdirectory).place(x=250, y=110)
lable_1 = Label(tab, text="ENTER VIDEVO URL : ", fg="red", bg="yellow").place(x=50, y=50)
entry_1 = Entry(tab, textvariable='url_value', relief=SUNKEN, width=60).place(x=230, y=50)

lable_2 = Label(tab, text="AUTO HIGH VIDEO QUALITY : ", fg="red", bg="yellow").place(x=50, y=150)

#  take  a value from  user for video link
url_value = StringVar()


#  take  a value from  user for path
# path_ = StringVar()
# path_value= url_.get()

# #create  botton downlode funtion

b1 = Button(tab, text="Downlode", fg="red", bg="yellow", command=download).place(x=200,y=300)

tab.mainloop()

