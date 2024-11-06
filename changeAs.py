
import tkinter as tk
from tkinter import LAST, Text, Button

class changeAs:
    def __init__(self, master, root_x, root_y):
        self.master = master
        self.top = tk.Toplevel(master)

        # Yeni pencereyi ana pencerenin üzerine açacak þekilde konumlandýr
        self.top.title("Reverse Text Page")
        self.top.geometry("600x600+{}+{}".format(root_x, root_y))

        # Sayfa baþlýðý
        self.label = tk.Label(
            self.top,
            text="PRINT REVERSE OF TEXT AND WORDS",
            fg="white",
            background="navy",
            font=("Georgia", 20, "underline", "bold")
        )
        self.label.place(x=50, y=25)

        # Giriþ ve çýkýþ alanlarý
        tk.Label(self.top, text="You can write a sentence or text").pack()

        self.inputtxt = Text(self.top, height=10, width=25, bg="white")
        self.inputtxt.pack()

        self.Output = Text(self.top, height=5, width=25, bg="light cyan")
        self.Output.pack()

        # 'Answer' butonu
        self.Display = tk.Button(self.top, height=2, width=20, text="Answer", command=self.display_text)
        self.Display.pack(pady=10)

        # Ana menüye dön butonu
        self.simple_button = tk.Button(self.top, text="Return to Main Menu", command=self.return_to_main_menu)
        self.simple_button.pack(pady=10)

    def changeAs(self, text):
        lastText = ""
        for word in text:
            if word == "a":
                lastText += "A"
            else:
                lastText += word
        return lastText

    def display_text(self):
        # Giriþ metnini al ve ters çevirerek çýkýþa ekle
        input_text = self.inputtxt.get("1.0", "end-1c")
        ntext = self.changeAs(input_text)
        self.Output.delete("1.0", "end")
        self.Output.insert("end", ntext)

    def return_to_main_menu(self):
        # Üst pencereyi kapatýr ve ana pencereyi yeniden gösterir
        self.top.destroy()
        self.master.deiconify()