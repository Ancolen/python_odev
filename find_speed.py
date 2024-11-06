
import tkinter as tk
from tkinter import Text, Button
from datetime import datetime
import re

class FindSpeed:
    def __init__(self, master, root_x, root_y):
        self.master = master
        self.top = tk.Toplevel(master)

        # Yeni pencereyi ana pencerenin �zerine a�acak �ekilde konumland�r
        self.top.title("FIND SPEED")
        self.top.resizable(False, False)
        self.top.minsize(height=650, width=810)

        # Sayfa ba�l���
        self.label = tk.Label(
            self.top,
            text="FIND SPEED",
            fg="white",
            background="navy",
            font=("Georgia", 20, "underline", "bold")
        )
        self.label.place(x= 313, y= 25)
        
        self.top.config(background="navy")
        self.text = tk.Message(self.top, text="You can write a sentence or text", fg="light grey", width=2000, font=("Arial", 14, "bold", "italic"), background="navy")
        self.text.place(x = 250, y=90)
        
        self.inputtxt = Text(self.top, height=10, width=35, bg="white")
        self.inputtxt.place(x = 265, y = 150)

        self.Output = Text(self.top, height=10, width=25, bg="light cyan")
        self.Output.place(x = 300, y = 400)

        # 'Answer' butonu
        self.Display = tk.Button(self.top, height=2, width=20, text="Answer", command=self.display_text)
        self.Display.place(x= 330, y = 330)

        # Ana menüye dön butonu
        self.simple_button = tk.Button(self.top, width=20, text="Back to the Main Menu", command=self.return_to_main_menu)
        self.simple_button.place(x = 330, y = 590)
    
    def find_speed(self, text):
        dtime = datetime.now()
        dtimestamp = dtime.timestamp()

        ddtime = datetime.now()
        ddtimestamp = ddtime.timestamp()

        res = len(re.findall(r'\w+', text))

        tmp = "your score is: ", (ddtimestamp - dtimestamp), "seconds"

        words = (60.0*res)/(ddtimestamp - dtimestamp)

        last = tmp, "\n", "your speed is: ", words, "words per minute"

        return last

    def display_text(self):
        # Giri� metnini al ve ters �evirerek ��k��a ekle
        input_text = self.inputtxt.get("1.0", "end-1c")
        tmp = self.find_speed(input_text)
        self.Output.delete("1.0", "end")
        self.Output.insert("end", tmp)

    def return_to_main_menu(self):
        # �st pencereyi kapat�r ve ana pencereyi yeniden g�sterir
        self.top.destroy()
        self.master.deiconify()