import tkinter as tk
import numpy as np 


class SalaryPredictionApp:
    def __init__ (self, root):
        self.root = root
        self.root.title("Salary Prediction App")
        self.root.geometry("500x400")
        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self.root, text="Salary Prediction using Linear Regression", font=("Arial", 28, "bold"), bg = "blue", fg = "white", pady=10)
        header.pack(fill = tk.X)    
        
if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryPredictionApp(root)
    root.mainloop() 