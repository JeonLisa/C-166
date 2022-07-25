from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("600x600")
root.title("Drawing Tool")
root.configure(background="light blue")
label_1=Label(root,text="Enter A Color Name",bg="light blue")
label_1.place(relx=0.7,rely=0.9,anchor=CENTER)
input_1=Entry(root)
input_1.place(relx=0.8,rely=0.9,anchor=CENTER)
input_1.insert(0,"black")
img_1=ImageTk.PhotoImage(Image.open("start_point1.png"))
canvas=Canvas(root,height=510,width=590,bg="white",highlightbackground="lightgray")
canvas.pack()
canvas.create_image(50,50,image=img_1)
direction=""
oldx=50
oldy=50
newx=50
newy=50
def draw(direction,oldx,oldy,newx,newy):
    fillcolor=input_1.get()
root.mainloop()