import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Button


class PrintSplit:
    def __init__(self, master, root_x, root_y):
        self.master = master
        self.top = tk.Toplevel(master)

        # Yeni pencereyi ana pencereyi �zerine a�acak �ekilde konumland�r
        self.top.title("Button 1 Sayfasi")
        self.top.geometry("600x600+{}+{}".format(root_x, root_y))  # Ana pencereyle ayn� konumda a��lacak

        # Sayfa i�eri�i
        self.label = tk.Label(self.top,  # 'root' yerine 'self.top' kullan�ld�
                             text="PRINT LETTERS ONE BELOW THE OTHER",
                             fg="white",
                             background="navy",
                             font=("Georgia", 20, "underline", "bold")
                             )
        self.label.place(x=50, y=25)  # Yerle�imi d�zelttim

        l = tk.Label(self.top, text="You can write a sentence or text")
        l.pack()

        # Input ve Output alanlar�
        self.inputtxt = Text(self.top, height=10, width=25, bg="white")
        self.inputtxt.pack()

        self.Output = Text(self.top, height=5, width=25, bg="light cyan")
        self.Output.pack()

        # Display butonu
        self.Display = tk.Button(self.top, height=2, width=20, text="Answer", command=self.display_text)
        self.Display.pack(pady=10)

        # Ana Men�ye d�n butonu
        self.simple_button = tk.Button(self.top, text="Ana Menuye Don", command=self.return_to_main_menu)
        self.simple_button.pack(pady=10)

    def print_split(self, text):
        words = text.split()
        print(words)
        return words

    def display_text(self):
        input_text = self.inputtxt.get("1.0", "end-1c")
        words = self.print_split(input_text)
        print(words)
        self.Output.delete("1.0", "end")
        formatedtext = str(words)
        self.Output.insert("end", formatedtext)

    def return_to_main_menu(self):
        self.top.destroy()
        self.master.deiconify()  # Ana men�y� tekrar g�ster