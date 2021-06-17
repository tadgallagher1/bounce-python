

# Imports 
import pygame 
import tkinter as tkr  
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")

# Prompt for music directory 
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

# Choose the song to play
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE) 

# Build array of songs
for item in song_list:
    pos=0
    play_list.insert(pos, item) 
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def stop():    
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()
    
def un_pause():    
    pygame.mixer.music.unpause()


Button_Play = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button_Stop = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button_Pause = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button_UnPause = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UN-PAUSE", command=un_pause, bg="orange", fg="white")
    
var = tkr.StringVar()  
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button_Play.pack(fill="x")
Button_Stop.pack(fill="x")
Button_Pause.pack(fill="x")
Button_UnPause.pack(fill="x")

play_list.pack(fill="both", expand="yes")
music_player.mainloop()