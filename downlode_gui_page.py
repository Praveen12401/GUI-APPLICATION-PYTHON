# from tkinter import*
# from pytube import YouTube
# tab=Tk()
# tab.geometry("600x600")
# tab.minsize(500,500)
#
#
# # only single video downlode now
# link="https://youtu.be/h1CmrQBAifY"
# youtube_1=YouTube(link)
# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)
# videos=youtube_1.streams.all()
# # vid=list(enumerate(videos))
# # for i in vid:
# #     print(i)
# # print()
# strm=int(input("Enter a number :  "))
# def downlode():
#
#     videos[strm].download()
#
# print("succesfully download")
#
#
#
# leble_1=Label(tab,text="ENTER URL :",fg="red",borderwidth=6,padx=33,bg="pink" ).place(x=240,y=60)
#
# b1=Button(tab,text="name",command=downlode)
# tab.mainloop()

import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


# Function to update the download percentage
def update_progress(stream, chunk, bytes_remaining):
    # Calculate the download percentage
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    # Update the status label
    status_label.config(text=f"Downloading... {percent:.2f}%")


# Function to download the video
def download_video():
    # Get the YouTube video URL from the input box
    url = url_input.get()
    # Create a YouTube object with the video URL
    yt = YouTube(url)
    # Get the highest resolution stream available
    stream = yt.streams.get_highest_resolution()
    # Ask the user to select a directory to save the video
    save_path = filedialog.askdirectory()
    # Download the video to the selected directory and update the progress
    stream.download(output_path=save_path)
    # Update the status label
    status_label.config(text="Download complete.")


# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("600x600")
lable1 =tk.Label(root, text="WELCOME MY FORM INFORMETION ", font='comicsansms', fg='red')
lable1.grid(row=0, column=3)
# Create the input box for the YouTube video URL
url_input = tk.Entry(root, width=50, font='comicsansms', fg='red')
url_input.grid(row=3,column=3)

# Create the status label
status_label = tk.Label(root, text="Enter url : ", font='comicsansms', fg='red')
status_label.grid(row=3,column=1)

# Create the button to download the video
download_button = tk.Button(root, text="Download", font='comicsansms', fg='red', command=download_video)
download_button.grid(row=5,column=3)



# Run the main event loop
root.mainloop()
