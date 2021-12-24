from tkinter import *
import time
import pyttsx3
from tkinter import ttk
import tkinter.ttk as ttk
import webbrowser
import os
from rsap import RSAP
from rsap import AsyncRSAP
import rsap
import win32gui, win32con
import tkinter.scrolledtext as ScrolledText
import sys
from tkinterweb import HtmlFrame

root = Tk()
root.title("Amelia Chatbot v1.0")
root.geometry("1000x500")
root.configure(bg="white")
#root.resizable(width=False, height=False)

#bg = PhotoImage(file="bg.jpg")
canvas1 = Canvas(root, width=500, height=500)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

frame1 = Frame(my_notebook, width=1000, height=500, bg="#ffc3a0")
frame2 = Frame(my_notebook, width=1000, height=500, bg="#ffdde1")
frame3 = Frame(my_notebook, width=1000, height=500, bg="#ffdde1")
frame4 = Frame(my_notebook, width=1000, height=500, bg="#ffdde1")
frame5 = Frame(my_notebook, width=1000, height=500, bg="#ffdde1")

frame1.pack(fill="both", expand=1)
#frame2.pack(fill='both', expand=1)
frame3.pack(fill='both', expand=1)
frame4.pack(fill='both', expand=1)
#frame5.pack(fill='both', expand=1)

my_notebook.add(frame1, text="Amelia Bot")
#my_notebook.add(frame2, text="About")
my_notebook.add(frame3, text="Credits")
my_notebook.add(frame4, text="How to use it")
#my_notebook.add(frame5, text="Web Search")

label10 = Label(frame4, text="The bot will reply to every text you send in the messagebox,", bg="#ffdde1", fg="black",font=("Arial", 20), padx=180, pady=0)
label10.grid(row=1, column=1)
label11 = Label(frame4, text="Write clear to clear the chats. \n Press enter to send the message \n Write exit to exit the program", bg="#ffdde1", fg="black",font=("Arial", 20), padx=270, pady=0)
label11.grid(row=2, column=1)

#my_notebook.add(frame2, text="Details")
label8 = Label(frame3, text="Developed by:", bg="#ffdde1", fg="black",font=("Arial", 30), padx=200, pady=0)
label8.grid(row=1, column=1, padx=180, pady=0)
label9 = Label(frame3, text="Kavin Jindal", bg="#ffdde1", fg="black", font=("Arial", 20), padx=200, pady=0)
label9.grid(row=2, column=1)
btn = Button(frame3, text='Visit Kavin on Github', fg='black', bg='#ffc3a0', font=("Arial", 15), command=lambda: webbrowser.open('https://github.com/kavin-jindal'))
btn.grid(row=3, column=1)
pg_l = Label(frame3, text="\nRandomStuff API", bg="#ffdde1", fg="black",font=("Arial", 30), padx=200, pady=0)
pg_l.grid(row=4, column=1)
rsap_bt = Button(frame3, text='Check out RandomStuff API', fg='black', bg='#ffc3a0', font=("Arial", 15), command=lambda: webbrowser.open("https://www.npmjs.com/package/random-stuff-api"))
rsap_bt.grid(row=5, column=1)
pg2_l = Label(frame3, text="\nPGamerX", bg="#ffdde1", fg="black",font=("Arial", 30), padx=200, pady=0)
pg2_l.grid(row=6, column=1)
btn_pg = Button(frame3, text='Visit PGamerX', fg='black', bg='#ffc3a0', font=("Arial", 15), command=lambda: webbrowser.open('https://pgamerx.com/'))
btn_pg.grid(row=7, column=1)
'''
def search():
    frame = HtmlFrame(frame5)
    frame.load_website(site_url.get())
    frame.pack()'''
def send(event=None):
    if e1.get() == 'clear':
        txt.configure(state='normal')
        txt.delete('1.0', END)
        e1.delete(0, END)
        txt.insert(END, """

▄▀█ █▀▄▀█ █▀▀ █░░ █ ▄▀█
█▀█ █░▀░█ ██▄ █▄▄ █ █▀█


        """)
        txt.insert(END, '[+] Developed by Kavin Jindal \n[+] Powered by RandomStuff API by PGamerX')
        txt.configure(state='disabled')
    elif e1.get() == 'exit':
        sys.exit()
    
       
    else:
        txt.configure(state='normal')
        send="You =>"+e1.get()
        txt.insert(END,"\n\n"+send)
        bot = RSAP(" ", bot_name = 'Amelia', dev_name = 'Kavin Jindal', language = 'en')
        ans = bot.ai_response(e1.get())
        txt.insert(END, '\n\nAmelia =>'+ans)
        e1.delete(0, END)
        txt.configure(state='disabled')
        txt.see(END)
 
txt = ScrolledText.ScrolledText(frame1, font=("Arial", 10), bg='#ffdde1', width=100)
txt.insert(END, """

▄▀█ █▀▄▀█ █▀▀ █░░ █ ▄▀█
█▀█ █░▀░█ ██▄ █▄▄ █ █▀█


""")
txt.insert(END, '[+] Developed by Kavin Jindal \n[+] Powered by RandStuff API by PGamerX')
txt.configure(state='disabled')
txt.grid(row=0, column=0,)
e1=ttk.Entry(frame1,width=100, font=('Arial', 15), text="Chat here")
e1.insert(END, 'Type here')
send1=ttk.Button(frame1, text="Send", command=send)
send1.grid(row=2, column=0, sticky=W)
root.bind('<Return>', send)
e1.grid(row=1, column=0, )

'''
label_s = Label(frame5, text="Search for a website", font=("Arial", 20), bg="#ffdde1", fg="black")
label_s.pack()
site_url = Entry(frame5, width=100, font=('Arial', 15), text="Enter URL")
site_url.pack(side=TOP)
search_btn = Button(frame5, text="Search", command=search())
search_btn.pack(side=TOP)
#site_url.insert(END, 'Enter URL')
'''
root.mainloop()
