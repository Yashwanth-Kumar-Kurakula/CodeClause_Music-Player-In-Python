import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Initialize the User Interface as Tkinter window
root = Tk()
root.title("Groovy Music Player")
root.geometry("485x700+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()

# Global variables
music_paused = False
current_music = None

# Function to add music to the playlist
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        # Add only .mp3 files to the playlist
        for song in songs:
            if song.endswith(".mp3") or song.endswith(".wav"):
                Playlist.insert(END, song)

# Function to play or pause music
def PlayPauseMusic():
    global music_paused, current_music
    if not current_music:
        current_music = Playlist.get(ACTIVE)
        mixer.music.load(current_music)
        mixer.music.play()
        music_paused = False
    elif music_paused:
        mixer.music.unpause()
        music_paused = False
    else:
        mixer.music.pause()
        music_paused = True

# Function to stop music
def StopMusic():
    global current_music
    mixer.music.stop()
    current_music = None

# Create the lower frame
lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0, y=400)

# Set the application icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Create GIF animation
frameCnt = 30
frames = [PhotoImage(file='best.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)

label = Label(root)
label.grid(row=0, column=0, columnspan=5)
root.after(0, update, 0)

# Create play/pause button
ButtonPlayPause = PhotoImage(file="play.png")
Button(root, image=ButtonPlayPause, bg="#FFFFFF", bd=0, height=60, width=60, command=PlayPauseMusic).place(x=215, y=487)

# Create stop button
ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=60, width=60, command=StopMusic).place(x=315, y=487)

# Create volume button
Buttonvolume = PhotoImage(file="volume.png")
Button(root, image=Buttonvolume, bg="#FFFFFF", bd=0, height=60, width=60, command=mixer.music.unpause).place(x=115, y=487)

# Create menu label
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

# Create the music playlist
Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

# Create a button to browse music
Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

# Create a scrollbar for the playlist
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Start the main application loop
root.mainloop()
