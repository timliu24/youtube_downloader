from tkinter import *
import pytube

# Functions
def download():
    video_url = url.get()
    try:
        # URL input from user
        youtube = pytube.YouTube(video_url)
        # Extract the audio file
        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        # Download the file
            #Sample for Windows. Enter your destination path or delete path to save file in current folder.
        video.download('C:/Users/#enter username#/Videos')        
        # Display successful
        notif.config(fg="green", text=youtube.title + " download completed")
    except Exception as error:
        print(error)
        # Display error
        notif.config(fg="red", text="Video could not be downloaded")

# Main GUI
root = Tk()
root.title("Youtube Video Downloader")
# Labels
Label(root, text="Youtube Video Downloader", fg="blue", font=("Arial", 18)).grid(sticky=N, padx=100, pady=10, row=0)
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