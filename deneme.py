import tkinter as tk
from tkinter import Text

from changeAs import changeAs
from print_letters import PrintLetters
from print_split import PrintSplit
from re_assemble import ReAssemble
from rev_print1 import RevPrint
from find_speed import find_speed
#from total_vow import TotalVow


class MainMenu:
    root_x = 0
    root_y = 0
    def __init__(self, root):
        self.root = root
        self.root.title("Ana Menu")
        self.root.geometry("500x500")

        # Ana pencerenin ekranýn üst sol köþesinin koordinatlarýný al
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        print(x)
        print(y)
        
        # Butonlarý oluþtur
        self.button1 = tk.Button(root, text="Button 1", command=self.open_button1_page)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(root, text="Button 2", command=self.open_button2_page)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(root, text="Button 3", command=self.open_button3_page)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(root, text="Button 4", command=self.open_button4_page)
        self.button4.pack(pady=10)
        
        self.button5 = tk.Button(root, text="Button 5", command=self.open_button5_page)
        self.button5.pack(pady=10)
        
        self.button6 = tk.Button(root, text="Button 6", command=self.open_button6_page)
        self.button6.pack(pady=10)
        
        self.button7 = tk.Button(root, text="Button 7", command=self.open_button7_page)
        self.button7.pack(pady=10)
        

    def open_button1_page(self):
        # Ana menüyü gizle
        self.root.withdraw()
        # Button 1 sayfasýný aç
        self.button1_page = PrintSplit(self.root, self.root_x, self.root_y)

    def open_button2_page(self):
        self.root.withdraw()
        self.button2_page = ReAssemble(self.root, self.root_x, self.root_y)

    def open_button3_page(self):
        self.root.withdraw()
        self.button3_page = TotalVow(self.root, self.root_x, self.root_y)

    def open_button4_page(self):
        self.root.withdraw()
        self.button4_page = find_speed(self.root, self.root_x, self.root_y)

    def open_button5_page(self):
        self.root.withdraw()
        self.button5_page = RevPrint(self.root, self.root_x, self.root_y)

    def open_button6_page(self):
        self.root.withdraw()
        self.button6_page = changeAs(self.root, self.root_x, self.root_y)

    def open_button7_page(self):
        self.root.withdraw()
        self.button7_page = PrintLetters(self.root, self.root_x, self.root_y)
# Ana pencereyi oluþtur ve sýnýfý baþlat
root = tk.Tk()
page = MainMenu(root)
root.mainloop()