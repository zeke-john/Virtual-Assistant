from tkinter import *
from googlesearch import *
import webbrowser
import speech_recognition as sr


root = Tk()
root.title("      Searcher")
e = Entry(root, width=39, borderwidth=7)
e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

def button_go():
    e = Entry(root, width=39, borderwidth=7)
    e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
    e.insert(0, END)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Got it, Taking you to " + r.recognize_google(audio))
            word = r.recognize_google(audio)
            query = word
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                e.delete(0, END)

        except Exception as e:
            e = Entry(root, width=39, borderwidth=7)
            e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
            e.insert(0, "Didn't get that, Try again")

btn_go = Button(root, text="Voice Search",padx= 120, pady=15, command=button_go)  
btn_go.grid(row=1, columnspan=3)


root.resizable(False, False)
root.mainloop()