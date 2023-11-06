from tkinter import *
import qrcode
from tkinter import messagebox as ms

base = Tk()
base.title("Qr Generator")
base.geometry("1000x500")
base.resizable(False, False)
ft = ("Arial Bold", 15)

def generate():
    nm = title.get()
    url = entry.get()
    check = len(url)

    if check > 0:
        qr=qrcode.make(url)
        qr.save("QrCode/"+str(nm)+".png")
        
        global Img
        Img = PhotoImage(file="QrCode/"+str(nm)+".png")
        image_view = Label(base)
        image_view.config(image=Img)
        image_view.place(x=560, y=100)
        
        ms.showinfo("QR Msg Box", "QR Code Generated Successfully")
    
    else:
        image_view = Label(base,text="No URL Provided ❌")
        image_view.place(x=700, y=180)
        ms.showwarning("Warning Box", "You did not provide an URL")
        title.delete(0, END)

        title.focus()

def clearAll():
    title.delete(0, END)
    entry.delete(0, END)
    title.focus()



lb = Label(base, text="QRCode Generator",font=ft )
lb.place(x=430, y=10)

lb1 = Label(base, text="QR Title : ",font=ft)
lb1.place(x=20, y=100)
title = Entry(base, font=ft, width=30)
title.place(x=120, y=100)
title.focus()

lbl2 = Label(base, text="User Url : ", font=ft)
lbl2.place(x=20, y=150)
entry = Entry(base, width=30, font=ft)
entry.place(x=120, y=150)

btn1 = Button(base, text="Generate", font=ft, command=generate)
btn1.place(x=100, y=200)

btn2 = Button(base, text=" Clear ", font=ft, command=clearAll)
btn2.place(x=260, y=200)

base.mainloop()