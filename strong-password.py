from tkinter import *
import random

root=Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="#9D98FF")
label= Label(root, fg="white", bg="#9D98FF", font="Arial 12 bold")

array_3d =[[['1','2','3','4','5','6','7','8','9','0'],["!","@","#","$","%","&"],["a","b","c","d","e","f","g","h","i","j","k","l"]]]

def new_password(): 
    random_no_1 = random.randint(0,9)
    random_no_2 = random.randint(0,5)
    random_no_3 = random.randint(0,11)
    random_no_4 = random.randint(0,11)
    random_no_5 = random.randint(0,5)
    random_no_6 = random.randint(0,11)
    random_no_7 = random.randint(0,9)
    random_no_8 = random.randint(0,11)
    random_no_9 = random.randint(0,11)
    random_no_10 = random.randint(0,11)
    
    letter1 =str(array_3d[0][0][random_no_1])
    letter2 =str(array_3d[0][1][random_no_2])
    letter3 =str(array_3d[0][2][random_no_3])
    letter4 =str(array_3d[0][2][random_no_4])
    letter5 =str(array_3d[0][1][random_no_5])
    letter6 =str(array_3d[0][2][random_no_6])
    letter7 =str(array_3d[0][0][random_no_7])
    letter8 =str(array_3d[0][2][random_no_8])
    letter9 =str(array_3d[0][2][random_no_9])
    letter10 =str(array_3d[0][2][random_no_10])
    label["text"] = letter1 + "" + letter2 + "" + letter3 + "" + letter4 + "" + letter5 + "" + letter6 + "" + letter7 + "" + letter8 + "" + letter9 + "" + letter10

btn = Button(root, text= "New Password", command = new_password)

btn.place(relx = 0.5, rely =0.5, anchor = CENTER)
label.place(relx = 0.5, rely =0.6, anchor = CENTER)

root.mainloop()
