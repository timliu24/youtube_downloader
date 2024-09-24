from tkinter import *
from pytubefix import YouTube
import os

# Functions
def download_video():
    video_url = url.get()
    try:
        # URL input from user
        youtube = YouTube(video_url)
        # Extract the audio file
        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        # Download the file
            #Sample for Windows. Enter your destination path or delete path to save file in current folder.
        video.download('C:/Users/# enter your username #/Videos')        
        # Display successful
        notif.config(fg="green", text=youtube.title + " video download completed")
    except Exception as error:
        print(error)
        # Display error
        notif.config(fg="red", text="Video could not be downloaded")

def download_music():
    video_url = url.get()
    try:
        # URL input from user
        youtube = YouTube(video_url)
        # Extract the audio file
        video = youtube.streams.filter(only_audio=True).first()
        # Download the file
        out_file = video.download('C:/Users/# enter your username #/Music')
        # Convert the file to mp3 format
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        # Display successful
        notif.config(fg="purple", text=youtube.title + " music download completed")
    except Exception as e:
        print(e)
        # Display error
        notif.config(fg="red", text="Music could not be downloaded")

# Main GUI
root = Tk()
root.title("Youtube Downloader")
# Labels
Label(root, text="Youtube Downloader", fg="blue", font=("Arial", 18)).grid(sticky=N, padx=100, pady=10, row=0)
Label(root, text="Enter or paste the link of the video below:", font=("Arial", 16)).grid(sticky=N, row=1, pady=10)
notif = Label(root, font=("Arial", 16))
notif.grid(sticky=N, pady=10, row=3)
Label(root, text="Disclaimer: This App is for education purpose only. We do not support or promote piracy in any way, and discourage unlawful downloading of copyright-protected content.", fg="red", font=("Arial", 8)).grid(sticky=N, padx=20, pady=10, row=7)
# Vars
url = StringVar()
# Entry line
Entry(root, width=60, textvariable=url).grid(sticky=N, pady=10, row=2)
# Button
Button(root, width=25, text="Download Video", font=("Arial", 16), command=download_video).grid(sticky=N, row=4, pady=15)
Button(root, width=25, text="Download Music", font=("Arial", 16), command=download_music).grid(sticky=N, row=5, pady=15)
root.mainloop()