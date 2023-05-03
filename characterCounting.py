import tkinter as tk
from collections import Counter

class CharacterCount:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Character Count")
        self.window.geometry("500x400")
        self.window.configure(bg='#f2f2f2')
        
        self.label = tk.Label(self.window, text="Enter a string:", font=("Helvetica", 16), bg='#f2f2f2')
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.window, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        
        self.button = tk.Button(self.window, text="Count", command=self.count_characters, font=("Helvetica", 16), bg='#009688', fg='white', activebackground='#26a69a', activeforeground='white')
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(self.window, text="", font=("Helvetica", 15, "bold"), bg='#f2f2f2')
        self.result_label.pack(pady=10)
        
        self.window.mainloop()
        
    def count_characters(self):
        text = self.entry.get()
        character_count = Counter(text)
        result = "The number of Character frequency:\n"
        
        for char, count in character_count.items():    
            result += f"{count} {char}'s\n"

        self.result_label.configure(text=result)

CharacterCount()
