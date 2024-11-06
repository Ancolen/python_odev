import tkinter as tk
from tkinter import Text, Button


class PrintLettersPage:
    def __init__(self, master, root_x, root_y):
        self.master = master
        self.top = tk.Toplevel(master)

        # Yeni pencereyi ana pencerenin �zerine a�acak �ekilde konumland�r
        self.top.title("PRINT LETTERS")
        self.top.resizable(False, False)
        self.top.minsize(height=650, width=810)

        # Sayfa ba�l���
        self.label = tk.Label(
            self.top,
            text= "PRINT LETTERS ONE BELOW THE OTHER",
            fg = "white",
            background="navy",
            font=("Georgia", 20, "underline", "bold")
        )
        self.label.place(x= 125, y= 25)
        
        self.top.config(background="navy")

        # Giri� ve ��k�� alanlar�
        self.text = tk.Message(self.top, text="You can write a sentence or text", fg="light grey", width=2000, font=("Arial", 14, "bold", "italic"), background="navy")
        self.text.place(x = 250, y=100)
        
        self.inputtxt = Text(self.top, height=10, width=25, bg="white")
        self.inputtxt.place(x = 300, y = 150)

        self.Output = Text(self.top, height=10, width=25, bg="light cyan")
        self.Output.place(x = 300, y = 400)

        # 'Answer' butonu
        self.Display = tk.Button(self.top, height=2, width=20, text="Answer", command=self.display_text)
        self.Display.place(x= 330, y = 330)

        # Ana men�ye d�n butonu
        self.simple_button = tk.Button(self.top, width=20, text="Return to Main Menu", command=self.return_to_main_menu)
        self.simple_button.place(x = 330, y = 570)
        
    def print_letters(self, txt):
        tmp = ""
        for chars in txt:
            tmp += chars + "\n"
        return(tmp)
            
    def display_text(self):
        input_text = self.inputtxt.get("1.0", "end-1c")
        tmp = self.print_letters(input_text)
        self.Output.delete("1.0", "end")
        self.Output.insert("end", tmp)
    
    def return_to_main_menu(self):
        self.top.destroy()
        self.master.deiconify()
    