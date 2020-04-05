#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3,TIT2
from tkinter import *

root=Tk()

root.minsize(300,300)

listofsongs=[]
realnames=[]
index=0
v=StringVar()
songlabel=Label(root,textvariable=v,width=35)

def nextsong(event):
    global index
    index+=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
    
def presong(event):
    global index
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
    
def stopsong(event):
    pygame.mixer_music.stop()
    v.set("")

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    
    

def directory_choser():
    directory=askdirectory()
    os.chdir(directory)
    
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            
            realdir=os.path.realpath(files)
            audio=ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            
            listofsongs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()
    
directory_choser()

    
label=Label(root,text="Musicplayer")
label.pack()
  

listbox=Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

    
realnames.reverse()    
#listofsongs.reverse()


nextbutton=Button(root,text="next")
nextbutton.pack()

previousbutton=Button(root,text="pre")
previousbutton.pack()

stopbutton=Button(root,text="stop")
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",presong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
            






root.mainloop()


# In[ ]:





# In[ ]:




