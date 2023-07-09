from tkinter import *
import smtplib

master=Tk()
master.title("TEJA MAIl APPLICATION")
master.geometry("450x300")

def send():
    try:
        username=temp_username.get()
        password=temp_password.get()
        to=temp_receiver.get()
        subject=temp_subject.get()
        body=temp_body.get()
        if username=="" or password =="" or to=="" or subject=="" or body=="":
            notify.config(text='   All Fields required!   ',fg="red")
            return
        else:
            finalMessage='Subject: {}\n\n{}'.format(subject, body)
            print(username,password,to,finalMessage)
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username,password)
            print("logged in")
            server.sendmail(username,to,finalMessage)
            print(send)
            notify.config(text='Email has been sent',fg="green")
    except:
        notify.config(text="Error sending email",fg="red")    
    


def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')


Label(master,text="Mail Application",font=('Calibri',15)).grid(row=0,sticky=N)
Label(master,text="USE THE FORM BELOW TO SEND AN EMAIL",font=('Calibri',11)).grid(row=1,sticky=W,padx=5)

Label(master,text="EMAIL:  ",font=('Calibri',11)).grid(row=3,sticky=W,padx=5)
Label(master,text="PASSWORD: ",font=('Calibri',11)).grid(row=5,sticky=W,padx=5)
Label(master,text="TO:",font=('Calibri',11)).grid(row=7,sticky=W,padx=5)
Label(master,text="Subject",font=('Calibri',11)).grid(row=9,sticky=W,padx=5)
Label(master,text="BODY:",font=('Calibri',11)).grid(row=11,sticky=W,padx=5)

notify=Label(master,text=" ",font=('Calibri',11))
notify.grid(row=13,sticky=S,padx=5)


temp_username=StringVar()
temp_password=StringVar()
temp_receiver=StringVar()
temp_subject=StringVar()
temp_body=StringVar()


usernameEntry=Entry(master,textvariable=temp_username)
usernameEntry.grid(row=3,column=1)
passwordEntry=Entry(master,show="*",textvariable=temp_password)
passwordEntry.grid(row=5,column=1)
receiverEntry=Entry(master,textvariable=temp_receiver)
receiverEntry.grid(row=7,column=1)
subjectEntry=Entry(master,textvariable=temp_subject)
subjectEntry.grid(row=9,column=1)
bodyEntry=Entry(master,textvariable=temp_body)
bodyEntry.grid(row=11,column=1)


Button(master,text="Send",command=send).grid(row=13,column=1,sticky=W,pady=15,padx=5)
Button(master,text="Reset",command=reset).grid(row=13,column=1,sticky=W,pady=45,padx=45)



master.mainloop()