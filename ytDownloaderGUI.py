#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
#from ytdowndl1 import *
#import youtube_dl
import yt_dlp
from termcolor import colored
import os
import shutil
import asyncio
from datetime import datetime
import time
from pydub import AudioSegment

class ytdowndlGUI(Frame):

    def __init__(self, master=None):
        global url
        global e1
        global show_msg
        color = "darkred"
        show_msg = 0

        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self['bg'] = color

        def dwl():
            dText.configure(text= "Downloade...")

        def clearE1():
            e1.delete(0, 'end')

        def dwl_aud():
            ytdl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
                'restrictfilenames': False,
                'noplaylist': True,
                'nocheckcertificate': True,
                'ignoreerrors': False,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'default_search': 'auto',
                'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
            }
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                url = e1.get()
                try:

                    data = ytdl.extract_info(url, download=False)
                    ytdl.download([url])
                    print("1")
                    filename1=ytdl.prepare_filename(data)
                    print("2")
                    #print(filename1)
                    finFilename = data['title'] + ".mp3"

                    base, ext = os.path.splitext(filename1)
                    filename1 = base + ".mp3"
                    try:
                        os.rename(filename1, finFilename)
                    except:
                        finFilename = filename1

                    #print(finFilename)
                    currentPath = os.getcwd()
                    source = "{}/".format(currentPath) + finFilename
                    dest = '/home/jan/Downloads/' + finFilename
                    #os.system("touch -d ""2 hours ago""" +filename2)
                    now = datetime.now()
                    current_time = time.mktime(now.timetuple())
                    os.utime(source, (current_time, current_time))
                    shutil.move(source,dest)
                    out = finFilename+ " wurde im Downloads Ordner gespeichert."
                    sText.configure(text= out, bg= 'green')

                except:
                    sText.configure(text="Fehler", bg= 'red')

        def dwl_vid():
            ytdl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
                'restrictfilenames': False,
                'noplaylist': True,
                'nocheckcertificate': True,
                'ignoreerrors': False,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'default_search': 'auto',
                'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
            }

            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                url = e1.get()
                try:
                    data = ytdl.extract_info(url, download=False)
                    ytdl.download([url])
                    print("1")
                    filename1=ytdl.prepare_filename(data)
                    print("2")
                    #print(filename1)
                    finFilename = data['title'] + ".mp4"
                    base, ext = os.path.splitext(filename1)
                    filename1 = base + ".mp4"
                    try:
                        os.rename(filename1, finFilename)
                    except:
                        finFilename = filename1

                    #print(finFilename)
                    currentPath = os.getcwd()
                    source = "{}/".format(currentPath) + finFilename
                    dest = '/home/jan/Downloads/' + finFilename
                    #os.system("touch -d ""2 hours ago""" +filename2)
                    now = datetime.now()
                    current_time = time.mktime(now.timetuple())
                    os.utime(source, (current_time, current_time))
                    shutil.move(source,dest)
                    out = finFilename+ " wurde im Downloads Ordner gespeichert."
                    sText.configure(text= out, bg= 'green')

                except:
                    sText.configure(text="Fehler", bg= 'red')



        dText = Label(self, text= "", bg = color)
        dText.place(x=30, y=100)
        sText = Label(self, text= "", bg = color)
        sText.place(x=30, y=120)
        lText = Label(self, text="Link eingeben:", bg = color)
        lText.place(x=30, y=20)
        e1 = Entry(font=('Arial', 11), width=50, bg = color)
        e1.place(x=30,y=40)
        button3 = Button(self, text='Download(mp3)', width=15, bg= color,command = lambda:[dwl(), dwl_aud(), clearE1()])
        button3.place(x=30, y=65)
        button4 = button3 = Button(self, text='Download(mp4)', width=15, bg= color,command = lambda:[dwl(), dwl_vid()])
        button4.place(x=180, y=65)


root = Tk()
app = ytdowndlGUI(root)
root.wm_title("YouTube downloader (v.1.2, Jan Meineke)")
root.geometry("610x150")
root.mainloop()
