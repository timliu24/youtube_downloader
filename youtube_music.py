from tkinter import *
import pytube
import os

# Functions
def download():
    video_url = url.get()
    try:
        # URL input from user
        youtube = pytube.YouTube(video_url)
        # Extract the audio file
        video = youtube.streams.filter(only_audio=True).first()
        # Download the file
        out_file = video.download('C:/Users/# enter your username #/Music')
        # Convert the file to mp3 format
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        # Display successful
        notif.config(fg="green", text=youtube.title + " download completed")
    except Exception as e:
        print(e)
        # Display error
        notif.config(fg="red", text="Music could not be downloaded")

# Main GUI
root = Tk()
root.title("")
# Labels
Label(root, text="", fg="teal", font=("Arial", 18)).grid(sticky=N, padx=100, pady=10, row=0)
Label(root, text="Enter or paste the link of the video below:", font=("Arial", 16)).grid(sticky=N, row=1, pady=10)
notif = Label(root, font=("Arial", 16))
notif.grid(sticky=N, pady=10, row=4)
# Vars
url = StringVar()
# Entry line
Entry(root, width=60, textvariable=url).grid(sticky=N, pady=10, row=2)
# Button
Button(root, width=25, text="Download", font=("Arial", 16), command=download).grid(sticky=N, row=3, pady=15)
root.mainloop()