from tkinter import *
root=Tk()
root.title("Dictionary")
root.geometry("600x400")

label_of_mutable=Label(root)
label_of_immutable=Label(root)
label_of_tkinter=Label(root)

dictionary={"mutable":"values can be changed just like list",
            "immutable":"values cannot be changed just like tupple",
            "tkinter":"It is the GUI library of python"
            }

def mutable():
    label_of_mutable["text"]=dictionary["mutable"]
    
def immutable():
        label_of_immutable["text"]=dictionary["immutable"]
    
def tkinter():
        label_of_tkinter["text"]=dictionary["tkinter"]   
        
button_mutable=Button(root,text="meaning of Mutable",command=mutable)
button_mutable.place(relx=0.5,rely=0.2,anchor=CENTER)

label_of_mutable.place(relx=0.5,rely=0.3,anchor=CENTER) 

button_immutable=Button(root,text="meaning of Immutable",command=immutable)
button_immutable.place(relx=0.5,rely=0.5,anchor=CENTER)

label_of_immutable.place(relx=0.5,rely=0.6,anchor=CENTER)

button_tkinter=Button(root,text="meaning of Tkinter",command=tkinter)
button_tkinter.place(relx=0.5,rely=0.8,anchor=CENTER)

label_of_tkinter.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()