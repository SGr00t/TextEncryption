import tkinter as tk
import string


alphabet = "".join(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

root = tk.Tk()
root.title("Text Encryption Tool")
root.config(bg= 'black')
root.geometry("500x500")
Font = ('Arial')
Bg = ('Slate Gray')


def encryption():
    result.delete("1.0", ['end'])
    encrypted_text = ""
    text = user_entry.get("1.0", "end-1c")
    for letter in text:
        letter = letter.lower() 
        if not letter == " ":
            index = alphabet.find(letter)
            if index == -1:
                encrypted_text += letter
            else:
                new_index = index + 4
                if new_index >= len(alphabet):
                    new_index -= len(alphabet)

                encrypted_text += alphabet[new_index]          

    result.insert("1.0", encrypted_text)


def copy():
    
    root.clipboard_clear()
    root.clipboard_append(result.get("1.0", "end-1c"))



lable1 = tk.Label(root, text="Cipher Text editor",font=('Arial', 24), bg='yellow')
lable1.pack(padx=10, pady=10)
lf1 = tk.LabelFrame(root, text="Enter your text Here:",font=(Font, 16), bg=(Bg))
lf1.pack(padx=10, pady=10)
user_entry = tk.Text(lf1, font=(Font),height=5)
user_entry.pack(padx=10, pady=10)
encrypt_button = tk.Button(root, text="ENCRYPT", font=(Font), bg='green', command=(encryption))
encrypt_button.pack(padx=10, pady=10)
lf2 = tk.LabelFrame(root, text="Encrypted Text:", font=(Font, 16), bg=(Bg))
lf2.pack(padx=10, pady=10)
result = tk.Text(lf2, font=(Font), height=5)
result.pack(padx=10, pady=10)
copy_button = tk.Button(root, text="copy", font=(Font), bg='gold', command=(copy))
copy_button.pack(pady=10)

root.mainloop()





