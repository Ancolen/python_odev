import tkinter as tk
from tkinter import Text, Button

class ReAssemblePage:
    def __init__(self, master, root_x, root_y):
        self.master = master
        self.top = tk.Toplevel(master)

        # Yeni pencereyi ana pencerenin �zerine a�acak �ekilde konumland�r
        self.top.title("Reverse Text Page")
        self.top.geometry("600x600+{}+{}".format(root_x, root_y))

        # Sayfa ba�l���
        self.label = tk.Label(
            self.top,
            text="PRINT REVERSE OF TEXT AND WORDS",
            fg="white",
            background="navy",
            font=("Georgia", 20, "underline", "bold")
        )
        self.label.place(x=50, y=25)

        # Giri� ve ��k�� alanlar�
        tk.Label(self.top, text="You can write a sentence or text").pack()

        self.inputtxt = Text(self.top, height=10, width=25, bg="white")
        self.inputtxt.pack()

        self.Output = Text(self.top, height=5, width=25, bg="light cyan")
        self.Output.pack()

        # 'Answer' butonu
        self.Display = tk.Button(self.top, height=2, width=20, text="Answer", command=self.display_text)
        self.Display.pack(pady=10)

        # Ana men�ye d�n butonu
        self.simple_button = tk.Button(self.top, text="Return to Main Menu", command=self.return_to_main_menu)
        self.simple_button.pack(pady=10)

    def re_assemble(self, text):
        ntext = text.replace(" ", "")
        return ntext

    def display_text(self):
        # Giri� metnini al ve ters �evirerek ��k��a ekle
        input_text = self.inputtxt.get("1.0", "end-1c")
        reversed_text = self.re_assemble(input_text)
        self.Output.delete("1.0", "end")
        self.Output.insert("end", reversed_text)

    def return_to_main_menu(self):
        # �st pencereyi kapat�r ve ana pencereyi yeniden g�sterir
        self.top.destroy()
        self.master.deiconify()