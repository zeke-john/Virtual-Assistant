from tkinter import *
from googlesearch import *
import webbrowser
import speech_recognition as sr
import threading 

root = Tk()
root.title("        Voice Search")
e = Entry(root, width=39, borderwidth=7)
e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

mic_on = PhotoImage(file = "/home/zeke/Documents/GitHub/Virtual-Assistant/images/mic_on.png") 
mic_off = PhotoImage(file = "/home/zeke/Documents/GitHub/Virtual-Assistant/images/mic_off.png") 

def Listening():
    e = Entry(root, width=39, borderwidth=7)
    e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
    e.insert(0, "Listening...")

def Loading():
    e = Entry(root, width=39, borderwidth=7)
    e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
    e.insert(0, "Loading...")

def button_go():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            btn_go = Button(root, image = mic_on ,text = '.', padx= 150, pady=7, command=threading.Thread(target=button_go).start, activebackground='#ff3333', bg='#5bc75d', compound = CENTER) 
            btn_go.grid(row=1, columnspan=3)
            t1 = threading.Thread(target=Listening)
            t1.start() 
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            t1.join()

            try:
                word = r.recognize_google(audio)
                query = word
                t2 = threading.Thread(target=Loading)
                t2.start() 
                t2.join()

                for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                    webbrowser.open("https://google.com/search?q=%s" % query)
                    e = Entry(root, width=39, borderwidth=7)
                    e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)  
                    e.delete(0, END)
                    btn_go = Button(root, image = mic_off ,text = '.', padx= 150, pady=7, command=threading.Thread(target=button_go).start, activebackground='#ff3333', bg='#5bc75d', compound = CENTER) 
                    btn_go.grid(row=1, columnspan=3)

            except:
                
                e = Entry(root, width=39, borderwidth=7)
                e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
                e.delete(0,END)
                e.insert(0, "Didn't get that, Try again")
                btn_go = Button(root, image = mic_off ,text = '.', padx= 150, pady=7, command=threading.Thread(target=button_go).start, activebackground='#ff3333', bg='#5bc75d', compound = CENTER) 
                btn_go.grid(row=1, columnspan=3)

    except:
        exit()
        quit()

btn_go = Button(root, image = mic_off ,text = '.', padx= 150, pady=7, command=threading.Thread(target=button_go).start, activebackground='#ff3333', bg='#5bc75d', compound = CENTER) 
btn_go.grid(row=1, columnspan=3)
root.resizable(False, False)
root.mainloop()




