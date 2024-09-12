from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x250")
        screen2.configure(bg="#00db56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii") 
        base64_bytes = base64.b64decode(decode_message) 
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="Decrypted Message:", font=("Helvetica", 12, "bold"), fg="white", bg="#00db56").place(x=10, y=10)
        text2 = Text(screen2, font="Helvetica 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("Encryption", "Please enter the password")

    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid password")

def encrypt():
    password = code.get()
    
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="#ffb3ba")

        message = text1.get(1.0, END) #This line extracts the text from a widget (likely a Text widget in Tkinter) starting from line 1, character 0, up to the end (END).
        encode_message = message.encode("ascii") #Converts the message string into a byte-like object using ASCII encoding. This is necessary to prepare the data for encoding in base64 (as base64 works on byte data).
        base64_bytes = base64.b64encode(encode_message) #This line encodes the encode_message (ASCII-encoded bytes) into a Base64 format. Base64 is a way to represent binary data in an ASCII string format. 
        encrypt = base64_bytes.decode("ascii") #Converts the Base64 encoded bytes back into an ASCII string. This allows the encoded message to be used or displayed as a regular string.

        Label(screen1, text="Encrypted Message:", font=("Helvetica", 12, "bold"), fg="white", bg="#ffb3ba").place(x=10, y=10)
        text2 = Text(screen1, font="Helvetica 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("Encryption", "Please enter the password")

    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid password")

def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("400x420")
    screen.configure(bg="#f0f0f0")
    screen.title("EncrypDecrypApp")

    # Adding a custom icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)

    def reset():
        code.set("")
        text1.delete(1.0, END)

    # Header Label
    Label(text="Enter text for encryption/decryption", fg="black", bg="#f0f0f0", font=("Helvetica", 14, "bold")).place(x=10, y=10)

    # Textbox for message input
    text1 = Text(font=("Helvetica", 12), bg="white", relief=GROOVE, wrap=WORD, bd=2)
    text1.place(x=10, y=50, width=380, height=100)

    # Secret key label and input
    Label(text="Enter secret key:", fg="black", bg="#f0f0f0", font=("Helvetica", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Helvetica", 18), show="*").place(x=10, y=200)

   
    Button(text="ENCRYPT", height=2, width=23, bg="#ff9999", fg="white", bd=0, command=encrypt, font=("Helvetica", 10)).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#99ff99", fg="white", bd=0, command=decrypt, font=("Helvetica", 10)).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="#9999ff", fg="white", bd=0, command=reset, font=("Helvetica", 10)).place(x=10, y=320)

    screen.mainloop()

main_screen()
