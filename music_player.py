def resumem():
    root.resumebutton.grid_remove()
    root.pauseb.grid()
    mixer.music.unpause()
def unmutemusic():

    global current
    root.unmuteb.grid_remove()
    root.muteb.grid()
    mixer.music.set_volume(current)
def mutemusic():
    global current
    root.muteb.grid_remove()
    root.unmuteb.grid()
    current = mixer.music.get_volume()
    mixer.music.set_volume(0)

def stopmusic():
    mixer.music.stop()
def pausemusic():
    mixer.music.pause()
    root.pauseb.grid_remove()
    root.resumebutton.grid()
def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)

def musicplay():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
def musictrack():
    nn = filedialog.askopenfilename()
    audiotrack.set(nn)
def labels():

    #global implay,ipause,iup,idown
    implay = PhotoImage(file='download.png')
    ipause = PhotoImage(file='pause.png')
    iup = PhotoImage(file='vup.png')
    idown = PhotoImage(file='volume-down.png')
    iresume = PhotoImage(file='download.png')

    implay = implay.subsample(2,2)
    ipause = ipause.subsample(2,2)
    iup = iup.subsample(2,2)
    idown = idown.subsample(2,2)
    iresume = iresume.subsample(2, 2)

    TrackLabel= Label(root,text="playing track",bg='lightskyblue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)
    TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'), width=36,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    searchb = Button(root,text='search',bg='yellow',font=('arial',15,'italic bold'),width=20,bd=5,activebackground="red",command=musictrack)
    searchb.grid(row=0,column=2,padx=20,pady=20)
    playb = Button(root, text='play', bg='green', font=('arial', 15, 'italic bold'), width=20,bd=5,activebackground="red",command=musicplay)
    playb.grid(row=1, column=0, padx=20, pady=20)
    stopb = Button(root, text='stop', bg='red', font=('arial', 15, 'italic bold'), width=20, bd=5,activebackground="red",command=stopmusic)
    stopb.grid(row=2, column=0, padx=20, pady=20)
    vupb = Button(root, text='volume up', bg='white', font=('arial', 15, 'italic bold'), width=20, bd=5,activebackground="red",command=volumeup)
    vupb.grid(row=1, column=2, padx=20, pady=20)
    vdownb = Button(root, text='volume down', bg='white', font=('arial', 15, 'italic bold'), width=20, bd=5,activebackground="red",command=volumedown)
    vdownb.grid(row=2, column=2, padx=20, pady=20)
    root.pauseb = Button(root, text='pause', bg='blue', font=('arial', 15, 'italic bold'), width=20, bd=5,activebackground="red",command=pausemusic)
    root.pauseb.grid(row=1, column=1, padx=20, pady=20)
    root.resumebutton = Button(root, text='text', bg='black', font=('arial', 15, 'italic bold'), width=20, bd=5, activebackground="red",command=resumem)
    root.resumebutton.grid(row=1, column=1, padx=20, pady=20)
    root.resumebutton.grid_remove()
    root.muteb =Button(root, text='mute',bg='black',fg='white',font=('times roman',9,'italic bold'),width=15,bd=5,activebackground="red",command=mutemusic)
    root.muteb.grid(row=4,column=2,padx=2,pady=2)
    root.unmuteb = Button(root, text='unmute', bg='black', fg='white', font=('times roman', 9, 'italic bold'), width=10,bd=5, activebackground="red", command=unmutemusic)
    root.unmuteb.grid(row=4, column=2, padx=2, pady=2)
    root.unmuteb.grid_remove()



from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.geometry("1100x500+200+50")
root.title('music player')
root.iconbitmap("mk.ico")
root.resizable(False,False)
root.configure(bg="lightskyblue")
audiotrack = StringVar()
count = 0
text =''
current = 0

k = 'mantosh chutiya hai'
slider = Label(root, text=k,bg='lightskyblue', font=('arial', 40, 'italic bold'))
slider.grid(row=3, column=0, padx=20, pady=20,columnspan = 3)
count = 0
text =''

k = 'mantosh chutiya hai'
def calling():
    global count,text
    if (count>=len(k)):
        count = -1
        text = ''
        slider.configure(text=text)

    else:
        text = text+k[count]
        slider.configure(text=text)
    count += 1
    slider.after(200, calling)


calling()
labels()
mixer.init()
resumem()
root.mainloop()

